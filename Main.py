import cv2
from cvzone.PoseModule import PoseDetector
import time

##########   VIDEO   ##########
cap = cv2.VideoCapture(0)
#cap.set(3, 1920)
#cap.set(4, 1080)

##########   DETECTORS   ##########
bodyDetector = PoseDetector()
def SendAlert(text):
    print(text)
##########   PROCESSING   ##########
while True:
    success, img = cap.read()

    img = bodyDetector.findPose(img)

    lmList, bboxInfo = bodyDetector.findPosition(img, bboxWithHands=True)
    try:
        ##########   LEFT LEG   ##########
        angle = int(bodyDetector.findAngle(img, 23, 25, 27))

    except:
        pass

    if bboxInfo:
        center = bboxInfo["center"]
        cv2.circle(img, center, 5, (255, 0, 255), cv2.FILLED)

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('\u0008'):
        break

    elif  cv2.waitKey(1) & 0xFF == ord('s'):
        if 100 >= angle >= 40:
            SendAlert("Sentado")
        else:
            SendAlert("Em pé")

    else:
        continue

        vid.release()
        cv2.destroyAllWindows()