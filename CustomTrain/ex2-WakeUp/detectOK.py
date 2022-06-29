from matplotlib import scale
import torch
import numpy as np
import cv2

model = torch.hub.load('ultralytics/yolov5', 'custom', path='last.pt', force_reload=True)

cap = cv2.VideoCapture(0)

frame_count = 0

while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    
    labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]

    n = len(labels)
    count = 0
    x_shape, y_shape = frame.shape[1], frame.shape[0]
    
    ok = 0
    OK = 15

    for i in range(n):
        if (labels[i] == OK):
            ok += 1
    
        count += 1
        row = cord[i]
        if row[4] >= 0.3:
            x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
            bgr = (0, 255, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)

    if (count > 0):
      frame_count += 1

    else:
      frame_count = 0

    if (frame_count >= 50):
      cv2.putText(frame, "Recognition detected", (20,150), cv2.FONT_HERSHEY_PLAIN, 3 , (0,0,0), 5)

    print(frame_count)

    # cv2.imshow('YOLO', np.squeeze(results.render()))
    cv2.imshow('yolo', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()