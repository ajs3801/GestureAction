# GestureAction
This repository is for implementing the variety of functionality through hand gesture in front of user's DESKTOP

```CustomTrain``` : There are toolkits for all project to customize your own data

```Library``` : Library study folder

```main``` : results of project

```Model```: save model

## posture
(1) Use opensource MediaPipe -> result:1 , result:6

(2) Use deep learning -> result:2 , result:3

## gesture
(3) Gesture Recognition (hand) -> result:4

(4) skeleton MHI (action recognition) -> result:5

## [result:1] : using hand-joint to scroll down and up

### preview
![Screen_Recording_2022-06-24_at_5_28_17_PM_AdobeExpress](https://user-images.githubusercontent.com/43237393/175544041-4d64f946-08b5-438e-bcd9-70dfc1471437.gif)

### description
If you get close the distance between the thumb and index finger, the scroll will move toward up.
If you get close the distance between the thumb and ring finger, the scroll will move toward down.

### where?
You can see the code in [this](https://github.com/ajs3801/GestureAction/blob/main/main/01_ScrollDownAndUpHandJoint.py)

## [result:2] : using deep learning to scroll down and up (yolov5 and pytorch)

### preview
![ScrollUPandDownCut_AdobeExpress](https://user-images.githubusercontent.com/43237393/176349183-19b55d5c-d68b-448c-986b-ef83d50ffbf7.gif)

### description
If you make your hand shape to uppoint, the scroll will move toward up.
If you make your hand shape to downpoint, the scroll will move toward down.

### where?
You can see the code in [this](https://github.com/ajs3801/GestureAction/blob/main/main/03_ScrollDownAndUpDeeplearning.py)

### improvement
> It is not accurate to detect the sign well, so the further improvment of dataset will be required.

## [result:3] : using deep learning based AI to wake up the gesture recognition program

### preview
![wakeup_AdobeExpress](https://user-images.githubusercontent.com/43237393/176349977-1a336a47-7ff7-45cf-9fdc-7e7fec3fdcee.gif)

### description
If you maintain the position-OK sign while 5sec, the recognition detect will be pop-up.
It can be used to wake up the heavy AI model and turn off the AI model.

### where?
You can see the code in [this](https://github.com/ajs3801/GestureAction/blob/main/main/04_DetectOK.py)

### improvement
> It is not accurate to detect the sign well, so the further improvment of dataset will be required.

## [result:4] : using tensorflow LSTM

### preview
> add later

### description
If you do gesture slicing to left -> recognize that gesture is move left.

### where?
You can see the code in [this](https://github.com/ajs3801/GestureAction/blob/main/main/05_LeftAndRight.py)

### improvement
> implement this not only using holistic but also pose

## [result:5] : skeleton MHI and image classification

### preview
<img width="400" alt="Screen Shot 2022-07-16 at 10 15 31 PM" src="https://user-images.githubusercontent.com/43237393/179356495-ff91775c-0eed-4072-a58d-9e985a5bc063.png">


### description
Train the left moving skeleton MHI picture and also the right moving skeleton MHI picture.
and resize it to 480x160 and put it to the model.

### where?
> add later

### improvement
> apply multi-action recognition

## [result:6] : mediapipe posture detection toolkit

### preview
> ADD LATER


### description
> ADD LATER

### where?
> ADD LATER

### improvement
> make more dataset

## NEXT DEVELOPING 
> POSE ACTION RECOGNITION USING SKELETON COORDINATE LSTM

> ACTION RECOGNITION USING SKELETON MHI

> Skeleton MHI + Object Detection
## Model
```actionmodelv1.pt``` : detect squat and stand

# Make your own model
In ```CustomTrain/custom``` folder, you can make your own custom dataset and train it through yolo v5.

If you want to see how to train your custom dataset, see this [page](https://velog.io/@ajs3801/Yolo-PyTorch-custom-dataset-%ED%95%99%EC%8A%B5%EC%8B%9C%ED%82%A4%EA%B8%B0-1)
