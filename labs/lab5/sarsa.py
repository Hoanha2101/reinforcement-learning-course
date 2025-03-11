import numpy as np
import gym
#tạo ra môi trường FrozenLake, nơi agent (người chơi) cần tìm cách đi từ vị trí bắt đầu đến mục tiêu tránh rơi xuống hố băng
env = gym.make('FrozenLake-v1')

# Defining parameters
epsilon = 0.9  # Xác suất chọn hành động ngẫu nhiên (exploration rate)
total_episodes = 10000  # Số tập huấn luyện
max_steps = 100  # Số bước tối đa trong mỗi tập
alpha = 0.85  # Tốc độ học (learning rate)
gamma = 0.95  # Hệ số chiết khấu (discount factor)

# Initializing Q-table
Q = np.zeros((env.observation_space.n, env.action_space.n))

print("Q.shape:", Q.shape)

# Function to choose an action
def choose_action(state): 
    if np.random.uniform(0, 1) < epsilon: 
        return env.action_space.sample() 
    else: 
        return np.argmax(Q[state, :])

# Function to update Q-values (SARSA)
def update(state, state2, reward, action, action2): 
    predict = Q[state, action] 
    target = reward + gamma * Q[state2, action2] 
    Q[state, action] = Q[state, action] + alpha * (target - predict) 

# SARSA training
for episode in range(total_episodes): 
    state1, _ = env.reset()  # Khởi tạo trạng thái ban đầu
    action1 = choose_action(state1)  # Chọn hành động đầu tiên
    t = 0 
    while t < max_steps: 
        env.render()  # Hiển thị môi trường (tùy chọn)
        
        state2, reward, done, _, info = env.step(action1)  # Thực hiện hành động
        # print(state2)
        
        action2 = choose_action(state2)  # Chọn hành động tiếp theo
        
        update(state1, state2, reward, action1, action2)  # Cập nhật Q-value
        
        state1 = state2  # Chuyển sang trạng thái mới
        action1 = action2  # Chuyển sang hành động mới
        
        t += 1 
        reward += 1 
        
        if done: 
            break

# Evaluating the performance 
print("Performance: ", reward / total_episodes) 
print(Q)
