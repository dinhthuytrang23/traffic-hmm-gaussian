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

Đề tài sử dụng bộ dữ liệu **Metro Interstate Traffic Volume** để mô phỏng và phân tích trạng thái giao thông theo chuỗi thời gian.

Dữ liệu được lưu trữ dưới định dạng **CSV** và trải qua bước tiền xử lý, trích xuất đặc trưng nhằm phục vụ cho quá trình huấn luyện mô hình.

Các đặc trưng bao gồm lưu lượng giao thông gốc cùng các đặc trưng thống kê và động học được tính toán từ dữ liệu theo thời gian, phục vụ xây dựng chuỗi quan sát cho mô hình Gaussian Hidden Markov Model.

Các đặc trưng này hỗ trợ mô hình trong việc suy diễn và phân loại các trạng thái giao thông ẩn.

---

## 3. Công nghệ và mô hình sử dụng

Hệ thống được xây dựng dựa trên các công nghệ và thư viện chính sau:

- **Python**: ngôn ngữ lập trình chính cho toàn bộ quá trình xử lý dữ liệu và xây dựng mô hình
- **Gaussian Hidden Markov Model (HMM)**: mô hình chính dùng để suy diễn và phân loại các trạng thái giao thông ẩn
- **Apache Kafka**: mô phỏng cơ chế truyền tải và xử lý dữ liệu giao thông theo thời gian thực
- **Scikit-learn**: hỗ trợ tiền xử lý dữ liệu và triển khai mô hình đối chứng K-Means
- **Pandas, NumPy**: xử lý và phân tích dữ liệu
- **Matplotlib**: trực quan hóa kết quả thực nghiệm
- **K-Means Clustering**: mô hình đối chứng dùng để so sánh với Gaussian HMM

---

## 4. Cấu trúc thư mục

Repository được tổ chức theo cấu trúc chính như sau:

```bash
Traffic Analysis/
├── *.ipynb             # Notebook phục vụ phân tích, huấn luyện và đánh giá mô hình
├── *.py                # Các script Kafka Producer và Consumer
├── *.csv               # Dữ liệu đầu vào phục vụ thực nghiệm
├── *.pkl               # Các mô hình đã huấn luyện được lưu trữ
├── database/           # Các file SQL
└── README.md
```
---


## 5. Quy trinh thực hiện

Hệ thống được triển khai theo quy trình gồm các bước chính sau:

1. **Phân tích bài toán và khảo sát dữ liệu**  
   Khảo sát bộ dữ liệu Metro Interstate Traffic Volume, phân tích đặc điểm chuỗi thời gian và đánh giá mức độ phù hợp với bài toán giám sát trạng thái giao thông.

2. **Phân tích đặc trưng và lựa chọn mô hình**  
   Xây dựng các đặc trưng từ dữ liệu chuỗi thời gian, đồng thời lựa chọn Gaussian Hidden Markov Model làm mô hình chính và K-Means làm mô hình tham chiếu.

3. **Thiết kế kiến trúc mô phỏng hệ thống**  
   Xây dựng kiến trúc xử lý dữ liệu gồm các thành phần thu thập, xử lý, suy diễn trạng thái, truyền dữ liệu qua Apache Kafka và lưu trữ kết quả.

4. **Tiền xử lý và trích xuất đặc trưng dữ liệu**  
   Làm sạch dữ liệu, chia tập huấn luyện/kiểm thử và xây dựng các đặc trưng phục vụ mô hình hóa trạng thái giao thông.

5. **Huấn luyện và tối ưu mô hình Gaussian HMM**  
   Thiết lập các cấu hình thử nghiệm, lựa chọn mô hình tối ưu và huấn luyện mô hình cuối cùng.

6. **Huấn luyện mô hình K-Means để đối chiếu**  
   Thiết lập mô hình tham chiếu nhằm so sánh hiệu quả suy diễn trạng thái với Gaussian HMM.

7. **Mô phỏng suy diễn trạng thái trên luồng dữ liệu**  
   Sử dụng Producer và Consumer trong Apache Kafka để mô phỏng dữ liệu thời gian thực và thực hiện suy diễn trạng thái giao thông.

8. **Lưu trữ, truy vấn và đánh giá hệ thống**  
   Lưu trữ kết quả bằng SQLite, thực hiện truy vấn và đánh giá hiệu năng của hệ thống mô phỏng.


---

## 6. Công nghệ sử dụng

- **Python** – ngôn ngữ lập trình chính
- **Apache Kafka** – xử lý luồng dữ liệu thời gian thực
- **MySQL** – lưu trữ dữ liệu
- **Pandas** – xử lý và phân tích dữ liệu
- **NumPy** – tính toán số học
- **Scikit-learn** – xây dựng mô hình machine learning
- **Jupyter Notebook** – thực nghiệm và đánh giá mô hình

