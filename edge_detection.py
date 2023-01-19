import cv2 as cv

# capture = cv.VideoCapture(0)
# frame = capture.read()
# img = cv.imread("capture", 1)
cap = cv.VideoCapture(0)

while True:
    isSuccess, img = cap.read()
    blur_img = cv.GaussianBlur(img, (7, 7), 0)

    img = cv.Canny(blur_img, 100, 100)
    cv.circle(img, (20, 40), 30, (255, 0, 0), thickness=3)
    cv.circle(img, (20, 435), 30, (255, 0, 0), thickness=3)
    cv.circle(img, (600, 50), 30, (255, 0, 0), thickness=3)
    cv.circle(img, (600, 450), 30, (255, 0, 0), thickness=3)
    cv.putText(img, 'edge detection', (0, 225),cv.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 1)
    cv.imshow('Circle image', img)

    if cv.waitKey(20) & 0xFF == ord('q'):
        break




