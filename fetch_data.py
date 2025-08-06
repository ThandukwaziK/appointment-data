import json
from datetime import datetime

appointments = [
    {"appointment_id": 1, "tutor": "Jane Doe", "start_time": "2025-08-07T10:00", "duration": 60},
    {"appointment_id": 2, "tutor": "John Smith", "start_time": "2025-08-07T12:00", "duration": 45}
]

with open("data/appointments.json", "w") as f:
    json.dump(appointments, f, indent=2)

print("✅ Appointments saved.")

