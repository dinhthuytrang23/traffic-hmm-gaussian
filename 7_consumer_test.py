from kafka import KafkaConsumer
import json
from collections import deque
import numpy as np
import pandas as pd
import uuid
import joblib
import sqlite3
import os

# ==========================================
# LOAD MODEL & SCALER
# ==========================================

hmm_model = joblib.load("gaussian_hmm_model.pkl")
hmm_scaler = joblib.load("gaussian_hmm_scaler.pkl")

kmeans_model = joblib.load("kmeans_model.pkl")
kmeans_scaler = joblib.load("kmeans_scaler.pkl")

# FEATURE SET CHO MODEL (CHỐT FINAL)
model_features = ['traffic_volume', 'avg_24h', 'volume_deviation']

# ==========================================
# SQLITE SETUP
# ==========================================

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/traffic_sql.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS traffic_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_time TEXT,
    traffic_volume REAL,
    lag_1 REAL,
    volume_change REAL,
    avg_3h REAL,
    avg_24h REAL,
    rolling_std_3h REAL,
    volume_deviation REAL,
    gaussian_hmm_state INTEGER,
    gaussian_hmm_prob REAL,
    kmeans_state INTEGER
)
""")

conn.commit()

# ==========================================
# KAFKA CONSUMER
# ==========================================

topic_name = "traffic_test_data11"

consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id=f"group_{uuid.uuid4().hex[:6]}",
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    consumer_timeout_ms=10000
)

# ==========================================
# WINDOWS + BUFFER
# ==========================================

window_3h = deque(maxlen=3)
window_24h = deque(maxlen=24)

sequence_buffer = []
MAX_SEQ = 10

last_val = None
all_results = []

print("=== Consumer running ===")

# ==========================================
# LOOP
# ==========================================

try:
    for message in consumer:

        record = message.value
        val = record.get("traffic_volume")

        if val is None:
            continue

        val = float(val)

        # ----------------------------------
        # BASIC FEATURES
        # ----------------------------------

        if last_val is None:
            lag_1 = val
            volume_change = 0.0
        else:
            lag_1 = last_val
            volume_change = val - last_val

        last_val = val

        # ----------------------------------
        # UPDATE WINDOWS
        # ----------------------------------

        window_3h.append(val)
        window_24h.append(val)

        # ----------------------------------
        # FEATURE WARM-UP
        # ----------------------------------

        if len(window_24h) < 24:
            continue

        # ----------------------------------
        # FEATURE ENGINEERING (FULL)
        # ----------------------------------

        avg_3h = np.mean(window_3h)
        avg_24h = np.mean(window_24h)
        rolling_std_3h = np.std(window_3h)
        volume_deviation = val - avg_24h

        # ----------------------------------
        # FEATURE DICTIONARY (FULL SET)
        # ----------------------------------

        feature_dict = {
            "traffic_volume": val,
            "avg_24h": avg_24h,
            "volume_deviation": volume_deviation,
            "volume_change": volume_change,
            "avg_3h": avg_3h,
            "rolling_std_3h": rolling_std_3h,
            "lag_1": lag_1,
        }

        # ----------------------------------
        # FEATURE SELECTION (MODEL INPUT)
        # ----------------------------------

        feature_vector = np.array([[feature_dict[f] for f in model_features]])

        # ----------------------------------
        # SCALE
        # ----------------------------------

        hmm_scaled = hmm_scaler.transform(feature_vector)
        kmeans_scaled = kmeans_scaler.transform(feature_vector)

        # ----------------------------------
        # KMEANS
        # ----------------------------------

        kmeans_state = int(kmeans_model.predict(kmeans_scaled)[0])

        # ----------------------------------
        # HMM BUFFER
        # ----------------------------------

        sequence_buffer.append(hmm_scaled[0])

        if len(sequence_buffer) > MAX_SEQ:
            sequence_buffer.pop(0)

        if len(sequence_buffer) < MAX_SEQ:
            continue

        seq = np.array(sequence_buffer)

        states = hmm_model.predict(seq)
        probs = hmm_model.predict_proba(seq)

        hmm_state = int(states[-1])
        hmm_prob = float(np.max(probs[-1]))

        # ----------------------------------
        # SAVE RECORD
        # ----------------------------------

        output_record = {
            "date_time": record.get("date_time"),
            "traffic_volume": val,
            "lag_1": lag_1,
            "volume_change": volume_change,
            "avg_3h": avg_3h,
            "avg_24h": avg_24h,
            "rolling_std_3h": rolling_std_3h,
            "volume_deviation": volume_deviation,
            "gaussian_hmm_state": hmm_state,
            "gaussian_hmm_prob": round(hmm_prob, 6),
            "kmeans_state": kmeans_state
        }

        all_results.append(output_record)

        # ----------------------------------
        # INSERT SQLITE
        # ----------------------------------

        cursor.execute("""
        INSERT INTO traffic_data (
            date_time,
            traffic_volume,
            lag_1,
            volume_change,
            avg_3h,
            avg_24h,
            rolling_std_3h,
            volume_deviation,
            gaussian_hmm_state,
            gaussian_hmm_prob,
            kmeans_state
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            output_record["date_time"],
            output_record["traffic_volume"],
            output_record["lag_1"],
            output_record["volume_change"],
            output_record["avg_3h"],
            output_record["avg_24h"],
            output_record["rolling_std_3h"],
            output_record["volume_deviation"],
            output_record["gaussian_hmm_state"],
            output_record["gaussian_hmm_prob"],
            output_record["kmeans_state"]
        ))

        conn.commit()

        # progress log
        if len(all_results) % 1000 == 0:
            print(f"Processed {len(all_results)} rows")

except KeyboardInterrupt:
    print("Stopped manually")

finally:

    print("Saving CSV...")

    if all_results:
        df = pd.DataFrame(all_results)
        df.to_csv("traffic_test_output_01.csv", index=False)
        print("Saved CSV:", df.shape)

    conn.close()
    print("SQLite connection closed")