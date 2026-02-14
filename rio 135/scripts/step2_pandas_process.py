import os
import pandas as pd

BASE_DIR = r"C:\Users\Dell\OneDrive\Documents\logistics_bigdata_project"

iot_path = os.path.join(BASE_DIR, r"data\rawdat\iot_sensors\iot_sensors_2025_12_23.csv")
orders_path = os.path.join(BASE_DIR, r"data\rawdat\operational_logs\orders_2025_12_23.csv")
weather_path = os.path.join(BASE_DIR, r"data\rawdat\external_feeds\weather_2025_12_23.csv")

# 1. Read CSVs
iot_df = pd.read_csv(iot_path)
orders_df = pd.read_csv(orders_path)
weather_df = pd.read_csv(weather_path)

# Convert times
orders_df["pickup_time"] = pd.to_datetime(orders_df["pickup_time"])
orders_df["expected_delivery"] = pd.to_datetime(orders_df["expected_delivery"])
orders_df["actual_delivery"] = pd.to_datetime(orders_df["actual_delivery"])

# 2. Feature engineering: delay in minutes
orders_df["delay_min"] = (orders_df["actual_delivery"] - orders_df["expected_delivery"]).dt.total_seconds() / 60.0

# 3. Join with IoT (on vehicle_id) and weather (on city)
merged = orders_df.merge(iot_df, on="vehicle_id", how="left") \
                  .merge(weather_df, left_on=["drop_city"], right_on=["city"], how="left")

print("Processed rows:", len(merged))
print(merged.head())

# 4. Save as Parquet (processed zone)
processed_dir = os.path.join(BASE_DIR, "data", "processed")
os.makedirs(processed_dir, exist_ok=True)
output_path = os.path.join(processed_dir, "orders_enriched.parquet")

merged.to_parquet(output_path, index=False)
print("Written processed file to:", output_path)
