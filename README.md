# 📷 CCTV Attendance System

An AI-based attendance system using face recognition technology that captures faces through CCTV or webcam feed and automatically marks attendance. This system is designed for educational institutions, offices, and organizations looking for automated, contactless, and efficient attendance management.

---

## 📁 Project Structure

CCTV_Attendance_System/
├── attendance/ # Logs Excel/CSV attendance reports
├── attendance1/ # (Optional) Backup/secondary log folder
├── capture_image/ # Script to register new user images
├── encode_faces/ # Generates encodings from known faces
├── encodings/ # Pickled files for faster recognition
├── known_faces/ # Directory of registered face images
├── attendance_system/ # Main codebase (alternative structure)
├── .dist/ # Build/cache-related folders (auto-generated)
├── .venv/ # Python virtual environment (optional)
├── dlib-19.22.99-...whl # Optional offline dlib wheel
├── encodings.pickle # Serialized face encodings
├── solomon_encoding.npy # NumPy array of face data
├── recognize_faces_final.py # 🔴 Main face recognition & attendance script
├── test.py # Script for basic testing/validation
├── requirements.txt # Python dependencies
└── README.md # Project documentation

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

🚀 Usage
✍️ Registering New Faces
python capture_image/capture_image.py

🧠 Encode Face Data
python encode_faces/encode_faces.py

🎥 Start Attendance System
python recognize_faces_final.py
```
📊 Output Example:

Excel file: Attendance_2025-06-10.xlsx

Columns: Name | Time | Date

🛠️ Future Enhancements:

🖥️ Add GUI for admin panel

🌐 Web-based dashboard

🔔 Alert system for unknown faces

🧾 Daily summary reports via email


---

### 🙋‍♂️ Author

**Solomon Goodwin Alexander**  
🎓 B.Tech in CSE (Data Science), St. Vincent Pallotti College of Engineering & Technology, Nagpur  
📍 Nagpur, Maharashtra, India  

🔗 [GitHub Profile](https://github.com/Solomon-Alexander1)  
🔗 [LinkedIn Profile](https://www.linkedin.com/in/solomon-alexander-184733170/)  
📧 Email: solomonalex99210@gmail.com  

---

📜 **License**  
This project is licensed under the **MIT License** – you are free to use, modify, and share it for personal or educational purposes.  

