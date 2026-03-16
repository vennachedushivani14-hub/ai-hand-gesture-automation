import cv2
import mediapipe as mp
import pyautogui

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            landmarks = []

            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                landmarks.append((cx, cy))

            if len(landmarks) != 0:

                x1, y1 = landmarks[8]
                x2, y2 = landmarks[4]

                screen_x = screen_width * x1 / w
                screen_y = screen_height * y1 / h

                pyautogui.moveTo(screen_x, screen_y)

                if abs(y1 - y2) < 30:
                    pyautogui.click()
                    cv2.putText(img, "CLICK", (50,50),
                    cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)

    cv2.imshow("Virtual Mouse", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()