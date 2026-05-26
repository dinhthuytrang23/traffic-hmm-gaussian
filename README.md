# THIẾT KẾ MÔ PHỎNG VÀ ĐÁNH GIÁ HỆ THỐNG GIÁM SÁT TRẠNG THÁI GIAO THÔNG SỬ DỤNG MÔ HÌNH MARKOV ẨN VÀ APACHE KAFKA

## 1. Giới thiệu đề tài
Đề tài tập trung vào việc mô phỏng và đánh giá hệ thống giám sát trạng thái giao thông dựa trên dữ liệu chuỗi thời gian.

Hệ thống sử dụng mô hình Gaussian Hidden Markov Model (HMM) kết hợp với Apache Kafka để xử lý và phân tích dữ liệu, từ đó suy diễn các trạng thái giao thông ẩn như:

- Tắc nghẽn thấp
- Bình thường
- Tắc nghẽn cao

Ngoài ra, nghiên cứu cũng thực hiện so sánh với thuật toán K-Means nhằm đánh giá hiệu quả của mô hình Gaussian HMM trong bài toán phân tích trạng thái giao thông.

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


