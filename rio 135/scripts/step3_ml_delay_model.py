import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

BASE_DIR = r"C:\Users\Dell\OneDrive\Documents\logistics_bigdata_project"

# 1. Load processed Parquet
processed_path = os.path.join(BASE_DIR, "data", "processed", "orders_enriched.parquet")
df = pd.read_parquet(processed_path)

print("Rows in processed data:", len(df))

# 2. Select features and target
# Target: delivery delay in minutes (already computed)
y = df["delay_min"]

# Simple numeric features; you can add more later
feature_cols = ["speed_kmph", "fuel_level_pct", "engine_temp_c", "temperature_c"]
X = df[feature_cols]

# 3. Train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=42
)

# 4. Train model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Evaluate
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("MAE:", mae)
print("R2:", r2)
print("Coefficients:", dict(zip(feature_cols, model.coef_)))
print("Intercept:", model.intercept_)

# 6. Save predictions for BI
df_pred = X_test.copy()
df_pred["actual_delay_min"] = y_test.values
df_pred["predicted_delay_min"] = y_pred

output_pred_path = os.path.join(BASE_DIR, "data", "processed", "delay_predictions.csv")
df_pred.to_csv(output_pred_path, index=False)
print("Saved predictions to:", output_pred_path)
