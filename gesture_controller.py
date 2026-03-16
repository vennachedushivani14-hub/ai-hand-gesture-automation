import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            landmarks = []
            for id, lm in enumerate(handLms.landmark):
                landmarks.append((lm.x, lm.y))

            if len(landmarks) > 0:

                thumb = landmarks[4][1]
                index = landmarks[8][1]

                if thumb < index:
                    pyautogui.press("right")
                    cv2.putText(img, "NEXT SLIDE", (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)

                else:
                    pyautogui.press("left")
                    cv2.putText(img, "PREVIOUS SLIDE", (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)

    cv2.imshow("Gesture Controller", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()