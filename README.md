# 🚦 Real-Time Object Detection with YOLOv8 🎥🤖

This project showcases **real-time object detection** using [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics) and OpenCV.  
It detects and labels everyday objects like **cars, people, and bikes** in videos — including live footage captured from **Bengaluru city**.  

The script processes an input video (or webcam stream), performs YOLOv8 inference frame by frame, and saves an **annotated output video** with bounding boxes and labels.

---

## 📌 Features
- Runs **YOLOv8n** (lightweight + fast) pre-trained model.  
- Works with both **video files** and **live webcam input**.  
- Outputs annotated video with detected objects.  
- Simple to use with minimal setup.  

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/punithkrishnakeepudi/YOLOv8-Video-Object-Detection.git
cd YOLOv8-Video-Object-Detection
```

### 2️⃣ (Optional) Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

If `requirements.txt` is missing, create one with:
```txt
ultralytics
opencv-python
```

---

## ▶️ Usage

### Run on a video file
```bash
python detect_video.py --video sample.mp4
```

### Run on a webcam (device `0`)
```bash
python detect_video.py --video 0
```

👉 The processed video will be saved as **`output_labeled.mp4`**.

---

## 📂 Project Structure
```
YOLOv8-Video-Object-Detection/
│── detect_video.py        # Main script
│── sample.mp4             # Example input video
│── output_labeled.mp4     # Example output (generated after running)
│── requirements.txt       # Dependencies
│── README.md              # Project documentation
```

---

## 🖼️ Example Output
(Add a screenshot or GIF of your Bengaluru video output here 👌)

---

## 💡 Notes
- You can swap `yolov8n.pt` with another YOLOv8 model (`yolov8s.pt`, `yolov8m.pt`, etc.) for different speed/accuracy tradeoffs.  
- Works with all video formats supported by OpenCV.  
- GPU acceleration is used automatically if available (CUDA).  

---

## 📜 License
This project is licensed under the **MIT License** – feel free to use, share, and modify.
