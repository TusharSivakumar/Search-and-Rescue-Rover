"""Settings for the Pi side. All values are placeholders to set from testing."""

# Camera
FRAME_WIDTH = 640          # TODO: smaller frames are faster; how small still works?
FRAME_HEIGHT = 480
FRAMERATE = 30

# Detection (HSV color range of the victim marker; tune with tools/tune_hsv.py)
VICTIM_HSV_LOW = (0, 0, 0)       # TODO
VICTIM_HSV_HIGH = (0, 0, 0)      # TODO
MIN_BLOB_AREA_PX = 0             # TODO: ignore blobs smaller than this
FRAMES_TO_CONFIRM = 0            # TODO: detections in a row before reporting (cuts false positives)

# Serial link to the microcontroller
SERIAL_PORT = "/dev/ttyUSB0"     # TODO: check with `ls /dev/tty*` (may be /dev/ttyACM0)
SERIAL_BAUD = 115200
