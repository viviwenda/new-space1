import cv2
from ultralytics import YOLO

model = YOLO("yolo11n.pt")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)   # DSHOW 让 Windows 摄像头启动更快

# 提高分辨率，画面更清楚
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ok, frame = cap.read()
    if not ok:
        break
    # conf=0.4: 只显示置信度>40%的框，减少乱框
    result = model.predict(frame, conf=0.4, verbose=False)[0]
    cv2.imshow("YOLO real-time detection - Press ESC to exit", result.plot())
    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
