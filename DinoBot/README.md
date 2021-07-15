# Automatic Dino Player
A program that plays the chrome dino game for you using opencv.

# Problem Statement
***Design an OpenCV program so that it captures the screen and allows one to play the Chrome Dino Game without Using keyboard***

# Working
1. Capturing screen using ```mss``` library
2. Converting the captured screen from BGR to GRAY
3. Finding Contours
4. Alloting key-press using the ```pyautogui``` library

# Setup
Make sure the setup is as shown in the picture. 
To get the same setup, give the left 1/2 of the screen to chrome. 
This can be done in windows by using the window + left arrow key.


![2020-10-13 18-37-14](https://user-images.githubusercontent.com/69965983/95869275-d4182e80-0d88-11eb-9dfe-fa35c0c6e5cf.gif)


# Scope of Improvement:
*Can be made more accurate using better contour constraints*
