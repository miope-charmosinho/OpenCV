import numpy as np
import cv2

dicio = {'black' : (0, 0, 0),
         'white' : (255, 255, 255),
         'red' : (0, 0, 255),
         'green' : (0, 255, 0),
         'blue' : (255, 0, 0)}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hight, width, _ = frame.shape

    l = 10
    h = 10

    point = frame[int(hight/2), int(width/2)]

    print(dicio['black'])
    print(point)


    for color in dicio:
        if (np.array_equal(dicio[color], point)):
            font = cv2.FONT_HERSHEY_SIMPLEX 
            frame = cv2.putText(frame, color, (int(hight/2 - 10/2), int(width/2 - 10/2)), font, 1, (0,255,128), 3, cv2.LINE_AA)


    cv2.imshow('Image', frame)
    #cv2.imshow('Black and White', where)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()