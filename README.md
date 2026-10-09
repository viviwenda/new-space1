# new-space1
aiu二面任务工作日志
#LM stdio本地部署
1.开始想着直接从网上下载，结果很慢很慢<img width="1706" height="1279" alt="67b9c0b7f84a0e51c59f53841ac23fd6" src="https://github.com/user-attachments/assets/52a42546-c25e-4df9-87c8-4398dc78e9b2" />
2.然后在ai的指导下上网搜夸克网盘，发现直接找到的教程特别冗长，最后自己在b站找到方便的安装包部署LM stdio<img width="1706" height="1279" alt="8de48e15d50e2e3aefed0f1f3b16a779" src="https://github.com/user-attachments/assets/8fc062c1-c984-4544-b527-002fa59676cb" />
3.本地大模型部署验证：使用 LM Studio 成功在本地部署 Qwen2.5-0.5B-Instruct 轻量级模型。
完成模型加载及初步对话测试，验证本地环境可正常作为 Model Provider 运行。<img width="1706" height="1279" alt="599b83a24e55c270e44b3e6a52328329" src="https://github.com/user-attachments/assets/7983327a-3236-4aca-9871-f2033cfd28b0" />











#yolo实时推理部署
1. 要做什么
让训练好的 YOLO11n 模型"动起来"：调用笔记本摄像头，对画面逐帧检测、实时画框。选型：YOLO11n（CPU 上跑得动的最轻量模型）+ OpenCV 取流 + 本地 Python 脚本。
2. 跑通最小流程：核心就是一个循环：读帧 → 推理 → 画框 → 显示。中间报错多次，比如下载时yolo11n.pt报错，问kimi说它本该自动从 GitHub 下载，但你的网络连不上 GitHub，下载失败,让我下WATT网络加速器。结果还是不行，换了一个ai,问minimax
