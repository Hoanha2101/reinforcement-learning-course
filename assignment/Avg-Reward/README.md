# Assignment 4 - Average Reward Softmax Actor-Critic

## 📜 Giới thiệu

Bài tập này yêu cầu triển khai thuật toán **Average Reward Softmax Actor-Critic** trong bài toán **Pendulum Swing-Up**. Qua bài tập này, bạn sẽ có cơ hội thực hành các phương pháp **actor-critic** trong một bài toán **continuing task**.

### 🎯 Mục tiêu bài tập

Trong bài tập này, bạn sẽ thực hiện các nhiệm vụ sau:
1. Triển khai agent sử dụng **softmax actor-critic** trên bài toán **continuing task**, sử dụng công thức phần thưởng trung bình.
2. Hiểu cách tham số hóa chính sách (**policy**) như một hàm học trong môi trường có hành động rời rạc.
3. Hiểu cách lấy mẫu **gradient** của mục tiêu để cập nhật **actor**.
4. Hiểu cách cập nhật **critic** bằng phương pháp **differential TD error**.

---

## 🔧 Môi trường Pendulum Swing-Up

Bài toán này sử dụng môi trường **Pendulum Swing-Up**, được phát triển từ nghiên cứu của **Santamaría et al. (1998)**.

### 🏗 Mô tả môi trường
- Môi trường bao gồm một **con lắc đơn**, có thể xoay **360 độ**.
- Con lắc chịu ảnh hưởng của **trọng lực** và lực mô-men xoắn từ agent.
- Mục tiêu là làm cho con lắc **cân bằng ở vị trí thẳng đứng** (**up-right**) và giữ nó càng lâu càng tốt.
- Hành động có thể điều khiển là **gia tốc góc** \( a \in \{-1, 0, 1\} \).

### 🌍 Trạng thái (State)
- Môi trường có **trạng thái 2 chiều**, gồm:
  - **Góc hiện tại** \( \beta \in [-\pi, \pi] \), đo từ vị trí thẳng đứng.
  - **Vận tốc góc** \( \dot{\beta} \in (-2\pi, 2\pi) \).
- Vận tốc góc bị giới hạn để tránh làm hỏng hệ thống con lắc.
- Nếu con lắc vượt quá giới hạn này, nó sẽ được đặt lại về vị trí nghỉ.

### 🏆 Phần thưởng (Reward)
- Phần thưởng được định nghĩa là **góc tuyệt đối âm** từ vị trí thẳng đứng:
  
  $$ R_t = -|\beta_t| $$
  
  - Khi con lắc nghiêng **xa vị trí thẳng đứng**, phần thưởng thấp hơn.
  - Khi con lắc gần **vị trí cân bằng**, phần thưởng cao hơn.

### 🔁 Tiếp tục nhiệm vụ (Continuing Task)
- Vì mục tiêu là giữ con lắc thẳng đứng mãi mãi, **bài toán không có trạng thái kết thúc (terminal state)**.
- Không có **tập hợp cố định số lần chạy**.
- **Bài toán được mô hình hóa như một continuing task**.

### 🔄 So sánh với MountainCar
- Tương tự như bài toán **MountainCar**, lực tác động lên con lắc **không đủ mạnh** để đưa nó ngay về vị trí mong muốn.
- Agent phải **tạo động lượng** bằng cách di chuyển **ra xa vị trí mong muốn** trước khi có đủ năng lượng để **đưa con lắc về vị trí thẳng đứng**.
- Sau khi đạt được vị trí thẳng đứng, agent phải tiếp tục **duy trì thăng bằng** trong trạng thái không ổn định.

---

## 🚀 Yêu cầu triển khai

- **Actor-Critic Agent**:
  - **Actor** sử dụng **softmax policy** để chọn hành động.
  - **Critic** sử dụng **differential TD error** để đánh giá giá trị trạng thái.
  - Cập nhật Actor và Critic dựa trên **phần thưởng trung bình**.

- **Chính sách học được** sẽ giúp agent cân bằng con lắc hiệu quả bằng cách tối ưu hóa tổng phần thưởng trung bình trên thời gian dài.

---

## 📌 Ghi chú
- Đây là bài toán **Continuing Task**, cần sử dụng công thức phần thưởng trung bình thay vì phần thưởng tích lũy thông thường.
- Bạn có thể thay đổi **hệ số học (learning rate)** hoặc **gamma** để kiểm tra ảnh hưởng của chúng đến hiệu suất học tập.
- Kết quả mong đợi là agent có thể giữ con lắc ở trạng thái **cân bằng lâu dài**.

---

## 📜 Bản quyền
Bài tập này được phát triển dựa trên nghiên cứu của **Santamaría et al. (1998)** và được sử dụng cho mục đích học tập.