"""Bench tool: find the HSV range of the victim marker.

Idea: show the camera feed (or a saved image) with trackbars for the HSV low/high
values and a live view of the mask, then copy the values into rover/config.py.

Run from the pi/ folder:  python -m tools.tune_hsv
"""
import cv2 as cv
import numpy as np


def main():
    # TODO: create a window with cv2.createTrackbar for H/S/V low and high,
    def on_change(value):
        pass
    WINDOW = "TrackBar"
    cv.namedWindow(WINDOW)
    cv.createTrackbar("H Low", WINDOW, 0, 179, on_change)
    cv.createTrackbar("H High", WINDOW, 179, 179, on_change)
    cv.createTrackbar("S Low", WINDOW, 0, 255, on_change)
    cv.createTrackbar("S High", WINDOW, 255, 255, on_change)
    cv.createTrackbar("V Low", WINDOW, 0, 255, on_change)
    cv.createTrackbar("V High", WINDOW, 255, 255, on_change)

    low = (cv.getTrackbarPos("H Low", WINDOW), cv.getTrackbarPos("S Low", WINDOW), cv.getTrackbarPos("V Low", WINDOW))
    high = (cv.getTrackbarPos("H High", WINDOW), cv.getTrackbarPos("S High", WINDOW), cv.getTrackbarPos("V High", WINDOW))
    camera = cv.VideoCapture(0)
    while True:
        isTrue, frame = camera.read()

        if isTrue:
            low = (cv.getTrackbarPos("H Low", WINDOW), cv.getTrackbarPos("S Low", WINDOW), cv.getTrackbarPos("V Low", WINDOW))
            high = (cv.getTrackbarPos("H High", WINDOW), cv.getTrackbarPos("S High", WINDOW), cv.getTrackbarPos("V High", WINDOW))
            hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
            mask = cv.inRange(hsv, np.array(low), np.array(high))
            mask_bgr = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
            cv.imshow("Frame over Mask", np.hstack([frame, mask_bgr]))
            key = cv.waitKey(1) & 0xFF
            if key == ord("p"):
                print(f"VICTIM_HSV_LOW = {low}")
                print(f"VICTIM_HSV_HIGH = {high}")
            elif key == ord('q'):
                break
        else:
            break
    cv.destroyAllWindows()

    # read frames, threshold with the trackbar values, show frame and mask side by side.
    # Test under different lighting: the range that works at your desk may fail in the arena.
    


if __name__ == "__main__":
    main()