---

## 7. Cách thực hiện nghiên cứu

Quy trình thực hiện được tiến hành theo các bước sau:

### Bước 1: Khảo sát dữ liệu đầu vào
- Đọc tệp dữ liệu thô (raw data)
- Khảo sát cấu trúc dữ liệu
- Phân tích các đặc trưng ban đầu
- Xác định các thuộc tính cần thiết cho bài toán

### Bước 2: Tiền xử lý dữ liệu
- Thực hiện tiền xử lý cơ bản
- Lựa chọn các segment phù hợp
- Tiếp tục tiền xử lý chuyên sâu
- Chia dữ liệu thành tập huấn luyện và tập kiểm thử

### Bước 3: Xây dựng đặc trưng và lựa chọn cấu hình mô hình
- Sử dụng tập train để xây dựng feature
- Thử nghiệm và lựa chọn cấu hình phù hợp cho mô hình HMM

### Bước 4: Huấn luyện mô hình
- Huấn luyện mô hình Hidden Markov Model (HMM)
- Huấn luyện mô hình K-Means

### Bước 5: Mô phỏng trên tập kiểm thử
- Sử dụng tập test để thực hiện mô phỏng
- Sinh dữ liệu đầu vào phục vụ pipeline streaming

### Bước 6: Triển khai pipeline streaming
- Khởi động Docker
- Chạy Kafka Consumer trước
- Chạy Kafka Producer sau để gửi dữ liệu vào hệ thống

### Bước 7: Thu thập và lưu trữ kết quả
- Consumer xuất dữ liệu đầu ra dưới dạng file CSV
- Đồng thời gửi trực tiếp dữ liệu đến cơ sở dữ liệu SQL để lưu trữ

### Bước 8: Đánh giá hệ thống
- Đánh giá chất lượng mô hình
- Đánh giá hiệu quả pipeline xử lý dữ liệu
- Đánh giá hiệu năng hệ thống dựa trên dữ liệu CSV được thu thập

---

## 8. Kết quả đạt được

Dự án đã xây dựng thành công một pipeline xử lý và phân tích dữ liệu giao thông, bao gồm các kết quả chính sau:

- Hoàn thiện quy trình tiền xử lý dữ liệu từ dữ liệu thô
- Xây dựng và triển khai mô hình HMM cho bài toán phân tích dữ liệu giao thông
- Mô phỏng thành công quá trình xử lý dữ liệu trên tập kiểm thử
- Triển khai pipeline streaming sử dụng Kafka với cơ chế Producer – Consumer
- Xuất dữ liệu đầu ra dưới dạng file CSV phục vụ phân tích
- Lưu trữ dữ liệu vào cơ sở dữ liệu SQL
- Thực hiện đánh giá mô hình và đánh giá hiệu năng của toàn bộ hệ thống
- Xây dựng được quy trình khép kín từ xử lý dữ liệu, huấn luyện mô hình, mô phỏng đến lưu trữ kết quả

---

## 9. Hướng phát triển

Từ kết quả thực nghiệm và quá trình đánh giá, một số hướng cần được xem xét và nghiên cứu thêm bao gồm:

- Xem xét sử dụng các bộ dữ liệu có chất lượng cao hơn nhằm nâng cao độ tin cậy của kết quả mô hình
- Nghiên cứu thêm các phương pháp xây dựng đặc trưng khác để cải thiện khả năng biểu diễn dữ liệu
- Việc lựa chọn các biến đặc trưng cần được thực hiện dựa trên cơ sở phân tích rõ ràng hơn thay vì chủ yếu dựa trên thực nghiệm
- Xem xét các phương pháp tối ưu hóa và lựa chọn mô hình khác ngoài tiêu chí BIC để xác định cấu hình phù hợp
- Cần đánh giá sâu hơn về tính hợp lý của ma trận chuyển trạng thái và khả năng phản ánh đúng đặc trưng giao thông thực tế
- Xem xét lại cách diễn giải các trạng thái ẩn để đảm bảo phù hợp hơn với ngữ cảnh giao thông thực tế
- Phân tích và đánh giá lại phân phối xác suất khởi tạo của mô hình nhằm xác định nguyên nhân dẫn đến hiện tượng tập trung hoàn toàn vào một trạng thái
- Thử nghiệm thêm các cấu hình đặc trưng và số lượng trạng thái khác nhằm kiểm chứng tính ổn định của mô hình
 ---

 ### Lưu ý
**Repository chỉ cung cấp dữ liệu mẫu để minh họa quy trình thực thi.
Các file dữ liệu đầy đủ không được đính kèm do giới hạn dung lượng.**
