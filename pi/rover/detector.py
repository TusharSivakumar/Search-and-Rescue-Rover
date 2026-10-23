"""Victim detection with OpenCV color/shape detection."""

from dataclasses import dataclass
import cv2 as cv
import numpy as np

@dataclass
class Detection:
    center_x: int      # pixels
    center_y: int      # pixels
    area: float        # pixels^2
    # TODO: anything else? A confidence score, a shape label, a bearing angle?


class VictimDetector:
    def __init__(self, hsv_low, hsv_high, min_area):
        self.hsv_high = hsv_high
        self.hsv_low = hsv_low
        self.min_area = min_area
        

    def detect(self, frame_bgr):
        hsv = cv.cvtColor(frame_bgr, cv.COLOR_BGR2HSV)
        mask = cv.inRange(hsv, np.array(self.hsv_low), np.array(self.hsv_high))
        kernel = np.ones((3,3), np.uint8)
        morph = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
        contours, hierarchies = cv.findContours(morph, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        big = [c for c in contours if cv.contourArea(c) >= self.min_area]
        if not big:
            return None
        bigg = max(big, key=cv.contourArea)
        M = cv.moments(bigg)
        if M["m00"] == 0:
            return None
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])

        return Detection(cx, cy, cv.contourArea(bigg))


    def draw(self, frame_bgr, detection):
        if detection is None:
            return frame_bgr
        frame = frame_bgr


        cx, cy = detection.center_x, detection.center_y
        area = detection.area

        GREEN = (0, 255, 0)      # BGR
        WHITE = (255, 255, 255)


        cv.circle(frame, (cx, cy), 6, GREEN, -1)


        radius = int(np.sqrt(area / np.pi))
        cv.circle(frame, (cx, cy), radius, GREEN, 2)


        label = f"VICTIM  area={int(area)}"
        cv.putText(frame, label, (cx + radius + 5, cy - radius),
        cv.FONT_HERSHEY_SIMPLEX, 0.6, GREEN, 2)


        h, w = frame.shape[:2]
        cv.line(frame, (w // 2, 0), (w // 2, h), WHITE, 1)


        cv.line(frame, (w // 2, h // 2), (cx, cy), WHITE, 1)
        return frame_bgr


