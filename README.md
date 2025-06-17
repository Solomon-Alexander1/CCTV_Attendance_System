# 📷 CCTV Attendance System

An AI-based attendance system using face recognition technology that captures faces through CCTV or webcam feed and automatically marks attendance. This system is designed for educational institutions, offices, and organizations looking for automated, contactless, and efficient attendance management.

---

## 📁 Project Structure

CCTV_Attendance_System/
│
├── attendance/ # Logs Excel/CSV attendance reports
├── attendance1/ # (Optional backup/secondary log folder)
├── capture_image/ # Script to register new user images
├── encode_faces/ # Generates encodings from known faces
├── encodings/ # Pickled files for faster recognition
├── known_faces/ # Directory of stored registered face images
├── attendance_system/ # Main codebase (alternative structure)
│
├── .dist/ # Build/cache-related folders (auto-generated)
├── .venv/ # Python virtual environment
├── dlib-19.22.99-...whl # Optional offline dlib wheel
├── encodings.pickle # Serialized face encodings
├── solomon_encoding.npy # NumPy array of face data
│
├── recognize_faces_final.py # 🔴 Main face recognition & attendance script
├── test.py # Test script for validation
├── requirements.txt # All Python dependencies
├── README.md # Project readme file



---

## 💡 Features

✅ Real-time face detection using webcam or CCTV stream  
✅ Face encoding using `dlib` and `face_recognition`  
✅ Records attendance with time & date in Excel format  
✅ CSV/Excel logs auto-generated per session  
✅ Add/encode new faces from webcam  
✅ Lightweight and customizable

---

## 🛠️ Technologies Used

| Tool/Library         | Purpose                                      |
|----------------------|----------------------------------------------|
| Python 3.x           | Core programming language                    |
| OpenCV (`cv2`)       | Video capture, face bounding                |
| dlib                 | Face landmark detection                     |
| face_recognition     | Facial encoding & matching                   |
| Pandas               | Data logging into Excel/CSV                  |
| NumPy                | Data structures and array processing         |
| Tkinter (Optional)   | GUI for advanced integration                 |
| pickle               | Save/load face encodings                     |
| datetime, os         | File handling and time management            |

---

## 🔄 How It Works

1. **Capture Known Faces**  
   Place known images in `known_faces/` or use `capture_image/` to snap a face and save it with a filename (e.g., `solomon.jpg`).

2. **Encode Faces**  
   Run encoding script to convert images into numerical facial data.

3. **Run Attendance System**  
Detects live faces and matches with encodings.


4. **Log Attendance**  
A new `.xlsx` or `.csv` will be created in `/attendance/` with the current date and time.

---

## ⚙️ Installation

### 🐍 Create a Virtual Environment (Recommended)
```bash
python -m venv venv
venv\Scripts\activate  # Windows

pip install -r requirements.txt
pip install face_recognition opencv-python dlib pandas numpy
pip install dlib‑19.22.99‑cp310‑cp310‑win_amd64.whl

