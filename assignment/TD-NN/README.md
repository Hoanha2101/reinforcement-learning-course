# Assignment 2 - Semi-gradient TD with a Neural Network

## 📜 Giới thiệu

Trong bài tập trước, bạn đã triển khai **semi-gradient TD với State Aggregation** để giải quyết bài toán **policy evaluation task**. Trong bài tập này, bạn sẽ triển khai **semi-gradient TD với mạng nơ-ron đơn giản** để giải quyết cùng một bài toán.

Bạn sẽ triển khai một agent để đánh giá chính sách cố định trong **500-State Randomwalk**. Mỗi tập (episode) bắt đầu với agent ở trạng thái trung tâm và kết thúc khi agent vượt ra ngoài biên giới trạng thái 1 hoặc trạng thái 500. Mỗi bước, agent chọn di chuyển **trái hoặc phải với xác suất 0.5**, và môi trường xác định mức độ di chuyển của agent.

---

## 🎯 Mục tiêu bài tập

Trong bài tập này, bạn sẽ:
- **Triển khai phương pháp stochastic gradient descent** để dự đoán giá trị trạng thái.
- **Triển khai semi-gradient TD với mạng nơ-ron** làm bộ xấp xỉ giá trị (function approximator) và sử dụng thuật toán **Adam optimizer**.
- **So sánh hiệu suất** của semi-gradient TD sử dụng **mạng nơ-ron** với semi-gradient TD sử dụng **tile-coding**.

---

## 🏗 Môi trường **500-State RandomWalk**

- Môi trường có **500 trạng thái**, được đánh số từ **1 đến 500**.
- Mỗi tập **bắt đầu từ trạng thái 250**.
- **Trạng thái biên (0 và 501)** là **trạng thái kết thúc**:
  - Nếu agent **chạm biên trái (state 0)**: Nhận phần thưởng **-1**.
  - Nếu agent **chạm biên phải (state 501)**: Nhận phần thưởng **+1**.
- **Hành động:**
  - Agent có thể di chuyển **trái hoặc phải với xác suất 0.5**.
  - Khi đi **trái**, agent ngẫu nhiên đến một trong **100 trạng thái bên trái**.
  - Khi đi **phải**, agent ngẫu nhiên đến một trong **100 trạng thái bên phải**.
  - Nếu agent gần biên, xác suất chạm biên sẽ cao hơn (ví dụ: từ state 50, đi trái có xác suất 50% chạm biên).

---

## 📦 Thư viện sử dụng

Bài tập này sử dụng các thư viện sau:
- **numpy**: Thư viện toán học cho Python.
- **matplotlib**: Hỗ trợ vẽ đồ thị kết quả.
- **RL-Glue**: Framework để chạy các thí nghiệm Reinforcement Learning.
- **tqdm**: Hiển thị thanh tiến trình khi huấn luyện.
- **BaseOptimizer**: Lớp trừu tượng cho API tối ưu hóa của Agent.
- **plot_script**: Tập lệnh để hiển thị kết quả.
- **RandomWalkEnvironment**: Môi trường 500-State RandomWalk từ Assignment 1.

**⚠️ Lưu ý quan trọng:**
- **Không nhập thêm thư viện khác**, vì điều này có thể làm hỏng bộ chấm điểm tự động.
- **Làm theo đúng trình tự các ô mã** để đảm bảo thuật toán hoạt động chính xác.

---

## 📌 Ghi chú
- **Mạng nơ-ron** được sử dụng như một **function approximator**, giúp **tổng quát hóa (generalization)** khi số lượng trạng thái lớn.
- **Adam optimizer** giúp cập nhật trọng số mạng nhanh chóng và ổn định.
- **So sánh với Tile Coding** sẽ giúp bạn hiểu rõ lợi ích của từng phương pháp trong việc xấp xỉ giá trị trạng thái.

---

## 📜 Bản quyền
Bài tập này được phát triển dựa trên các tài liệu về **Reinforcement Learning** của **Richard Sutton**.

