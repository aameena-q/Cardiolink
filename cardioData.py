import firebase_admin
from firebase_admin import credentials, db
import time
from datetime import datetime

# === Initialize Firebase ===
cred = credentials.Certificate("cardiolink-1f862-firebase-adminsdk-fbsvc-928409ab8e.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://cardiolink-1f862-default-rtdb.asia-southeast1.firebasedatabase.app/'
})

# === Unique patient ID ===
patient_id = "patient_001"  # Change for each patient/device

# === Create a folder for today's date ===
today_date = datetime.now().strftime("%Y-%m-%d")

# === Reference path for today's ECG readings ===
ref = db.reference(f"patients/{patient_id}/sessions/{today_date}/ecg_readings")

# # === Optional Clear today's session before uploading new readings ===
ref.delete()



# === Read ECG readings from file ===
with open("ecg_readings.txt", "r") as file:
    readings = file.readlines()

# === Upload readings one by one ===
for i, value in enumerate(readings):
    value = value.strip()
    if value:
        ref.push({
            "timestamp": time.time(),
            "value": float(value)
        })
        print(f"[{patient_id}] Sent reading {i+1}: {value}")
        time.sleep(0.001)  # Adjust delay as needed (e.g. 0.05 or 0.1)







