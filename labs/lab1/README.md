# Epsilon-Greedy Algorithm cho Multi-Armed Bandit

Đây là một triển khai thuật toán **Epsilon-Greedy** để giải quyết bài toán **Multi-Armed Bandit**.

## 🛠 Cài đặt

Trước khi chạy mã, bạn cần cài đặt thư viện cần thiết:

```bash
pip install numpy
```

## 📜 Mô tả

Bài toán **Multi-Armed Bandit** mô phỏng tình huống chọn cánh tay tốt nhất trong một số lượng cánh tay nhất định của máy đánh bạc, mỗi cánh tay có một giá trị phần thưởng khác nhau.

### 🎯 Mục tiêu
- Tìm ra hành động có giá trị kỳ vọng cao nhất.
- Cân bằng giữa **khai thác (exploitation)** và **khám phá (exploration)** bằng chiến lược **epsilon-greedy**.

## 🏗 Cách thức hoạt động

1. **Khởi tạo môi trường** gồm `num_arms` cánh tay với giá trị phần thưởng thực sự được lấy từ phân phối chuẩn `N(0,1)`.
2. **Agent chọn hành động** dựa trên chiến lược **epsilon-greedy**:
   - Với xác suất `epsilon`: chọn hành động ngẫu nhiên (**exploration**).
   - Ngược lại: chọn hành động có giá trị kỳ vọng cao nhất (**exploitation**).
3. **Môi trường trả về phần thưởng**, phần thưởng này được lấy từ phân phối `N(Q*(a),1)`.
4. **Cập nhật giá trị kỳ vọng** của hành động theo công thức:
   
   $$ Q(a) \leftarrow Q(a) + \frac{1}{N} (r - Q(a)) $$
   
5. **Lặp lại quá trình trên trong `num_steps` bước.**

## 🔢 Tham số chính

| Tham số | Giá trị |
|---------|--------|
| Số cánh tay (num_arms) | 10 |
| Số bước thực hiện (num_steps) | 1000 |
| Epsilon | 0.1 |

## ▶️ Chạy chương trình

Để chạy mã, sử dụng lệnh sau trong terminal:

```bash
python python src/ex.py
```

Chương trình sẽ hiển thị **tổng phần thưởng** và **giá trị kỳ vọng của các hành động**.

## 📈 Kết quả mong đợi

- **Tổng phần thưởng:** Giá trị càng cao, agent học được chính sách tốt hơn.
- **Giá trị kỳ vọng của hành động:** Phản ánh mức độ gần đúng với giá trị thực của các cánh tay bandit.

## 📌 Ghi chú
- Bạn có thể thay đổi **epsilon** để xem ảnh hưởng của khám phá và khai thác.
- Thử nghiệm với các giá trị **num_arms** lớn hơn để kiểm tra độ hiệu quả của thuật toán.

## 📜 Bản quyền
Mã nguồn được cung cấp miễn phí và có thể sử dụng cho mục đích học tập hoặc nghiên cứu.

