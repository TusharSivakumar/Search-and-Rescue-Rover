#include <Arduino.h>
#include "config.h"
#include "ultrasonic.h"

void ultrasonicBegin() {
  // TODO: trig pins as outputs, echo pins as inputs.
}

float readDistanceCm(int index) {
  // TODO: send the trigger pulse, time the echo pulse, convert time to distance.
  // Look up the HC-SR04 datasheet for the pulse timing and the speed of sound.
  // Use a timeout so a missing echo can't freeze the loop.
  return -1.0;
}

void readAllDistances(float out[]) {
  // TODO: read each sensor in turn, with a short gap between them.
}
