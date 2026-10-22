"""Pi main loop: camera -> detector -> report to microcontroller.

Run from the pi/ folder:  python -m rover.main
"""

from rover import config
from rover.camera import Camera
from rover.detector import VictimDetector
from rover.serial_link import SerialLink


def main():
    camera = Camera(config.FRAME_WIDTH, config.FRAME_HEIGHT, config.FRAMERATE)
    detector = VictimDetector(config.VICTIM_HSV_LOW, config.VICTIM_HSV_HIGH, config.MIN_BLOB_AREA_PX)
    link = SerialLink(config.SERIAL_PORT, config.SERIAL_BAUD)

    try:
        while True:
            # TODO:
            #   1. Read a frame
            #   2. Run the detector
            #   3. Only report after FRAMES_TO_CONFIRM detections in a row
            #   4. Send VICTIM to the microcontroller (once, not every frame)
            #   5. Read messages from the microcontroller (POSE, STATE) and log them
            #   6. Optional: save annotated frames for the demo video
            pass
    except KeyboardInterrupt:
        pass
    finally:
        # TODO: tell the microcontroller to stop, then close everything.
        pass


if __name__ == "__main__":
    main()
