# new-space1
#aiu二面任务工作日志
#LM stdio本地部署
1.开始想着直接从网上下载，结果很慢很慢<img width="1706" height="1279" alt="67b9c0b7f84a0e51c59f53841ac23fd6" src="https://github.com/user-attachments/assets/52a42546-c25e-4df9-87c8-4398dc78e9b2" />
2.然后在ai的指导下上网搜夸克网盘，发现直接找到的教程特别冗长，最后自己在b站找到方便的安装包部署LM stdio<img width="1706" height="1279" alt="8de48e15d50e2e3aefed0f1f3b16a779" src="https://github.com/user-attachments/assets/8fc062c1-c984-4544-b527-002fa59676cb" />
3.本地大模型部署验证：使用 LM Studio 成功在本地部署 Qwen2.5-0.5B-Instruct 轻量级模型。
完成模型加载及初步对话测试，验证本地环境可正常作为 Model Provider 运行。<img width="1706" height="1279" alt="599b83a24e55c270e44b3e6a52328329" src="https://github.com/user-attachments/assets/7983327a-3236-4aca-9871-f2033cfd28b0" />


#搭建智能体，并通过API的形式，接入到自己的应用中（cli）
1.尝试dify海外网站连不上，用的扣子网页版，搭建智能体华农二面编程问题解答助手并部署<img width="1706" height="1279" alt="4ae36a46caa855662610d3ff8ff01fa7" src="https://github.com/user-attachments/assets/5640b82d-7dfb-4fa7-8247-6130189394a5" />，一路顺利。
2.然后卡在API，上b站专门搜扣子api的相关教程，结合扣子本身给予的入门讲解制作得到API Token,和专属网址url,去 扣子开放平台 API 文档 申请个人访问令牌（PAT）。通过python脚本成功调用扣子API，完成了CLI形式的应用接入。在vs code 里安装插件python<img width="1706" height="1279" alt="77e27381f5fe0effa81feb935535c3fe" src="https://github.com/user-attachments/assets/2e9dc1a1-8933-4316-92d3-f79b4386c823" />
，然后在vs code里新建一个test.py（python）文件，并在终端中运行python文件<img width="1706" height="1279" alt="8ed41d68d39e6ee465828d987a5a90ba" src="https://github.com/user-attachments/assets/b4da5f34-a5db-4791-9b09-c39a5c34095f" />简单介绍一下里面写了啥：在代码里写了“请简单介绍自己，ai回复为纯文本

#













#yolo实时推理部署
1. 要做什么
让训练好的 YOLO11n 模型"动起来"：调用笔记本摄像头，对画面逐帧检测、实时画框。选型：YOLO11n（CPU 上跑得动的最轻量模型）+ OpenCV 视觉 + 本地 Python 脚本。
2. 跑通最小流程：核心就是一个循环：读帧 → 推理 → 画框 → 显示。中间报错多次，比如下载时yolo11n.pt报错，问kimi说它本该自动从 GitHub 下载，但你的网络连不上 GitHub，下载失败,让我下WATT网络加速器假装自己是GitHub。结果还是不行，换了一个ai,问minimax说把WATT关掉，因为里面SSL证书是自签的python不认，搞得我一团乱麻，然后全部推翻重来。经历询问各种ai对比试验，各种报错，最后是这三条成功整出一个模糊的镜头，以下是图片<img width="1279" height="1706" alt="cb99e8357ee95693df2a40787fe93139" src="https://github.com/user-attachments/assets/706c4be8-a58d-4c4a-8d65-e8c9c97508a8" />
conda activate yolo
cd C:\Users\HUAMEI
yolo train model=yolo11n.pt data=coco8.yaml epochs=5 imgsz=640
3.问题：画面很糊，置信度只有 0.28
排查后发现是华为本的摄像头是键盘上的弹出式设计，我忘了把它按弹出来，镜头缩在键帽后面偷拍，画面自然又暗又糊；加上分辨率只有 640×480。
4.最后在ai给的代码打开vs code修改分辨率1280×720<img width="1279" height="1706" alt="95556bb8c0f6c0fc1dc6dbe296569e93" src="https://github.com/user-attachments/assets/f2b9eb3d-3bf9-4b13-bb16-d5675439ef62" />
5. 诚实声明
脚本的编写借助了 AI 辅助
