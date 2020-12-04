import cv2

from mss import mss

import numpy

import pyautogui

# auto start the game
pyautogui.press('up')

keyDown = 0
while True:

    # Take a screenshot and crop out required area.
    sct = mss()
    monitor = {"top": 220, "left": 35, "width": 960, "height": 300}
    block = numpy.array(sct.grab(monitor))
    block_bw = cv2.cvtColor(block, cv2.COLOR_BGR2GRAY)

    # Find the obstacles and the dinosaur
    _, thresh = cv2.threshold(block_bw, 127, 255, 0)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE,
                                   cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if 300 <= cv2.contourArea(c) <= 5000:
            x, y, w, h = cv2.boundingRect(c)
            # If the obstacle is of right size
            if w/h < 2:
                cv2.rectangle(block, (x, y), (x + w, y + h), (0, 255, 0), 2)

                # Jump over cacti
                if (x < 180 and (w/h) < 0.6) or \
                   (x < 200 and y > 190):
                    if keyDown:
                        pyautogui.keyUp('down')
                        keyDown = 0
                    pyautogui.press('up')
                    break

            # keep ducking if no obstacle is to be jumped over.
            elif not keyDown:
                pyautogui.keyDown('down')
                keyDown = 1
                break

    # Display capture area.
    cv2.imshow("Screen capture", block)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
