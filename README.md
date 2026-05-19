# PHÂN TÍCH DỮ LIỆU GIAO THÔNG BẰNG GAUSSIAN HIDDEN MARKOV MODEL (HMM)

## 1. Giới thiệu đề tài
Đề tài này tập trung vào việc phân tích và mô hình hóa dữ liệu lưu lượng giao thông theo chuỗi thời gian bằng mô hình Gaussian Hidden Markov Model (HMM).

Mục tiêu của nghiên cứu là xác định các trạng thái giao thông ẩn như:
- Tắc nghẽn thấp
- Bình thường
- Tắc nghẽn cao

---

## 2. Dữ liệu sử dụng
- Dữ liệu sẽ được bổ sung sau
- Định dạng dự kiến: file CSV dạng chuỗi thời gian
- Các biến chính:
  - traffic_volume (lưu lượng giao thông)
  - avg_24h (trung bình 24 giờ)
  - volume_deviation (độ lệch)
  - volume_change (biến động)

---

## 3. Phương pháp nghiên cứu (dự kiến)

Quy trình thực hiện gồm:

1. Thu thập dữ liệu
2. Tiền xử lý dữ liệu
3. Xây dựng đặc trưng
4. Huấn luyện mô hình Gaussian HMM
5. Suy diễn trạng thái bằng thuật toán Viterbi
6. Đánh giá mô hình
7. So sánh với mô hình K-Means

---

## 4. Cấu trúc dự án (dự kiến)
# traffic-hmm-gaussian


---

## 5. Cách chạy chương trình (sẽ cập nhật sau)

```bash
pip install -r requirements.txt
python src/main.py


---


