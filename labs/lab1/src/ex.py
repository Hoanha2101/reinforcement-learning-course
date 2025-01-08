import numpy as np

# Lớp EpsilonGreedyAgent đại diện cho agent (người chơi) áp dụng chiến lược epsilon-greedy
class EpsilonGreedyAgent:
    def __init__(self, num_actions, epsilon=0.1):
        """
        Hàm khởi tạo agent epsilon-greedy.
        - num_actions: Số hành động có thể thực hiện.
        - epsilon: Xác suất chọn hành động ngẫu nhiên (khám phá).
        """
        self.num_actions = num_actions  # Số hành động có thể thực hiện
        self.epsilon = epsilon          # Xác suất khám phá
        self.action_values = np.zeros(num_actions)  # Giá trị kỳ vọng của từng hành động
        self.action_counts = np.zeros(num_actions)  # Số lần thực hiện mỗi hành động

    def select_action(self):
        """
        Chọn hành động dựa trên chiến lược epsilon-greedy:
        - Với xác suất epsilon: chọn hành động ngẫu nhiên (khám phá).
        - Với xác suất 1 - epsilon: chọn hành động có giá trị kỳ vọng lớn nhất (khai thác).
        """
        if np.random.rand() < self.epsilon:
            # Khám phá - exploration: chọn hành động ngẫu nhiên
            action = np.random.randint(self.num_actions)
        else:
            # Khai thác - exploitation: chọn hành động có giá trị kỳ vọng lớn nhất
            action = np.argmax(self.action_values)
        return action

    def update_value(self, action, reward):
        """
        Cập nhật giá trị kỳ vọng của hành động vừa thực hiện bằng công thức:
        Q(a) <- Q(a) + (1/N) * (r - Q(a))
        - action: Hành động vừa thực hiện.
        - reward: Phần thưởng nhận được sau hành động.
        """
        self.action_counts[action] += 1  # Tăng số lần thực hiện hành động này
        # Cập nhật giá trị kỳ vọng của hành động dựa trên phần thưởng mới nhận được
        self.action_values[action] += (1 / self.action_counts[action]) * (reward - self.action_values[action])

# Lớp MultiArmedBandit mô phỏng môi trường multi-armed bandit
class MultiArmedBandit:
    def __init__(self, num_arms):
        """
        Hàm khởi tạo môi trường multi-armed bandit.
        - num_arms: Số lượng cánh tay (hành động).
        """
        self.num_arms = num_arms  # Số cánh tay
        # Giá trị thực sự của mỗi hành động, được lấy ngẫu nhiên từ phân phối chuẩn N(0, 1)
        self.true_action_values = np.random.normal(0, 1, num_arms)

    def get_reward(self, action):
        """
        Trả về phần thưởng khi thực hiện hành động.
        - Phần thưởng được lấy từ phân phối chuẩn có trung bình là giá trị thực của hành động.
        """
        return np.random.normal(self.true_action_values[action], 1)

# Số lượng cánh tay (hành động) của bandit
num_arms = 10
# Số bước tương tác giữa agent và môi trường
num_steps = 1000

# Tạo một agent epsilon-greedy
agent = EpsilonGreedyAgent(num_arms)

# Tạo môi trường multi-armed bandit
bandit = MultiArmedBandit(num_arms)

# Tổng phần thưởng nhận được
total_rewards = 0

# Vòng lặp tương tác giữa agent và môi trường
for step in range(num_steps):
    # Agent chọn một hành động
    action = agent.select_action()
    # Môi trường trả về phần thưởng cho hành động đó
    reward = bandit.get_reward(action)
    # Agent cập nhật giá trị kỳ vọng của hành động dựa trên phần thưởng nhận được
    agent.update_value(action, reward)
    # Cộng phần thưởng vào tổng phần thưởng
    total_rewards += reward

# Hiển thị kết quả
print("Tổng phần thưởng nhận được:", total_rewards)
print("Giá trị kỳ vọng ước lượng của các hành động:", agent.action_values)
