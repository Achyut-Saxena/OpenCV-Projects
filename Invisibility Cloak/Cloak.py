import time

import cv2

import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
print("Invisibility cloak starts working in:", end="")
for i in range(5):
    print(i+1, end=" ")
    time.sleep(i)
background = 0
for _ in range(30):
    ret, background = cap.read()
background = np.flip(background, axis=1)
while True:
    ret, img = cap.read()
    img = np.flip(img, axis=1)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    green_low_lim = np.array([25, 52, 72])
    green_up_lim = np.array([102, 255, 255])
    mask1 = cv2.inRange(hsv, green_low_lim, green_up_lim)
    mask2 = cv2.inRange(hsv, green_low_lim, green_up_lim)
    mask = mask1+mask2
    mask2 = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(img, img, mask=mask2)
    res2 = cv2.bitwise_and(background, background, mask=mask1)
    final_output = res1+res2
    cv2.imshow("Cloak", final_output)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
cap.release()
