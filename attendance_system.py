import cv2
import face_recognition
import numpy as np
import pandas as pd
import os
from datetime import datetime

# Load your face encoding
solomon_encoding = np.load("encodings/solomon.npy")

# Initialize attendance CSV
CSV_FILE = "attendance.csv"

if not os.path.exists(CSV_FILE):
    df = pd.DataFrame(columns=["Name", "Date", "Time"])
    df.to_csv(CSV_FILE, index=False)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces([solomon_encoding], face_encoding)
        if matches[0]:
            print("✅ Solomon Detected!")

            # Get current date & time
            now = datetime.now()
            date_str = now.strftime("%Y-%m-%d")
            time_str = now.strftime("%H:%M:%S")

            # Load CSV and update attendance
            df = pd.read_csv(CSV_FILE)
            new_entry = pd.DataFrame([{"Name": "Solomon Alexander", "Date": date_str, "Time": time_str}])
            df = pd.concat([df, new_entry], ignore_index=True)
            df.to_csv(CSV_FILE, index=False)
            print(f"✅ Attendance Marked: {date_str} {time_str}")

    cv2.imshow("CCTV Attendance", frame)
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
