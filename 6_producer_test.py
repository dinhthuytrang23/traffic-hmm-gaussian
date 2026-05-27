from kafka import KafkaProducer
import pandas as pd
import json
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = 'traffic_test_data11'
df = pd.read_csv('traffic_test.csv')
df.columns = df.columns.str.strip()

print(f"Bắt đầu gửi dữ liệu vào {topic_name}...")

# Dùng enumerate để vừa có số dòng (index) vừa có dữ liệu dòng (row)
# Trong vòng lặp gửi data
for i, (index, row) in enumerate(df.iterrows()):
    data = row.to_dict()
    producer.send(topic_name, value=data)
    
    # Cứ mỗi 1000 dòng thì in ra (nên để i+1 để bắt đầu đếm từ 1)
    if (i + 1) % 1000 == 0:
        current_time = data.get('date_time')
        print(f"Producer: Đã gửi đến mốc {current_time} (Dòng thứ {i + 1})")

producer.flush()
print("--- Producer đã gửi xong toàn bộ dữ liệu tệp test ! ---")
time.sleep(0.1) # Tốc độ gửi để bạn kịp quan sát