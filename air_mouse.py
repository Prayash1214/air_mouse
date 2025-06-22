import cv2
import mediapipe as mp
import pyautogui
import os 
import time
cv2.namedWindow("frame",cv2.WINDOW_NORMAL)
time.sleep(1)
os.system("wmctrl -r frame -b add,above")

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

screen_w, screen_h = pyautogui.size()

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    id_6 = None
    id_8 = None
    id_4 = None
    id_3 = None
    id_12 = None
    id_10 = None

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 8:
                    id_8 = cy
                    mouse_x = lm.x * screen_w
                    mouse_y = lm.y * screen_h
                if id == 6:
                    id_6 = cy
                if id == 4:
                    id_4 = cx
                if id == 3:
                    id_3 = cx
                if id == 12:
                    id_12 = cy
                if id == 10:
                    id_10 = cy

            if id_8 is not None and id_6 is not None  and id_4 is not None and id_3 is not None and id_12 is not None  and id_10 is not None:
                if id_8 < id_6:
                    pyautogui.moveTo(mouse_x, mouse_y)
                if id_12 < id_10:
                    pyautogui.click(button='right')
                if id_4 > id_3:
                    pyautogui.click(button='left')

            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
