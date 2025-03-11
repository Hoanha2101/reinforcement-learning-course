# Q-Learning với MountainCar-v0

Đây là một triển khai của thuật toán **Q-Learning** để giải quyết bài toán **MountainCar-v0** trong OpenAI Gym.

## 🛠 Cài đặt

Trước khi chạy mã, bạn cần cài đặt thư viện cần thiết:

```bash
pip install numpy gym
```

## 📜 Mô tả

Bài toán **MountainCar-v0** yêu cầu một chiếc xe leo lên đỉnh dốc bằng cách lắc lư qua lại để lấy động lượng. Thuật toán **Q-Learning** được sử dụng để học cách điều khiển xe một cách hiệu quả.

### 🚗 Môi trường:
- **Trạng thái (State):**
  - Vị trí hiện tại của xe.
  - Vận tốc của xe.
- **Hành động (Action):**
  - 0: Di chuyển trái.
  - 1: Không làm gì.
  - 2: Di chuyển phải.
- **Phần thưởng (Reward):**
  - `-1` cho mỗi bước đi để khuyến khích xe về đích nhanh nhất.
  - Nếu xe đạt đến mục tiêu (cờ đỏ), tập sẽ kết thúc.

## 🔢 Tham số Q-Learning

| Tham số | Giá trị |
|---------|--------|
| Learning rate (alpha) | 0.1 |
| Discount factor (gamma) | 0.9 |
| Epsilon (ban đầu) | 0.9 |
| Số episode huấn luyện | 10,000 |
| Hiển thị mỗi | 1,000 episode |
| Số phân đoạn trạng thái | 20x20 |

## 🏗 Cách thức hoạt động

1. **Khởi tạo Q-table** với giá trị ngẫu nhiên từ -2 đến 0.
2. **Huấn luyện bằng Q-Learning**
   - Chọn hành động theo chiến lược **Epsilon-Greedy**.
   - Cập nhật giá trị Q-value theo phương trình Bellman.
   - Giảm dần epsilon theo thời gian để giảm dần việc thử nghiệm.
3. **Lưu lại tập tốt nhất** có phần thưởng cao nhất.
4. **Chạy lại tập tốt nhất** để quan sát kết quả.

## ▶️ Chạy chương trình

Để chạy mã, sử dụng lệnh sau trong terminal:

```bash
python MountainCar.py
```

Chương trình sẽ hiển thị môi trường sau mỗi 1,000 episode và lưu lại tập có phần thưởng tốt nhất.

## 📈 Kết quả

- Chương trình sẽ hiển thị **phần thưởng cao nhất** đạt được.
- **Danh sách hành động tốt nhất** giúp xe về đích nhanh nhất.
- **Phát lại tập tốt nhất** để kiểm tra hiệu quả của mô hình.

## 📌 Ghi chú
- Bạn có thể điều chỉnh các tham số như `c_learning_rate`, `c_discount_value`, `v_epsilon`, `q_table_size` để tối ưu kết quả.
- Nếu muốn hiển thị môi trường nhiều hơn, giảm giá trị `c_show_each`.

## 📜 Bản quyền
Mã nguồn được cung cấp miễn phí và có thể sử dụng cho mục đích học tập hoặc nghiên cứu.