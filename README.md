# GestureAction
This repository is for implementing the variety of functionality through hand gesture in front of user's DESKTOP

# How to implement?
1. Detect hand-joint
2. Extract the data between each joint and add functionality
3. Extend functionality to Web or App

## 1. Detect hand-joint

Use opensource MediaPipe

- [link to MediaPipe github page](https://github.com/google/mediapipe)
- [link to MediaPipe information](https://google.github.io/mediapipe/getting_started/python.html)

The extracted data through MediaPipe
<img width="914" alt="Screen Shot 2022-05-26 at 7 56 47 PM" src="https://user-images.githubusercontent.com/43237393/170474742-b8905415-85fe-4448-b4ce-01bbbd7c5c0f.png">

The extracted data in Local Desktop

![image](https://user-images.githubusercontent.com/43237393/172122107-08d04c98-65f6-4bf6-831c-ab6291c6ab8f.png)

See this wiki page to see how to do [link](https://github.com/ajs3801/GestureAction/wiki/How-to-use-mediapipe-in-Window-using-Jupyter-notebook)

## 2. Extract the data between each joint and add functionality

### [idea1] : using hand-joint to scroll down and up

### preview
![Screen_Recording_2022-06-24_at_5_28_17_PM_AdobeExpress](https://user-images.githubusercontent.com/43237393/175544041-4d64f946-08b5-438e-bcd9-70dfc1471437.gif)

### description
If you get close the distance between the thumb and index finger, the scroll will move toward up.
If you get close the distance between the thumb and ring finger, the scroll will move toward down.

### how to use

```
main/ScrollDownAndUp.py
```

### [idea2] : using hand joint to wake up the gesture recognition AI
(now developing)

## License information

MediaPipe | [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)

pycaw | [MIT License](https://opensource.org/licenses/MIT)
