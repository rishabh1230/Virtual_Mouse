import cv2
from hand_tracking import HandTracker
from mouse_controller import MouseController
from gesture_control import GestureController

cap = cv2.VideoCapture(0)

hand_tracker = HandTracker()
mouse = MouseController()
gesture = GestureController()

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)
    h, w, _ = frame.shape

    landmarks = hand_tracker.find_hand_landmarks(frame)

    if landmarks:
        index_x, index_y = landmarks[8][1], landmarks[8][2]
        mouse.move_mouse(index_x, index_y, w, h)

        if gesture.is_click(landmarks):
            mouse.click()

    cv2.imshow("Virtual Mouse", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
