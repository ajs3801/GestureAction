from sqlite3 import DatabaseError
from datetime import datetime
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt
import time
import uuid

# Path for exported data, numpy arrays
DATA_PATH = os.path.join('Data') 

# Actions that we try to detect
actions = np.array(['squat','pushup','lunge'])

# Thirty videos worth of data
no_sequences = 5

# Videos are going to be 30 frames in length
sequence_length = 30

cap = cv2.VideoCapture(0)
# Set mediapipe model 

def ProcessingReverse(videopath,action,action_num,sequence,flip):
  cap = cv2.VideoCapture(videopath)

  fourcc = cv2.VideoWriter_fourcc(*'DIVX')
  width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
  height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
  fps = cap.get(cv2.CAP_PROP_FPS)
  fps = int(fps)
  
  reverse_videopath = os.path.join(DATA_PATH,action+'-up','{}-{}-{}-{}-{}.avi'.format(str('0'+str(action_num+1)),datetime.today().strftime('%Y%m%d%H%M'),str(sequence),str(fps),str(flip)))
  out = cv2.VideoWriter(reverse_videopath, fourcc, fps, (width,height))

  count = 0
  ret = True
  frame_list = []

  while(ret == True):
    ret, vid = cap.read()
    if (ret == False):
      break
    frame_list.append(vid)
    count += 1

  # print('count :' ,count)

  frame_list.reverse()

  # 역재생
  for frame in frame_list:
    out.write(frame)
    if cv2.waitKey(10) and 0xFF == ord("q"):
        break

  cap.release()
  out.release()
  cv2.destroyAllWindows()

  if (flip == 0):
    print('save the original reverse video to {}'.format(videopath))
  else:
    print('save the flipped reverse video to {}'.format(videopath))

# NEW LOOP
# Loop through actions
action_num = 1
for action in actions:
    # Loop through sequences aka videos
    for sequence in range(no_sequences):
        # Loop through video length aka sequence length
        fourcc = cv2.VideoWriter_fourcc(*'DIVX')

        # Read feed
        width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        fps = int(fps)
        # videoname = str('0'+str(action_num)+'-'+str(datetime.today().strftime('%Y%m%d%H%M'))+'-'+str(sequence)+'-'+str(fps)+'-'+str(0))
        # videoname_flip = str('0'+str(action_num)+'-'+str(datetime.today().strftime('%Y%m%d%H%M'))+'-'+str(sequence)+'-'+str(fps)+'-'+str(1))
        #                                       운동번호 일련번호 번호 프레임 flip(true or false)
        videopath = os.path.join(DATA_PATH,action+'-down','{}-{}-{}-{}-{}.avi'.format(str('0'+str(action_num)),datetime.today().strftime('%Y%m%d%H%M'),str(sequence),str(fps),str(0)))
        videopath_flip = os.path.join(DATA_PATH,action+'-down','{}-{}-{}-{}-{}.avi'.format(str('0'+str(action_num)),datetime.today().strftime('%Y%m%d%H%M'),str(sequence),str(fps),str(1)))

        out = cv2.VideoWriter(videopath, fourcc, fps, (width,height))
        out_flip = cv2.VideoWriter(videopath_flip, fourcc, fps, (width,height))

        print('Collecting frames for {} Video Number {}'.format(action, sequence))
        for frame_num in range(sequence_length):
            ret, frame = cap.read()
            show_frame = frame.copy()

            print('Collecting frames for {} Video Number {}'.format(action, sequence))
            cv2.putText(show_frame,'Collecting frames for {} Video Number {}'.format(action, sequence), (50,50), cv2.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)
            cv2.imshow('Realtime view',show_frame)

            frame_flip = cv2.flip(frame, 1)
            # NEW Apply wait logic
            if frame_num == 0: 
                print('STARTING COLLECTION for {} wait...'.format(action))
                # cv2.imshow('Data collection', frame)
                cv2.waitKey(5000)
                # Show to screen

                out.write(frame) # 영상데이터만 저장 (소리 X)
                out_flip.write(frame_flip)

            else: 
                # Show to screen
                # cv2.imshow('Data collection', frame)
                out.write(frame) # 영상데이터만 저장 (소리 X)
                out_flip.write(frame_flip)

            # Break gracefully
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        
        print('save to ', videopath)
        print('save to ', videopath_flip)

        ProcessingReverse(videopath,action,action_num,sequence,0)
        ProcessingReverse(videopath_flip,action,action_num,sequence,1)
        
        print('######## DONE ########')

        cv2.waitKey(1000)
    action_num += 2

out.release()
out_flip.release()
cap.release()
cv2.destroyAllWindows()