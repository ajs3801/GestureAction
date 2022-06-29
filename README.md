# GestureAction
This repository is for implementing the variety of functionality through hand gesture in front of user's DESKTOP

# How to implement?
1. Detect hand-joint
2. Extract the data between each joint and add functionality
3. Extend functionality to Web or App

# 1. Detect hand-joint

1. Use opensource MediaPipe -> result:1
2. Use deep learning -> result:2 , result:3

# 2. Extract the data between each joint and add functionality

## [result:1] : using hand-joint to scroll down and up

### preview
![Screen_Recording_2022-06-24_at_5_28_17_PM_AdobeExpress](https://user-images.githubusercontent.com/43237393/175544041-4d64f946-08b5-438e-bcd9-70dfc1471437.gif)

### description
If you get close the distance between the thumb and index finger, the scroll will move toward up.
If you get close the distance between the thumb and ring finger, the scroll will move toward down.

## [result:2] : using deep learning to scroll down and up (yolov5 and pytorch)

### preview
![ScrollUPandDownCut_AdobeExpress](https://user-images.githubusercontent.com/43237393/176349183-19b55d5c-d68b-448c-986b-ef83d50ffbf7.gif)

### description
If you make your hand shape to uppoint, the scroll will move toward up.
If you make your hand shape to downpoint, the scroll will move toward down.

## [result:3] : using deep learning based AI to wake up the gesture recognition program

### preview
![wakeup_AdobeExpress](https://user-images.githubusercontent.com/43237393/176349977-1a336a47-7ff7-45cf-9fdc-7e7fec3fdcee.gif)

### description
If you maintain the position-OK sign while 5sec, the recognition detect will be pop-up.
It can be used to wake up the heavy AI model and turn off the AI model.

## [idea1] : recognize hand's gesture (movement) (ex)hello, shake hands
> now developing
## License information

MediaPipe | [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

pycaw | [MIT License](https://opensource.org/licenses/MIT)
