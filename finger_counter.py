import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

tip_ids = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            lm_list = []

            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lm_list.append((cx, cy))

            fingers = []

            if len(lm_list) != 0:

                if lm_list[tip_ids[0]][0] > lm_list[tip_ids[0]-1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

                for id in range(1,5):
                    if lm_list[tip_ids[id]][1] < lm_list[tip_ids[id]-2][1]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                total = fingers.count(1)

                cv2.putText(img, str(total), (50,100),
                cv2.FONT_HERSHEY_SIMPLEX, 3, (0,255,0), 3)

    cv2.imshow("Finger Counter", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()