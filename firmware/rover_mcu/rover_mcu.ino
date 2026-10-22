// Search and Rescue Rover — microcontroller firmware (Phase 1).
// Open this folder in the Arduino IDE; the .h/.cpp files compile with the sketch.

#include "config.h"
#include "motors.h"
#include "ultrasonic.h"
#include "encoders.h"
#include "serial_link.h"

// Avoidance state machine. TODO: add, remove or rename states as your design needs.
enum class State {
  Explore,      // drive forward
  BackOff,      // obstacle ahead: reverse
  Turn,         // turn away from the obstacle
  VictimFound,  // the Pi reported a victim
  Stopped,
};

State state = State::Explore;
unsigned long stateStartMs = 0;   // when the current state began (for timed states)
unsigned long lastSensorMs = 0;
unsigned long lastPoseMs = 0;
float distances[NUM_ULTRASONIC];

void enterState(State next) {
  // TODO: record the new state and its start time; tell the Pi (sendState).
}

void setup() {
  serialLinkBegin();
  motorsBegin();
  ultrasonicBegin();
  encodersBegin();
  // TODO: anything else to do before the rover moves? A start button or delay?
  enterState(State::Explore);
}

void loop() {
  unsigned long now = millis();

  // 1. Messages from the Pi
  PiCommand cmd = pollPiCommand();
  // TODO: react to cmd (e.g. Victim -> VictimFound, Stop -> Stopped).

  // 2. Sensors, at a fixed period
  if (now - lastSensorMs >= SENSOR_PERIOD_MS) {
    lastSensorMs = now;
    readAllDistances(distances);
  }

  // 3. Odometry and pose reports
  updateOdometry();
  if (now - lastPoseMs >= POSE_PERIOD_MS) {
    lastPoseMs = now;
    // TODO: sendPose(...)
  }

  // 4. Behavior
  switch (state) {
    case State::Explore:
      // TODO: drive forward; if an obstacle is closer than OBSTACLE_DISTANCE_CM -> BackOff.
      break;
    case State::BackOff:
      // TODO: reverse for a while, then -> Turn.
      break;
    case State::Turn:
      // TODO: turn away from the closer side, then -> Explore.
      break;
    case State::VictimFound:
      // TODO: stop and report the pose where the victim was seen.
      break;
    case State::Stopped:
      // TODO
      break;
  }

  // Keep loop() fast: no delay() calls, so serial and sensors stay responsive.
}
