from matplotlib import scale
import torch
import numpy as np
import cv2

def main():
  # custom dataset을 불러옴 
  model = torch.hub.load('ultralytics/yolov5', 'custom', path='../CustomTrain/ex2-WakeUp/last.pt', force_reload=True)

  cap = cv2.VideoCapture(0)

  # frame이 연속으로 몇 번 찍히는지 저장
  frame_count = 0

  while cap.isOpened():
      # 이미지 읽어옴
      ret, frame = cap.read()
      
      # 불러온 모델에 캡쳐한 frame을 넣고 detection 진행
      results = model(frame)
      
      # detection이 진행된 results에서 어떤 라벨이 뽑혔는지와, 그 라벨의 bounding box에 대한 정보를 labels와 cord에 담음
      labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]

      # detection된 수를 뽑음
      number_detection = len(labels)

      count = 0 # 
      x_shape, y_shape = frame.shape[1], frame.shape[0]
      
      ok = 0 # OK sign이 총 몇개가 있는지 저장
      OK = 15 # OK의 라벨 번호

      # 발견된 detection 수만큼 loop를 돌며, 
      for i in range(number_detection):
          row = cord[i]
          probability = row[4] # 검출된 객체 cord[i]의 confidence 깂
          count += 1

          if probability >= 0.3: # 0.3 이상으로 확신하는 경우만 바운딩 박스를 그림
              x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
              bgr = (0, 255, 0)
              cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)

      # 검출된 값이 하나라도 있으면 frame_count를 1로 늘리지만
      if (count > 0):
        frame_count += 1
      # 검출된 값이 없다면 frame_count를 다시 0으로 고정
      else:
        frame_count = 0

      # 증가시킨 frame_count값이 50이상으로 유지된다면, OK-sign이라고 인식
      if (frame_count >= 50):
        cv2.putText(frame, "OK sign detected", (20,150), cv2.FONT_HERSHEY_PLAIN, 4 , (0,0,255), 10)

      print(frame_count)
      cv2.imshow('OK - sign detection', frame)
      
      if cv2.waitKey(10) & 0xFF == ord('q'):
          break

  # 자원 해제
  cap.release()
  cv2.destroyAllWindows()

if __name__ == "__main__":
  main()