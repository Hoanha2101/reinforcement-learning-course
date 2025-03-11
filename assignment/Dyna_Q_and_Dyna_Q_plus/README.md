# Assignment: Dyna-Q and Dyna-Q+

## 📜 Giới thiệu

Bài tập này yêu cầu bạn:
1. **Triển khai các thuật toán Dyna-Q và Dyna-Q+**.
2. **So sánh hiệu suất** của chúng trong một môi trường có thay đổi, khiến nhiệm vụ trở nên dễ dàng hơn theo thời gian.

Chúng tôi sẽ cung cấp môi trường và hạ tầng để chạy thí nghiệm và trực quan hóa kết quả. Bài tập sẽ được chấm điểm tự động bằng cách so sánh hành vi của agent với các triển khai thuật toán chuẩn. Để tránh sai số ngẫu nhiên, **random seed** sẽ được đặt cố định.

Hãy làm theo thứ tự các ô mã để đảm bảo hiểu đúng bài tập.

---

## 🏗 Môi trường **Shortcut Maze**

Mục tiêu của agent là **đi đến trạng thái mục tiêu (G) nhanh nhất có thể** từ vị trí bắt đầu (S).

### 🎯 Quy tắc môi trường
- **Hành động:** Lên, Xuống, Trái, Phải.
- **Di chuyển:**
  - Agent di chuyển **một cách xác định** đến ô lân cận tương ứng.
  - Nếu gặp **tường (ô xám)** hoặc **biên của mê cung**, agent vẫn giữ nguyên vị trí.
- **Phần thưởng:**
  - Khi đến **mục tiêu (G)**, nhận **+1**.
  - Các bước di chuyển khác nhận **0**.
- **Kết thúc một tập:**
  - Khi agent đạt **G**, nó sẽ quay lại vị trí **S** và bắt đầu tập mới.
- **Hệ số chiết khấu** \( \gamma = 0.95 \).

### 🔄 Biến đổi môi trường
Sau một số bước nhất định, **một đường tắt** xuất hiện, giúp agent tìm được đường đi ngắn hơn. Chúng tôi sẽ kiểm tra xem **Dyna-Q và Dyna-Q+ có thể thích nghi với thay đổi này không**.

---

## 📦 Thư viện sử dụng
Bài tập này sử dụng các thư viện sau:
1. **numpy**: Thư viện toán học cho Python.
2. **matplotlib**: Hỗ trợ vẽ đồ thị kết quả.
3. **RL-Glue**: Framework để chạy các thí nghiệm học tăng cường.

**⚠️ Lưu ý quan trọng:**
- **Không nhập thêm thư viện khác**, vì điều này có thể làm hỏng bộ chấm điểm tự động.
- **Làm theo đúng trình tự các ô mã** để đảm bảo thuật toán hoạt động chính xác.

---

## 📌 Ghi chú
- **Dyna-Q** sử dụng kết hợp **Q-learning + mô hình hóa môi trường** để cập nhật chính sách.
- **Dyna-Q+** cải tiến bằng cách bổ sung **khám phá dựa trên thời gian không truy cập trạng thái**.
- So sánh hai thuật toán sẽ giúp bạn hiểu được **khả năng thích nghi** của chúng khi môi trường thay đổi.

---

## 📜 Bản quyền
Bài tập này được phát triển dựa trên các tài liệu về **Reinforcement Learning** của **Richard Sutton**.

