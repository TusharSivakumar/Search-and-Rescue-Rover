#include <Arduino.h>
#include "config.h"
#include "motors.h"

void motorsBegin() {
  // TODO: set the direction and PWM pins as outputs; make sure motors start stopped.
}

void setMotorSpeeds(int left, int right) {
  // TODO: for each motor, pick the direction pins from the sign and write
  // the PWM from the magnitude. Clamp to the valid range.
  // Bench test first: does positive spin each wheel forward? (Swap wires or flip in code.)
}

void stopMotors() {
  // TODO
}
