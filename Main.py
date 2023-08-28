import cv2
from cvzone.PoseModule import PoseDetector
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://web.whatsapp.com/send/?phone=5511937218726&text&type=phone_number&app_absent=0") #https://web.whatsapp.com/send/?phone=5511976492228&text&type=phone_number&app_absent=0

##########   VIDEO   ##########
cap = cv2.VideoCapture(0)
#cap.set(3, 1920)
#cap.set(4, 1080)

##########   DETECTORS   ##########
bodyDetector = PoseDetector()
def SendAlert():
    browser.find_element(By.XPATH, "//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']").click()
    browser.find_element(By.XPATH, "//div[@class='to2l77zo gfz4du6o ag5g9lrv bze30y65 kao4egtt']").send_keys("""Atenção, temos uma intercorrência no carro
                                                                                                             Nº7854 com destino a estação Perus""")
    time.sleep(5)
    browser.find_element(By.XPATH, "//button[@class='tvf2evcx oq44ahr5 lb5m6g5c svlsagor p2rjqpw5 epia9gcq']").click()
    time.sleep(3)
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
            SendAlert()
        else:
            pass

    else:
        continue

        vid.release()
        cv2.destroyAllWindows()