from ultralytics import YOLO
import cv2
import torch



model = YOLO("Model\yolov8n-face-lindevs.pt")
if torch.cuda.is_available():
    model.to("cuda")
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    results = model.predict(source=frame, conf=0.5,verbose=False)[0]
    h, w, _ = frame.shape  # Get frame dimensions
    for box in results.boxes.xyxy:
        x1, y1, x2, y2 = map(int, box.tolist())
        # # was creating unblur in edges leaking the actual face 
        # # Clamp all coordinates within frame bounds
        # x1 = max(0, min(x1, w))
        # y1 = max(0, min(y1, h))
        # x2 = max(0, min(x2, w))
        # y2 = max(0, min(y2, h))
        # Skip invalid or zero-area boxes
        if x2 <= x1 or y2 <= y1:
            continue

        face = frame[y1:y2, x1:x2]
        blurred = cv2.GaussianBlur(face, (45, 45), 30)
        frame[y1:y2, x1:x2] = blurred

    cv2.imshow("Face blurring",frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()