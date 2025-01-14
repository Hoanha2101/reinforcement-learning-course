import numpy as np

# Lớp GridWorld đại diện cho môi trường lưới 3x3
class GridWorld:
    def __init__(self):
        # Kích thước của lưới (3x3)
        self.grid_size = (3, 3)
        # Số hành động có thể thực hiện trong môi trường (Lên, Xuống, Trái, Phải)
        self.num_actions = 4
        # Ma trận phần thưởng, phần thưởng +1 ở ô góc dưới
        self.rewards = np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 1, 0]  # Phần thưởng +1 tại ô (2, 1) (dòng thứ 3, cột thứ 2)
        ])
    
    # Hàm để lấy phần thưởng của một trạng thái (ô cụ thể trên lưới)
    def get_reward(self, state):
        return self.rewards[state[0], state[1]]


# Lớp ValueFunction đại diện cho hàm giá trị của từng trạng thái trong lưới
class ValueFunction:
    def __init__(self, grid_size):
        # Khởi tạo ma trận giá trị với giá trị ban đầu bằng 0
        self.values = np.zeros(grid_size)
        
    # Hàm cập nhật giá trị mới cho một trạng thái cụ thể
    def update_value(self, state, new_value):
        self.values[state[0], state[1]] = new_value
        
    # Hàm trả về giá trị của một trạng thái cụ thể
    def get_value(self, state):
        return self.values[state[0], state[1]]


# Tạo một môi trường lưới 3x3
grid_world = GridWorld()

# Tạo một hàm giá trị cho môi trường lưới
value_function = ValueFunction(grid_world.grid_size)

# Khởi tạo giá trị ban đầu của hàm giá trị bằng phần thưởng tại mỗi ô
for i in range(grid_world.grid_size[0]):  # Duyệt qua từng dòng của lưới
    for j in range(grid_world.grid_size[1]):  # Duyệt qua từng cột của lưới
        state = (i, j)  # Tạo trạng thái đại diện cho vị trí (i, j) trong lưới
        # Cập nhật giá trị trạng thái bằng phần thưởng tại trạng thái đó
        value_function.update_value(state, grid_world.get_reward(state))
        print(value_function.values)
        

# In giá trị ban đầu của hàm giá trị (chính là ma trận phần thưởng)
print("Initial Value Function:")
print(value_function.values)
