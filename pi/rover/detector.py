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
        """Draw the detection on the frame for debugging and demo video."""
        raise NotImplementedError
