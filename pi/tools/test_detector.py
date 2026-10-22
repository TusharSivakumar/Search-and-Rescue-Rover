"""Bench tool: run the detector on a folder of saved images and count results.

Collect test images with and without the victim marker (different distances, angles,
lighting), sort them into two folders, and measure:
  - false positives: detections on images WITHOUT the marker
  - false negatives: missed detections on images WITH the marker
These numbers are Phase 1 evidence and the baseline for Phase 2.

Run from the pi/ folder:  python -m tools.test_detector <with_dir> <without_dir>
"""


def main():
    # TODO: load each image, run VictimDetector.detect, tally the four outcomes,
    # print the rates and save annotated copies of the mistakes to look at.
    raise NotImplementedError


if __name__ == "__main__":
    main()
