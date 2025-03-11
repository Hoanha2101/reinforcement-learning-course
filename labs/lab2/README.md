# GridWorld - Mô phỏng môi trường lưới 3x3

Đây là một triển khai đơn giản của môi trường **GridWorld** với lưới 3x3 và một trạng thái có phần thưởng +1.

## 🛠 Cài đặt

Trước khi chạy mã, bạn cần cài đặt thư viện cần thiết:

```bash
pip install numpy
```

## 📜 Mô tả

Bài toán **GridWorld** là một môi trường đơn giản trong **Reinforcement Learning**, trong đó một agent di chuyển trên lưới 3x3 và nhận phần thưởng tại một số ô nhất định.

### 🎯 Môi trường
- Lưới có kích thước **3x3**.
- Số hành động có thể thực hiện: **4 hành động (Lên, Xuống, Trái, Phải)**.
- Phần thưởng:
  - Ô (2,1) có phần thưởng **+1**.
  - Các ô còn lại có phần thưởng **0**.

### 🏗 Cách thức hoạt động

1. **Tạo môi trường GridWorld**:
   - Môi trường được biểu diễn dưới dạng ma trận 3x3.
   - Phần thưởng được xác định trước.

2. **Khởi tạo hàm giá trị**:
   - Mỗi trạng thái trong lưới có một giá trị ban đầu bằng 0.
   - Giá trị ban đầu của trạng thái được cập nhật bằng phần thưởng tại trạng thái đó.

3. **Hiển thị giá trị ban đầu của các trạng thái**.

## 🔢 Tham số chính

| Tham số | Giá trị |
|---------|--------|
| Kích thước lưới | 3x3 |
| Số hành động | 4 |
| Phần thưởng | Ô (2,1) có +1 |

## ▶️ Chạy chương trình

Để chạy mã, sử dụng lệnh sau trong terminal:

```bash
python src/ex.py
```

Chương trình sẽ hiển thị **giá trị ban đầu của từng trạng thái** trong lưới.

## 📈 Kết quả mong đợi

Sau khi chạy chương trình, bạn sẽ thấy giá trị trạng thái được khởi tạo bằng phần thưởng của từng ô:

```
Initial Value Function:
[[0. 0. 0.]
 [0. 0. 0.]
 [0. 1. 0.]]
```

## 📌 Ghi chú
- Mô hình này chỉ khởi tạo giá trị trạng thái, chưa có chính sách hay quá trình học tập.
- Có thể mở rộng bằng việc áp dụng **Dynamic Programming** hoặc **Reinforcement Learning** để học giá trị tối ưu.

## 📜 Bản quyền
Mã nguồn được cung cấp miễn phí và có thể sử dụng cho mục đích học tập hoặc nghiên cứu.

