import cv2


# function to place and resize images on face
def face_find(frame, final, img, rect, scaling, wwarp_factor=3.0,
              hwarp_factor=2.5):
    final = frame
    # face coordinates
    (x, y, w, h) = rect
    # scaling values
    (sw, sh, ow, oh) = scaling
    # resizing image wrt scaling factors
    img = cv2.resize(img, (int(w * sw), int(h * sh)))
    alpha = img[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha
    ow = int(ow / wwarp_factor * w)
    oh = int(oh / hwarp_factor * h)
    try:
        for c in range(0, 3):
            yh = y + oh
            xw = x + ow
            img0 = img.shape[0]
            img1 = img.shape[1]
            final[yh: yh + img0, xw: xw + img1, c] = \
                (alpha * img[:, :, c] +
                 alpha_l * frame[yh: yh + img0, xw: xw + img1, c])
    except Exception as ex:
        print(ex)
    return final


def process_screen():
    # capture vid from cam
    vidcapture = cv2.VideoCapture(0)

    while True:
        _, block = vidcapture.read()
        _, blockfin = vidcapture.read()
        # assign images to variables
        sgs = g_og
        mst = m_og
        bw = cv2.cvtColor(block, cv2.COLOR_BGR2GRAY)
        # detect faces and stores
        faces = face_cascade.detectMultiScale(bw, 1.3, 10)
        for (x, y, w, h) in faces:
            # drawing rect around face
            cv2.rectangle(block, (x, y), ((x + w), (y + h)),
                          (0, 255, 0), 2)
            final = face_find(block, blockfin, sgs, (x, y, w, h),
                              (0.8, 0.5, 0.5, 0.15), wwarp_factor=3,
                              hwarp_factor=1)
            final = face_find(final, final, mst, (x, y, w, h),
                              (0.7, 0.25, 0.5, 0.9), wwarp_factor=2.5,
                              hwarp_factor=1.5)
        cv2.imshow('final', final)
        k = cv2.waitKey(1) & 0xFF
        if k == 27 or k == ord('q'):
            break
    cv2.destroyAllWindows()
    return None


if __name__ == '__main__':
    face_cascade = cv2.CascadeClassifier(r'C:\Users\achyu\PycharmProjects\FaceFilter\haar-cascade-files-master'
                                         r'\haar-cascade-files-master\haarcascade_frontalface_default.xml')
    g_og = cv2.imread('Glasses.png', cv2.IMREAD_UNCHANGED)
    m_og = cv2.imread('Moustache.png', cv2.IMREAD_UNCHANGED)
    process_screen()
