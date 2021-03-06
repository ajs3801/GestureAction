import torch
import numpy as np
import cv2
import pyautogui


def main():
  model = torch.hub.load('ultralytics/yolov5', 'custom', path='../CustomTrain/ex1-ScrollUpandScrollDown/last.pt', force_reload=True)

  cap = cv2.VideoCapture(0)
  while cap.isOpened():
      ret, frame = cap.read()
      
      # Make detections 
      results = model(frame)
      
      labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]

      n = len(labels)
      count = 0
      x_shape, y_shape = frame.shape[1], frame.shape[0]
      
      scrollUp = 0
      scrollDown = 0
      SCROLL_UP = 15
      SCROLL_DOWN = 16

      for i in range(n):
          if (labels[i] == SCROLL_UP):
              scrollDown += 1
          
          if (labels[i] == SCROLL_DOWN):
              scrollUp += 1
      
          count += 1
          row = cord[i]
          if row[4] >= 0.3:
              x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
              bgr = (0, 255, 0)
              cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
      
      
      # print("scrollUp : {} | scrollDown : {} | count : {}".format(scrollUp,scrollDown,count))
      
      if (scrollUp > 0):
        print('scroll up')
        pyautogui.scroll(1)

      elif (scrollDown > 0):
        print('scroll down')
        pyautogui.scroll(-1)

      # cv2.imshow('YOLO', np.squeeze(results.render()))
      cv2.imshow('yolo', frame)
      
      if cv2.waitKey(10) & 0xFF == ord('q'):
          break

  cap.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  main()