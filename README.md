# GestureAction
This repository is for implementing the variety of functionality through hand gesture in front of user's DESKTOP

# Just sketch of this project
1. Detect hand-joint
2. Extract the data between each joint and add functionality
3. Extend functionality to Web or App

## 1. Detect hand-joint

how? Maybe try to use MediaPipe 
- [link to MediaPipe github page](https://github.com/google/mediapipe)
- [link to MediaPipe information](https://google.github.io/mediapipe/getting_started/python.html)

the extracted data through MediaPipe
<img width="914" alt="Screen Shot 2022-05-26 at 7 56 47 PM" src="https://user-images.githubusercontent.com/43237393/170474742-b8905415-85fe-4448-b4ce-01bbbd7c5c0f.png">

## 2. Extract the data between each joint and add functionality

(idea 1), gesture-motion-detection to control Window's volumn.

how to control window's audio? Maybe use pycaw

- [link to pycaw github page](https://github.com/AndreMiras/pycaw)
- [link to pycaw information](https://pypi.org/project/pycaw/)

(idea 2), gesture-motion-detection to swap multi-desktop

how to implement? Maybe use pyautogui to control keyboard

[link to see more about pyautogui](https://pyautogui.readthedocs.io/en/latest/index.html)

## 3. Extend functionality to Web or App

### 1. javascript
MediaPipe in javascript [(link to see more)](https://google.github.io/mediapipe/getting_started/javascript.html)

MediaPipe in javascript information [(link to see more)](https://google.github.io/mediapipe/solutions/hands#javascript-solution-api)

### 2. Android
MediaPipe in Android [(link to see more)](https://google.github.io/mediapipe/getting_started/android.html)

### 3. iOS
MediaPipe in iOS [(link to see more)](https://google.github.io/mediapipe/getting_started/ios.html)

## License information

MediaPipe | Apache License 2.0 [Apache License](https://www.apache.org/licenses/LICENSE-2.0)

pycaw | MIT License [MIT License](https://opensource.org/licenses/MIT)
