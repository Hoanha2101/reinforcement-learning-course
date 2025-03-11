# Softmax Policy for Action Selection

Đây là một triển khai của **Chính sách Softmax (Softmax Policy)** để chọn hành động dựa trên giá trị Q-value.

## 🛠 Cài đặt

Trước khi chạy mã, bạn cần cài đặt thư viện cần thiết:

```bash
pip install numpy
```

## 📜 Mô tả

Softmax Policy là một kỹ thuật phổ biến trong **Reinforcement Learning** để chọn hành động dựa trên **Softmax Distribution**, giúp cân bằng giữa **khai thác (exploitation)** và **khám phá (exploration)**.

### 🎯 Cách hoạt động
- Softmax chuyển đổi giá trị **Q-value** của các hành động thành xác suất.
- Hành động có **giá trị Q cao hơn** sẽ có **xác suất cao hơn** để được chọn.
- **Temperature** điều chỉnh sự cân bằng giữa khai thác và khám phá:
  - **Nhiệt độ cao**: Chọn hành động gần như ngẫu nhiên.
  - **Nhiệt độ thấp**: Chọn hành động tốt nhất với xác suất cao.

### 🏗 Công thức Softmax

Giá trị Q được chuyển đổi thành xác suất bằng công thức:

$$ P(a) = \frac{e^{Q(a) / T}}{\sum_{b} e^{Q(b) / T}} $$

Trong đó:
- \( P(a) \) là xác suất chọn hành động \( a \).
- \( Q(a) \) là giá trị Q của hành động \( a \).
- \( T \) là nhiệt độ (temperature), điều chỉnh mức độ ngẫu nhiên.

## 🔢 Tham số chính

| Tham số | Giá trị |
|---------|--------|
| Số hành động | 4 (Up, Down, Left, Right) |
| Nhiệt độ (temperature) | 0.5 |

## ▶️ Chạy chương trình

Để chạy mã, sử dụng lệnh sau trong terminal:

```bash
python softmax_policy.py
```

Chương trình sẽ hiển thị xác suất của các hành động và hành động được chọn:

```
probabilities [0.0871 0.6439 0.0320 0.2368]
Selected Action: 1
```

## 📈 Kết quả mong đợi
- **Xác suất của các hành động** sẽ phản ánh giá trị Q tương ứng.
- **Hành động có giá trị Q cao hơn** có nhiều khả năng được chọn hơn.
- **Tăng hoặc giảm nhiệt độ** sẽ ảnh hưởng đến mức độ ngẫu nhiên khi chọn hành động.

## 📌 Ghi chú
- Giá trị nhiệt độ (`temperature`) càng cao, hành động được chọn càng ngẫu nhiên.
- Nếu nhiệt độ rất thấp, chính sách gần giống **Greedy Policy**.
- Softmax Policy thường được sử dụng trong các thuật toán như **Policy Gradient Methods** hoặc **Actor-Critic**.

## 📜 Bản quyền
Mã nguồn được cung cấp miễn phí và có thể sử dụng cho mục đích học tập hoặc nghiên cứu.

