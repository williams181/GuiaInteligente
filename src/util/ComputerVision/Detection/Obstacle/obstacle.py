import cv2 as cv
import numpy as np

cap = cv.VideoCapture("data\\videos\\input\\ifpe (30).mp4")

while True:
    _, frame1 = cap.read()
    frame = cv.blur(frame1, (20, 20))
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 40])

    mask = cv.inRange(hsv, lower_black, upper_black)
    res = cv.bitwise_not(mask)
    # cv.imshow('mask',mask)

    contours, _ = cv.findContours(res, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(frame, contours, 0, (0, 255, 0), 3)

    # cv.imshow('res',res)

    coordinates = (250, 100)
    font = cv.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (0, 0, 255)
    thickness = 2

    try:
        cnt = contours[0]

        M = cv.moments(cnt)
        try:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])

        except ZeroDivisionError:
            continue

        if cx < 320:
            text = "A esquerda..."
            # Send signal to motor driver to turn left
        else:
            text = "A direita..."
            # Send signal to motor driver to turn right

    except IndexError:
        continue
    frame = cv.putText(frame, text, coordinates, font,
                       fontScale, color, thickness, cv.LINE_AA)

    
    imS = cv.resize(frame, (960, 540)) 
    cv.imshow("img", imS)

    k = cv.waitKey(15) & 0xFF  # Esc button to quit
    if k == ord('q') or k == 27:
        break

cv.destroyAllWindows()
# cap.release()
