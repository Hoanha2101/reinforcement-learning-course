import random

import gym
import numpy as np

# Tạo môi trường MountainCar-v0
env = gym.make("MountainCar-v0")
env.reset()

# Các hằng số cho thuật toán Q-learning
c_learning_rate = 0.1  # Tốc độ học (alpha)
c_discount_value = 0.9  # Hệ số chiết khấu (gamma)
c_no_of_eps = 10000  # Số lượng episode để huấn luyện
c_show_each = 1000  # Hiển thị mỗi c_show_each episode

# Tham số epsilon cho chiến lược epsilon-greedy
v_epsilon = 0.9  # Giá trị ban đầu của epsilon (tỉ lệ explore)
c_start_ep_epsilon_decay = 1  # Episode bắt đầu giảm epsilon
c_end_ep_epsilon_decay = c_no_of_eps // 2  # Episode kết thúc giảm epsilon
v_epsilon_decay = v_epsilon / (c_end_ep_epsilon_decay - c_start_ep_epsilon_decay)  # Tốc độ giảm epsilon

# Kích thước của Q-table
q_table_size = [20, 20]  # Số ô phân chia không gian trạng thái
q_table_segment_size = (env.observation_space.high - env.observation_space.low) / q_table_size  # Kích thước từng ô

# Hàm chuyển đổi từ trạng thái thực tế về chỉ mục Q-table
def convert_state(real_state):
    q_state = (real_state - env.observation_space.low) // q_table_segment_size
    return tuple(q_state.astype(int))

# Khởi tạo Q-table với giá trị ngẫu nhiên trong khoảng [-2, 0]
q_table = np.random.uniform(low=-2, high=0, size=(q_table_size + [env.action_space.n]))

# Biến theo dõi phần thưởng cao nhất đạt được
max_ep_reward = -999  # Giá trị phần thưởng lớn nhất tìm thấy
max_ep_action_list = []  # Danh sách hành động tương ứng với phần thưởng cao nhất
max_start_state = None  # Trạng thái bắt đầu tương ứng với phần thưởng cao nhất

# Vòng lặp huấn luyện Q-learning
for ep in range(c_no_of_eps):
    print("Eps = ", ep)
    done = False  # Cờ kiểm tra khi nào episode kết thúc
    current_state, _ = env.reset()  # Reset môi trường
    current_state = convert_state(current_state)  # Chuyển đổi trạng thái
    ep_reward = 0  # Khởi tạo phần thưởng của episode
    ep_start_state = current_state  # Lưu trạng thái bắt đầu
    action_list = []  # Lưu danh sách hành động của episode

    # Xác định có hiển thị môi trường hay không
    show_now = (ep % c_show_each == 0)

    while not done:
        # Chọn hành động theo epsilon-greedy
        if np.random.random() > v_epsilon:
            action = np.argmax(q_table[current_state])  # Khai thác (exploit)
        else:
            action = np.random.randint(0, env.action_space.n)  # Thử nghiệm (explore)

        action_list.append(action)  # Lưu lại hành động

        # Thực hiện hành động và nhận kết quả
        next_real_state, reward, done, _, info = env.step(action)
        ep_reward += reward  # Cộng dồn phần thưởng

        if show_now:
            env.render()  # Hiển thị môi trường

        if done:
            # Kiểm tra xem có đến được vị trí mục tiêu không
            if next_real_state[0] >= env.goal_position:
                print("Đã đến cờ tại ep = {}, reward = {}".format(ep, ep_reward))
                if ep_reward > max_ep_reward:
                    max_ep_reward = ep_reward
                    max_ep_action_list = action_list
                    max_start_state = ep_start_state
        else:
            # Chuyển đổi trạng thái tiếp theo sang chỉ mục Q-table
            next_state = convert_state(next_real_state)

            # Cập nhật giá trị Q-value bằng phương trình Bellman
            current_q_value = q_table[current_state + (action,)]
            new_q_value = (1 - c_learning_rate) * current_q_value + c_learning_rate * (reward + c_discount_value * np.max(q_table[next_state]))
            q_table[current_state + (action,)] = new_q_value

            # Chuyển sang trạng thái tiếp theo
            current_state = next_state
    
    # Giảm dần epsilon trong khoảng xác định
    if c_end_ep_epsilon_decay >= ep > c_start_ep_epsilon_decay:
        v_epsilon = v_epsilon - v_epsilon_decay

# Hiển thị kết quả tốt nhất tìm được
print("Max reward = ", max_ep_reward)
print("Max action list = ", max_ep_action_list)

# Phát lại tập tốt nhất tìm được
env.reset()
env.state = max_start_state  # Đặt trạng thái ban đầu thành trạng thái tốt nhất
for action in max_ep_action_list:
    env.step(action)  # Thực hiện hành động
    env.render()  # Hiển thị môi trường

# Duy trì môi trường ở trạng thái đứng yên sau khi chạy xong
done = False
while not done:
    _, _, done, _ = env.step(0)  # Giữ xe ở trạng thái không di chuyển
    env.render()
