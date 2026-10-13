import cv2
from ultralytics import YOLO
#python把工具cv2和yolo搬进来
#cv2 （OpenCV）→ 负责眼睛（摄像头）和手（画框、显示窗口）
#YOLO  → 从 ultralytics 库引入"加载模型"的类
model = YOLO("yolo11n.pt")
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)   # DSHOW 让 Windows 摄像头启动更快

# 提高分辨率，画面更清楚
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ok, frame = cap.read()#读帧
    if not ok:
        break
    # conf=0.4: 只显示置信度>40%的框，减少乱框#把不要的扔掉
    result = model.predict(frame, conf=0.4, verbose=False)[0]#取第一张图的结果
    cv2.imshow("YOLO real-time detection - Press ESC to exit", result.plot())#
    if cv2.waitKey(1) == 27:
        break#等一毫秒并听键盘：按下esc就退出

cap.release()#关掉摄像头
cv2.destroyAllWindows()#关掉显示窗口
