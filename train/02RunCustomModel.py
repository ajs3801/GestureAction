import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2

model = torch.hub.load('ultralytics/yolov5', 'custom', path='', force_reload=True)

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    # custom data로 학습시킨 model에 frame을 넣어 결과 확인
    results = model(frame)
    
    cv2.imshow('Custom', np.squeeze(results.render()))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

