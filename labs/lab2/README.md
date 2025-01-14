# GridWorld và Value Function

## Giới thiệu

Dự án này là một ví dụ minh họa về cách xây dựng môi trường lưới (GridWorld) và hàm giá trị (Value Function) trong lĩnh vực **Học tăng cường (Reinforcement Learning)**.  

GridWorld là một môi trường cơ bản được sử dụng rộng rãi để minh họa các khái niệm cốt lõi trong học tăng cường, chẳng hạn như phần thưởng (reward), trạng thái (state), và giá trị của trạng thái (state value).  

## Cấu trúc mã

### 1. `GridWorld`
Lớp `GridWorld` đại diện cho môi trường lưới 2D, với các đặc điểm chính:
- **Kích thước**: 3x3.
- **Phần thưởng**: Mỗi ô (trạng thái) có một giá trị phần thưởng, cụ thể:
  - Các ô thông thường: `0`.
  - Ô ở góc dưới bên phải: `+1`.
- **Phương thức**:
  - `get_reward(state)`: Trả về phần thưởng tại một trạng thái cụ thể.

### 2. `ValueFunction`
Lớp `ValueFunction` lưu trữ và quản lý giá trị của từng trạng thái:
- Giá trị ban đầu của các trạng thái được khởi tạo bằng `0`.
- Có thể **cập nhật** và **truy vấn** giá trị của một trạng thái thông qua các phương thức:
  - `update_value(state, new_value)`: Cập nhật giá trị mới cho trạng thái.
  - `get_value(state)`: Trả về giá trị của trạng thái.

## Mô tả thuật toán

1. **Khởi tạo môi trường**:
   - Xác định kích thước lưới và phần thưởng tại mỗi trạng thái.

2. **Khởi tạo hàm giá trị**:
   - Giá trị ban đầu của mỗi trạng thái được gán bằng phần thưởng tại trạng thái đó.

3. **In giá trị ban đầu của hàm giá trị**:
   - In ma trận giá trị, trùng với ma trận phần thưởng.

## Mã nguồn

```python
import numpy as np

class GridWorld:
    def __init__(self):
        self.grid_size = (3, 3)
        self.num_actions = 4
        self.rewards = np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 1, 0]
        ])
    
    def get_reward(self, state):
        return self.rewards[state[0], state[1]]

class ValueFunction:
    def __init__(self, grid_size):
        self.values = np.zeros(grid_size)
        
    def update_value(self, state, new_value):
        self.values[state[0], state[1]] = new_value
        
    def get_value(self, state):
        return self.values[state[0], state[1]]

grid_world = GridWorld()
value_function = ValueFunction(grid_world.grid_size)

for i in range(grid_world.grid_size[0]):
    for j in range(grid_world.grid_size[1]):
        state = (i, j)
        value_function.update_value(state, grid_world.get_reward(state))

print("Initial Value Function:")
print(value_function.values)
