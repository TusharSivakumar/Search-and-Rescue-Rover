#include <Arduino.h>
#include "config.h"
#include "encoders.h"

// Tick counters are changed inside interrupts, so they must be volatile.
static volatile long leftCount = 0;
static volatile long rightCount = 0;
static Pose pose = {0.0, 0.0, 0.0};

static void onLeftTick() {
  // TODO: increment or decrement leftCount (use channel B for direction).
}

static void onRightTick() {
  // TODO
}

void encodersBegin() {
  // TODO: set pin modes and attach interrupts to onLeftTick / onRightTick.
}

long leftTicks() {
  // TODO: read the volatile counter safely (it can change mid-read).
  return 0;
}

long rightTicks() {
  // TODO
  return 0;
}

void updateOdometry() {
  // TODO: differential-drive odometry.
  //   1. Ticks since last update for each wheel -> distance each wheel moved.
  //   2. From the two distances: how far the robot moved and how much it turned.
  //   3. Update x, y, heading.
  // Work out the geometry on paper first and put the derivation in the build log.
}

Pose currentPose() {
  return pose;
}

void resetPose() {
  // TODO
}
