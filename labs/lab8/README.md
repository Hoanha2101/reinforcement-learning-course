# Actor-Critic Algorithm for GridWorld

Đây là một triển khai thuật toán **Actor-Critic** để học chính sách tối ưu trong môi trường **GridWorld**.

## 🛠 Cài đặt

Trước khi chạy mã, bạn cần cài đặt thư viện cần thiết:

```bash
pip install numpy
```

## 📜 Mô tả

Bài toán **GridWorld** mô phỏng một môi trường dạng lưới 3x3, trong đó agent di chuyển theo các hướng **Lên, Xuống, Trái, Phải** và nhận phần thưởng khi đến ô đích.

### 🎯 Môi trường
- Lưới có kích thước **3x3**.
- Số hành động có thể thực hiện: **4 hành động (Lên, Xuống, Trái, Phải)**.
- Phần thưởng:
  - Ô (2,2) có phần thưởng **+1**.
  - Các ô còn lại có phần thưởng **0**.
- Trạng thái bắt đầu: **(0,0)**.
- Trạng thái kết thúc: **(2,2)**.

### 🏗 Cách thức hoạt động

1. **Tạo môi trường GridWorld**:
   - Xác định kích thước lưới và phần thưởng tại từng ô.
   - Định nghĩa quy tắc di chuyển (step function).

2. **Thuật toán Actor-Critic**:
   - **Critic**: Học giá trị trạng thái \( V(s) \) để đánh giá hành động.
   - **Actor**: Điều chỉnh chính sách xác suất hành động \( \pi(a | s) \).
   - **Cập nhật Actor và Critic theo sai số TD**:
     
     $$ \delta = r + \gamma V(s') - V(s) $$
     
     - **Critic Update**:
       
       $$ V(s) \leftarrow V(s) + \alpha_{critic} \cdot \delta $$
       
     - **Actor Update**:
       
       $$ \pi(a | s) \leftarrow \pi(a | s) + \alpha_{actor} \cdot \delta $$

3. **Huấn luyện Actor-Critic**:
   - Khởi tạo giá trị trạng thái và chính sách hành động.
   - Lặp lại trong `num_episodes` lần.
   - Chọn hành động theo **Softmax Policy**.
   - Cập nhật Actor và Critic dựa trên sai số TD.
   - Kết thúc khi đến trạng thái mục tiêu **(2,2)**.

## 🔢 Tham số chính

| Tham số | Giá trị |
|---------|--------|
| Kích thước lưới | 3x3 |
| Số hành động | 4 |
| Số tập huấn luyện | 1000 |
| Learning rate (alpha_actor) | 0.1 |
| Learning rate (alpha_critic) | 0.1 |
| Discount factor (gamma) | 0.9 |

## ▶️ Chạy chương trình

Để chạy mã, sử dụng lệnh sau trong terminal:

```bash
python actor_critic_gridworld.py
```

Chương trình sẽ hiển thị tổng phần thưởng thu được bằng chính sách học được:

```
Total reward obtained by learned policy: X
```

(X là tổng phần thưởng thu được sau khi áp dụng chính sách học được)

## 📈 Kết quả mong đợi
- **Critic** sẽ học được giá trị trạng thái tối ưu.
- **Actor** sẽ học được chính sách xác suất hành động.
- **Chính sách học được** sẽ dẫn agent đến trạng thái mục tiêu với phần thưởng tối ưu.

## 📌 Ghi chú
- Actor-Critic kết hợp giữa **Value-Based (Critic)** và **Policy-Based (Actor)** để cải thiện chính sách.
- Bạn có thể thay đổi **alpha_actor** và **alpha_critic** để kiểm tra ảnh hưởng của tốc độ học.
- Softmax Policy đảm bảo việc chọn hành động **có tính xác suất**, giúp tránh tối ưu cục bộ.

## 📜 Bản quyền
Mã nguồn được cung cấp miễn phí và có thể sử dụng cho mục đích học tập hoặc nghiên cứu.

