"""Victim detection with OpenCV color/shape detection."""

from dataclasses import dataclass


@dataclass
class Detection:
    center_x: int      # pixels
    center_y: int      # pixels
    area: float        # pixels^2
    # TODO: anything else? A confidence score, a shape label, a bearing angle?


class VictimDetector:
    def __init__(self, hsv_low, hsv_high, min_area):
        # TODO: store settings.
        raise NotImplementedError

    def detect(self, frame_bgr):
        """Return a Detection for the best candidate in the frame, or None.

        Suggested steps (look each up in the OpenCV docs):
          1. Convert BGR -> HSV
          2. Threshold to a mask with the HSV range
          3. Clean the mask (blur / erode / dilate)
          4. Find contours, drop ones smaller than min_area
          5. Optional: check the shape (aspect ratio, approxPolyDP, circularity)
          6. Pick the best candidate
        """
        raise NotImplementedError

    def draw(self, frame_bgr, detection):
        """Draw the detection on the frame for debugging and demo video."""
        raise NotImplementedError
