import subprocess
import datetime
import os

BASE_DIR = r"C:\Users\Dell\OneDrive\Documents\logistics_bigdata_project"
LOG_PATH = os.path.join(BASE_DIR, "pipeline_run.log")

def log(msg):
    now = datetime.datetime.now().isoformat(timespec="seconds")
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"{now} - {msg}\n")

steps = [
    r".\scripts\ingest_files.py",
    r".\scripts\step2_pandas_process.py",
    r".\scripts\step3_ml_delay_model.py",
]

def main():
    log("PIPELINE START")
    for step in steps:
        try:
            log(f"START {step}")
            subprocess.check_call(["python", step], cwd=BASE_DIR)
            log(f"SUCCESS {step}")
        except Exception as e:
            log(f"FAIL {step}: {e}")
            break
    else:
        log("PIPELINE COMPLETE")

if __name__ == "__main__":
    main()
