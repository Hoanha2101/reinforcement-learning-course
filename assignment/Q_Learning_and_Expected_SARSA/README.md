# Assignment 2 - Q-Learning and Expected Sarsa

## 📜 Giới thiệu

Bài tập này yêu cầu bạn triển khai và so sánh hai thuật toán **Q-Learning** và **Expected Sarsa** trên bài toán **Cliff World**.

### 🎯 Mục tiêu bài tập
1. **Triển khai Q-Learning** với chính sách **ε-greedy**.
2. **Triển khai Expected Sarsa** với chính sách **ε-greedy**.
3. **Phân tích hành vi của hai thuật toán** trên môi trường **Cliff World** (mô tả ở trang 132 của sách giáo khoa).

Chúng tôi sẽ cung cấp môi trường và hạ tầng để chạy thí nghiệm và trực quan hóa kết quả. **Bài tập sẽ được chấm điểm tự động**, bằng cách so sánh hành vi của agent với các triển khai chuẩn của **Expected Sarsa** và **Q-Learning**.

Để tránh kết quả khác nhau do ngẫu nhiên, **random seed sẽ được đặt cố định**.

---

## 🏗 Mô tả bài toán **Cliff World**

- **Môi trường Cliff World** là một lưới, nơi mà agent phải di chuyển từ **vị trí xuất phát (Start)** đến **đích (Goal)**.
- **Hành động:** Agent có thể di chuyển **Lên, Xuống, Trái, Phải**.
- **Trạng thái đặc biệt:**
  - Nếu agent **rơi xuống vực (Cliff)**, nó nhận **phần thưởng -100** và quay lại vị trí xuất phát.
  - Nếu agent **đến đích (Goal)**, nó nhận **phần thưởng 0** và kết thúc tập.
  - Các bước đi thông thường có **phần thưởng -1**.

Mục tiêu của agent là **học cách đến đích nhanh nhất có thể**, tránh rơi xuống vực.

---

## 🔢 Các thuật toán sử dụng

### ✅ **Q-Learning**
- **Là thuật toán Off-Policy**, cập nhật giá trị trạng thái-hành động theo công thức:

  $$ Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)] $$

- Agent cập nhật giá trị **dựa trên hành động tốt nhất có thể**, thay vì hành động thực tế đã chọn.

### ✅ **Expected Sarsa**
- **Là thuật toán On-Policy**, cập nhật giá trị theo **trung bình có trọng số** của tất cả các hành động khả thi:

  $$ Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \sum_{a'} \pi(a'|s') Q(s', a') - Q(s, a)] $$

- Agent **sử dụng chính sách π hiện tại** để cập nhật giá trị trạng thái-hành động.

---

## 📦 Thư viện sử dụng
Bài tập này sử dụng các thư viện sau:
1. **numpy**: Thư viện toán học cho Python.
2. **matplotlib**: Hỗ trợ vẽ đồ thị kết quả.
3. **RL-Glue**: Framework để chạy các thí nghiệm học tăng cường.

**⚠️ Lưu ý quan trọng:**
- **Không nhập thêm thư viện khác**, vì điều này có thể làm hỏng bộ chấm điểm tự động.
- **Làm theo đúng trình tự các ô mã** để đảm bảo thuật toán hoạt động chính xác.
- **Sử dụng đúng hàm để tạo số ngẫu nhiên**, và **không thay đổi số lần gọi hàm ngẫu nhiên**, vì điều này có thể làm sai lệch kết quả.

---

## 📌 Ghi chú
- **Q-Learning** thường hội tụ nhanh hơn nhưng không ổn định bằng **Expected Sarsa**.
- **Expected Sarsa** thường hoạt động tốt hơn trong các môi trường có nhiễu, vì nó cập nhật dựa trên chính sách hiện tại.
- So sánh hai thuật toán sẽ giúp bạn hiểu rõ hơn về sự khác biệt giữa **On-Policy** và **Off-Policy**.

---

## 📜 Bản quyền
Bài tập này được phát triển dựa trên các tài liệu về **Reinforcement Learning** của **Richard Sutton**.