"""Pi Camera capture."""


class Camera:
    def __init__(self, width, height, framerate):
        # TODO: open the camera (picamera2 on current Raspberry Pi OS).
        raise NotImplementedError

    def read(self):
        """Return the latest frame as a BGR numpy array (what OpenCV expects), or None."""
        # TODO: picamera2 returns RGB by default; convert or configure for BGR.
        raise NotImplementedError

    def close(self):
        # TODO
        raise NotImplementedError
