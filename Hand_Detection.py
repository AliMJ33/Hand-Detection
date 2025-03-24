import cv2
from cvzone.HandTrackingModule import HandDetector

frame = cv2.VideoCapture(0)
frame.set(3, 1280)
frame.set(4, 720)

handDetector = HandDetector(detectionCon= 0.8)

while(True):
    _, img = frame.read()
    hands = handDetector.findHands(img)

    cv2.imshow("My Hands", img)
    if cv2.waitKey(1) == 27:
        break

frame.release()
cv2.destroyAllWindows()
