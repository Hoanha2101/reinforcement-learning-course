# Monte Carlo Estimation for GridWorld

Đây là một triển khai thuật toán **Monte Carlo** để ước lượng **hàm giá trị trạng thái** trong môi trường **GridWorld**.

## 🛠 Cài đặt

Trước khi chạy mã, bạn cần cài đặt thư viện cần thiết:

```bash
pip install numpy
```

## 📜 Mô tả

Bài toán **GridWorld** mô phỏng môi trường dạng lưới 3x4, trong đó một agent di chuyển theo các hướng **Lên, Xuống, Trái, Phải** và nhận phần thưởng khi đến ô đích.

### 🎯 Môi trường
- Lưới có kích thước **3x4**.
- Số hành động có thể thực hiện: **4 hành động (Lên, Xuống, Trái, Phải)**.
- Phần thưởng:
  - Ô (2,3) có phần thưởng **+1**.
  - Các ô còn lại có phần thưởng **0**.
- Trạng thái bắt đầu: **(2,0)**.
- Trạng thái kết thúc: **(2,3)**.

### 🏗 Cách thức hoạt động

1. **Tạo môi trường GridWorld**:
   - Xác định kích thước lưới và phần thưởng tại từng ô.
   - Định nghĩa quy tắc di chuyển (step function).

2. **Tạo thuật toán Monte Carlo**:
   - Lặp lại `num_episodes` lần.
   - Sinh các tập hợp `(state, action, reward)`.
   - Tính toán giá trị kỳ vọng **G** của mỗi trạng thái:
     
     $$ G = \sum_{i=0}^{T} \gamma^i r_{i} $$
     
   - Cập nhật giá trị trạng thái bằng trung bình cộng của tất cả các lần xuất hiện trong tập.

3. **Sinh các tập (Episodes)**:
   - Bắt đầu từ trạng thái `(2,0)`.
   - Chọn hành động ngẫu nhiên và di chuyển đến trạng thái tiếp theo.
   - Lưu lại `(state, action, reward)` vào tập.
   - Kết thúc khi đến trạng thái `(2,3)`.

4. **Tính giá trị trạng thái**:
   - Trung bình các giá trị **G** đã thu thập được.
   - Xuất ra **hàm giá trị trạng thái ước lượng**.

## 🔢 Tham số chính

| Tham số | Giá trị |
|---------|--------|
| Kích thước lưới | 3x4 |
| Số hành động | 4 |
| Số tập huấn luyện | 1000 |
| Hệ số chiết khấu (gamma) | 1.0 |

## ▶️ Chạy chương trình

Để chạy mã, sử dụng lệnh sau trong terminal:

```bash
python src/ex.py
```

Chương trình sẽ hiển thị **hàm giá trị trạng thái** đã học.

## 📈 Kết quả mong đợi

Sau khi chạy chương trình, bạn sẽ thấy một ma trận giá trị trạng thái được cập nhật dựa trên thuật toán Monte Carlo:

```
Estimated State-Value Function:
[[0.  0.  0.  0. ]
 [0.  0.  0.  0. ]
 [0.  0.  0.  1. ]]
```

## 📌 Ghi chú
- Đây là phương pháp Monte Carlo **First-Visit**, chỉ cập nhật trạng thái lần đầu tiên nó xuất hiện trong tập.
- Bạn có thể thay đổi **num_episodes** để xem ảnh hưởng của số lần lặp lên kết quả.
- Có thể mở rộng để áp dụng **chính sách chọn hành động** thay vì hành động ngẫu nhiên.

## 📜 Bản quyền
Mã nguồn được cung cấp miễn phí và có thể sử dụng cho mục đích học tập hoặc nghiên cứu.

