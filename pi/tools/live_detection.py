"""Bench tool: run the detector live on the webcam (AI-written example).

Run from the pi/ folder:  python -m tools.live_detection
Press q to quit.
"""
import cv2 as cv

from rover import config
from rover.detector import VictimDetector


def main():
    detector = VictimDetector(config.VICTIM_HSV_LOW, config.VICTIM_HSV_HIGH,
                              config.MIN_BLOB_AREA_PX)
    camera = cv.VideoCapture(0)
    if not camera.isOpened():
        print("Could not open the camera")
        return

    while True:
        ok, frame = camera.read()
        if not ok:
            break
        detection = detector.detect(frame)
        print(detection)
        cv.imshow("Detector", detector.draw(frame, detection))
        if cv.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
