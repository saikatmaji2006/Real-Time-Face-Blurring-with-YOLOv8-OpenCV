# 🕶️ Real-Time Face Blurring with YOLOv8 & OpenCV

Automatically detect and blur faces from live webcam or video input using **YOLOv8** and **OpenCV** — a fast, privacy-focused computer vision tool.

---

## 🎥 Demo

> _[https://github.com/saikatmaji2006/Real-Time-Face-Blurring-with-YOLOv8-OpenCV/blob/main/Demo/DemoVideoFaceBlur.mp4]_  

---

## 🚀 Features

- 🧠 Deep learning-based face detection with `yolov8n-face.pt`
- ⚡ Real-time frame processing (via webcam or video input)
- 🛡️ Safe bounding box handling to avoid frame slicing errors
- 🧊 Gaussian blur applied to all detected faces
- 💻 Lightweight and fast — works locally

---

## 🛠 Tech Stack

- **Python**
- **OpenCV** – for image/video processing
- **YOLOv8** – face detection using pretrained `yolov8n-face.pt` model (from Ultralytics)


---

## 📦 Installation

```bash
git clone https://github.com/saikatmaji2006/Real-Time-Face-Blurring-with-YOLOv8-OpenCV
pip install -r requirements.txt
