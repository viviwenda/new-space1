from ultralytics import YOLO
import gradio as gr

model = YOLO("yolo11n.pt")

def detect(img):
    if img is None:
        return None
    result = model.predict(img, verbose=False)[0]
    return result.plot()

demo = gr.Interface(
    fn=detect,
    inputs=gr.Image(label="上传图片"),
    outputs=gr.Image(label="检测结果"),
    title="YOLO 目标检测 Demo",
    description="创智部二面实战演示",
)
demo.launch()   # 自动打开浏览器网页
