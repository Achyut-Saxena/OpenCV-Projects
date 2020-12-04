import cv2

cam = cv2.VideoCapture(0)
while True:
    _, block1 = cam.read()
    block1 = cv2.flip(block1, 1)
    hsv = cv2.cvtColor(block1, cv2.COLOR_BGR2HSV)
    mask = cv2.GaussianBlur(block1, (5, 5), 0)
    g_frame = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    hc = cv2.HoughCircles(g_frame, cv2.HOUGH_GRADIENT, 1, 200,
                          param1=50, param2=70, minRadius=20, maxRadius=200)
    if hc is not None:
        for circle in hc[0, :]:
            circlepresent = cv2.circle(block1, (int(circle[0]),
                                       int(circle[1])), int(circle[2]),
                                       (255, 0, 0), thickness=2)
        cv2.imshow("original", circlepresent)
    else:
        cv2.imshow("original", block1)
    k = cv2.waitKey(5)
    if k == 27:
        break
cv2.destroyAllWindows()
cam.release()
