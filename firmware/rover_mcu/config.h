// Pins, thresholds and timing. Every value here is a placeholder:
// set it from your wiring and measurements, and note changes in the build log.
#pragma once

// ---- Motor driver ----------------------------------------------------------
// TODO: match your driver. L298N and TB6612FNG both use two direction pins
// and one PWM (speed) pin per motor; TB6612FNG also has a STBY pin.
const int LEFT_IN1 = -1;
const int LEFT_IN2 = -1;
const int LEFT_PWM = -1;
const int RIGHT_IN1 = -1;
const int RIGHT_IN2 = -1;
const int RIGHT_PWM = -1;

// ---- Ultrasonic sensors (HC-SR04) ------------------------------------------
// TODO: one trig/echo pair per sensor. On an ESP32 the echo pin needs a
// voltage divider (5 V -> 3.3 V).
const int NUM_ULTRASONIC = 3;
const int US_TRIG[NUM_ULTRASONIC] = {-1, -1, -1};   // left, center, right?
const int US_ECHO[NUM_ULTRASONIC] = {-1, -1, -1};

// ---- Wheel encoders ---------------------------------------------------------
// TODO: interrupt-capable pins for the encoder A channels (B for direction).
const int LEFT_ENC_A = -1;
const int LEFT_ENC_B = -1;
const int RIGHT_ENC_A = -1;
const int RIGHT_ENC_B = -1;

// ---- Robot geometry (measure these) -----------------------------------------
const float WHEEL_DIAMETER_M = 0.0;   // TODO
const float WHEEL_BASE_M = 0.0;       // TODO: distance between wheel centers
const float TICKS_PER_REV = 0.0;      // TODO: encoder ticks per wheel revolution

// ---- Behavior thresholds -----------------------------------------------------
const float OBSTACLE_DISTANCE_CM = 0.0;   // TODO: how close counts as "blocked"?
const int CRUISE_SPEED = 0;               // TODO: PWM value (0-255 on most boards)
const int TURN_SPEED = 0;                 // TODO

// ---- Timing -----------------------------------------------------------------
const unsigned long SERIAL_BAUD = 115200;
const unsigned long SENSOR_PERIOD_MS = 0;   // TODO: how often to read sensors
const unsigned long POSE_PERIOD_MS = 0;     // TODO: how often to send POSE to the Pi
