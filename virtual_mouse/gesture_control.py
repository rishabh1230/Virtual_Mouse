import math

class GestureController:
    def __init__(self, click_threshold=30):
        self.click_threshold = click_threshold

    def is_click(self, landmarks):
        thumb = landmarks[4][1], landmarks[4][2]
        index = landmarks[8][1], landmarks[8][2]

        distance = math.hypot(index[0] - thumb[0],
                               index[1] - thumb[1])
        return distance < self.click_threshold
