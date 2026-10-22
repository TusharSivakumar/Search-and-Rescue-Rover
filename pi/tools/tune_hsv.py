"""Bench tool: find the HSV range of the victim marker.

Idea: show the camera feed (or a saved image) with trackbars for the HSV low/high
values and a live view of the mask, then copy the values into rover/config.py.

Run from the pi/ folder:  python -m tools.tune_hsv
"""


def main():
    # TODO: create a window with cv2.createTrackbar for H/S/V low and high,
    # read frames, threshold with the trackbar values, show frame and mask side by side.
    # Test under different lighting: the range that works at your desk may fail in the arena.
    raise NotImplementedError


if __name__ == "__main__":
    main()
