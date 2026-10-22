# Search and Rescue Rover

A small rover that explores a space, avoids obstacles, and finds and reports a "victim."

- **Raspberry Pi + Pi Camera:** vision (OpenCV color/shape detection), high-level decisions
- **Arduino / ESP32:** motors, ultrasonic sensors, wheel encoders, reactive avoidance
- **Link:** the Pi sends messages (e.g. "victim found") to the microcontroller over USB serial;
  position comes from wheel odometry

## Status

Phase 1 skeleton. Every file holds structure, function signatures and TODOs only;
the logic is written by me. The initial scaffold was generated with an AI assistant
(see `docs/build-log.md`, entry 0).

## Layout

```
firmware/rover_mcu/     Arduino/ESP32 sketch (open this folder in the Arduino IDE)
  rover_mcu.ino           setup(), loop(), avoidance state machine
  config.h                pins, thresholds, timing
  motors.*                motor driver (L298N / TB6612FNG / DRV8833)
  ultrasonic.*            HC-SR04 sensors
  encoders.*              wheel encoder ticks and odometry
  serial_link.*           messages to/from the Pi
pi/                     Raspberry Pi code (Python 3)
  rover/config.py         camera, detection and serial settings
  rover/camera.py         Pi Camera capture
  rover/detector.py       victim detection (OpenCV)
  rover/serial_link.py    messages to/from the microcontroller
  rover/main.py           main loop
  tools/                  bench tools: HSV tuning, detector test on saved images
docs/
  build-log.md            dated build log (becomes the video script)
  parts-list.md           parts, prices, where bought
  serial-protocol.md      message format between Pi and microcontroller
```

## Phase 1 plan

1. CAD and print the chassis around the motors and battery (budget 2–3 prints)
2. Motor driver wired, basic drive on a test frame — `motors.*`
3. Ultrasonic sensors and reactive avoidance (back off and turn) — `ultrasonic.*`, `rover_mcu.ino`
4. OpenCV detection on its own (`pi/tools/`), then integrated — `detector.py`, `main.py`
5. Full demo run and documentation
