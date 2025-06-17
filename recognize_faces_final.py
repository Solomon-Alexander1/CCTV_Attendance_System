import cv2
import face_recognition
import pickle
import numpy as np
import os
import threading
import pandas as pd
from datetime import datetime

# Load known face encodings
with open("encodings.pickle", "rb") as file:
    data = pickle.load(file)

known_face_encodings = np.array(data["encodings"], dtype=np.float64)
known_face_names = np.array(data["names"])

# Initialize video capture with DirectShow (fixes lag on Windows)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

attendance_file = "attendance1.csv"

# Ensure CSV file has correct headers
if not os.path.exists(attendance_file):
    df = pd.DataFrame(columns=["Name", "Date", "Time"])
    df.to_csv(attendance_file, index=False)

attendance_log = set()  # Avoid duplicate entries

# Function to mark attendance
def mark_attendance(name):
    now = datetime.now()
    date_today = now.strftime("%Y-%m-%d")
    time_now = now.strftime("%H:%M:%S")

    if (name, date_today) not in attendance_log:
        attendance_log.add((name, date_today))  # Avoid duplicate entries

        df = pd.DataFrame([[name, date_today, time_now]], columns=["Name", "Date", "Time"])
        df.to_csv(attendance_file, mode="a", header=False, index=False)

        print(f"✅ Attendance marked for {name} at {time_now}")

# Function to process frames
def process_frame():
    while True:
        ret, frame = cap.read()
        if not ret:
            print("❌ Failed to capture frame")
            break

        # Convert frame from BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Detect faces
        face_locations = face_recognition.face_locations(rgb_frame, model="hog")
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.6)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances) if len(face_distances) > 0 else -1

            name = "Unknown"
            if best_match_index != -1 and matches[best_match_index]:
                name = known_face_names[best_match_index]

            # Draw a rectangle around the face
            top, right, bottom, left = face_location
            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)

            # Mark attendance in a separate thread
            if name != "Unknown":
                threading.Thread(target=mark_attendance, args=(name,)).start()

        # Show the frame
        cv2.imshow("Face Recognition Attendance", frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Start processing frames
process_frame()

# Release resources
cap.release()
cv2.destroyAllWindows()
