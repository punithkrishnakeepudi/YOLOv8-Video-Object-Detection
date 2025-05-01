import cv2
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Input video (change to 0 for webcam)
video_path = "sample.mp4"
cap = cv2.VideoCapture(video_path)

# Get video properties
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Output video writer
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output_labeled.mp4", fourcc, fps, (width, height))

# Process video
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Inference
    results = model(frame, verbose=False)

    # YOLO-styled frame
    labeled_frame = results[0].plot()

    # Save to output
    out.write(labeled_frame)

# Clean up
cap.release()
out.release()
