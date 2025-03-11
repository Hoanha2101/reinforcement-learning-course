import numpy as np

class GridWorld:
    def __init__(self):
        self.grid_size = (3, 3)
        self.num_actions = 4 
        self.start_state = (0, 0)  
        self.goal_state = (2, 2)  

    def step(self, state, action):
        """
        Mô tả động lực học của môi trường.
        Trả về trạng thái tiếp theo và phần thưởng sau khi thực hiện hành động.
        """
        row, col = state
        if action == 0:  # Up
            row = max(0, row - 1)
        elif action == 1:  # Down
            row = min(self.grid_size[0] - 1, row + 1)
        elif action == 2:  # Left
            col = max(0, col - 1)
        elif action == 3:  # Right
            col = min(self.grid_size[1] - 1, col + 1)

        next_state = (row, col)
        reward = 1 if next_state == self.goal_state else 0 

        return next_state, reward


class ActorCritic:
    def __init__(self, num_actions, alpha_actor, alpha_critic, gamma):
        """
        Khởi tạo agent Actor-Critic
        """
        self.num_actions = num_actions
        self.alpha_actor = alpha_actor  # Hệ số học cho Actor
        self.alpha_critic = alpha_critic  # Hệ số học cho Critic
        self.gamma = gamma  # Hệ số chiết khấu

        # Tham số của Actor (bảng xác suất hành động theo trạng thái)
        self.actor_params = np.zeros((3, 3, num_actions))  
        
        # Hàm giá trị Critic (giá trị trạng thái)
        self.critic_values = np.zeros((3, 3))  

    def select_action(self, state):
        """
        Chọn hành động dựa trên xác suất từ Actor.
        """
        action_probs = self.softmax(self.actor_params[state])
        action = np.random.choice(self.num_actions, p=action_probs)  # Chọn hành động theo phân phối xác suất
        return action

    def update(self, state, action, reward, next_state):
        """
        Cập nhật giá trị Critic và tham số Actor dựa trên sai số TD (Temporal Difference).
        """
        # Tính TD error (sai số giá trị)
        td_error = reward + self.gamma * self.critic_values[next_state] - self.critic_values[state]

        # Cập nhật Critic (hàm giá trị trạng thái)
        self.critic_values[state] += self.alpha_critic * td_error

        # Cập nhật Actor (chính sách xác suất)
        self.actor_params[state][action] += self.alpha_actor * td_error

    def softmax(self, x):
        """
        Tính softmax để chuyển đổi giá trị thành xác suất.
        """
        e_x = np.exp(x - np.max(x))  
        return e_x / e_x.sum(axis=0)


# Tạo môi trường GridWorld
grid_world = GridWorld()


num_actions = 4  
alpha_actor = 0.1  # Learning rate cho Actor
alpha_critic = 0.1  # Learning rate cho Critic
gamma = 0.9  # Hệ số chiết khấu

actor_critic_agent = ActorCritic(num_actions, alpha_actor, alpha_critic, gamma)

# Huấn luyện Actor-Critic
num_episodes = 1000
for _ in range(num_episodes):
    state = grid_world.start_state
    while state != grid_world.goal_state:
        action = actor_critic_agent.select_action(state)
        next_state, reward = grid_world.step(state, action)
        actor_critic_agent.update(state, action, reward, next_state)
        state = next_state

# Đánh giá chính sách học được
total_reward = 0
state = grid_world.start_state
while state != grid_world.goal_state:
    action = actor_critic_agent.select_action(state)
    next_state, reward = grid_world.step(state, action)
    total_reward += reward
    state = next_state

print("Total reward obtained by learned policy:", total_reward)
