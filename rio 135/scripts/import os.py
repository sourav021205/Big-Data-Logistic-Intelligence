import os
import csv
import hashlib
from datetime import datetime

# 1. Base directory of your project (change if needed)
BASE_DIR = r"C:\Users\Dell\OneDrive\Documents\logistics_bigdata_project"

RAW_DIR = os.path.join(BASE_DIR, "data", "rawdat")      # or "raw" if that is your name
MANIFEST_PATH = os.path.join(BASE_DIR, "ingestion_manifest.csv")

# 2. Helper: calculate checksum of a file
def file_checksum(path):
    h = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)
    return h.hexdigest()

# 3. Load existing manifest rows (to avoid duplicate entries)
existing_files = set()
if os.path.exists(MANIFEST_PATH):
    with open(MANIFEST_PATH, newline="", mode="r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            existing_files.add(row["file_path"])

# 4. Open manifest for appending new rows
manifest_file = open(MANIFEST_PATH, mode="a", newline="", encoding="utf-8")
fieldnames = ["source", "file_path", "checksum", "timestamp", "status"]
writer = csv.DictWriter(manifest_file, fieldnames=fieldnames)

# If file was empty, write header
if os.path.getsize(MANIFEST_PATH) == 0:
    writer.writeheader()

# 5. Walk through rawdat folder and register all CSV files
for source in ["iot_sensors", "operational_logs", "external_feeds"]:
    source_dir = os.path.join(RAW_DIR, source)
    for root, _, files in os.walk(source_dir):
        for name in files:
            if not name.lower().endswith(".csv"):
                continue

            full_path = os.path.join(root, name)
            rel_path = os.path.relpath(full_path, BASE_DIR)

            # Skip if already in manifest
            if rel_path in existing_files:
                continue

            checksum = file_checksum(full_path)
            ts = datetime.now().isoformat(timespec="seconds")

            writer.writerow({
                "source": source,
                "file_path": rel_path,
                "checksum": checksum,
                "timestamp": ts,
                "status": "INGESTED"
            })
            print("Logged:", rel_path)

manifest_file.close()
print("Ingestion manifest updated.")
