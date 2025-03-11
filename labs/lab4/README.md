# Temporal Difference Learning for GridWorld

Đây là một triển khai thuật toán **Temporal Difference (TD) Learning** để ước lượng **hàm giá trị trạng thái** trong môi trường **GridWorld**.

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
  - Ô (2,2) có phần thưởng **+10**.
  - Các ô còn lại có phần thưởng **-1**.
- Trạng thái bắt đầu: **(0,0)**.
- Trạng thái kết thúc: **(2,2)**.

### 🏗 Cách thức hoạt động

1. **Tạo môi trường GridWorld**:
   - Xác định kích thước lưới và phần thưởng tại từng ô.
   - Định nghĩa quy tắc di chuyển (step function).

2. **Thuật toán Temporal Difference (TD) Learning**:
   - Khởi tạo hàm giá trị **V(s) = 0** cho tất cả các trạng thái.
   - Lặp lại **num_episodes** lần:
     - Bắt đầu từ trạng thái **(0,0)**.
     - Chọn hành động ngẫu nhiên.
     - Di chuyển đến trạng thái tiếp theo và nhận phần thưởng.
     - Cập nhật giá trị trạng thái theo công thức:
       
       $$ V(s) \leftarrow V(s) + \alpha [r + \gamma V(s') - V(s)] $$
       
     - Kết thúc khi đến trạng thái **(2,2)**.

3. **Trả về hàm giá trị trạng thái sau khi huấn luyện**.

## 🔢 Tham số chính

| Tham số | Giá trị |
|---------|--------|
| Kích thước lưới | 3x3 |
| Số hành động | 4 |
| Số tập huấn luyện | 1000 |
| Learning rate (alpha) | 0.1 |
| Discount factor (gamma) | 0.9 |

## ▶️ Chạy chương trình

Để chạy mã, sử dụng lệnh sau trong terminal:

```bash
python src/ex.py
```

Chương trình sẽ hiển thị **hàm giá trị trạng thái** đã học.

## 📈 Kết quả mong đợi

Sau khi chạy chương trình, bạn sẽ thấy một ma trận giá trị trạng thái được cập nhật dựa trên thuật toán Temporal Difference:

```
Value function:
[[ -x  -x  -x]
 [ -x  -x  -x]
 [ -x  -x  10]]
```

(x là các giá trị trạng thái được cập nhật dựa trên TD Learning)

## 📌 Ghi chú
- Đây là phương pháp **TD(0)**, cập nhật giá trị trạng thái từng bước dựa trên quan sát trực tiếp.
- Bạn có thể thay đổi **alpha** và **gamma** để kiểm tra ảnh hưởng của tốc độ học và hệ số chiết khấu.
- Có thể mở rộng để áp dụng **chính sách chọn hành động** thay vì hành động ngẫu nhiên.

## 📜 Bản quyền
Mã nguồn được cung cấp miễn phí và có thể sử dụng cho mục đích học tập hoặc nghiên cứu.