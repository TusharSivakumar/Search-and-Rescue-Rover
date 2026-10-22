// Wheel encoders and odometry (dead reckoning).
#pragma once

struct Pose {
  float x;        // m, TODO: decide your frame (where is 0,0? which way is +x?)
  float y;        // m
  float heading;  // rad
};

// Set up encoder pins and interrupts. Call once from setup().
void encodersBegin();

// Ticks counted since start (signed: forward positive).
long leftTicks();
long rightTicks();

// Update the pose estimate from the ticks counted since the last call.
// Call regularly from loop().
void updateOdometry();

Pose currentPose();
void resetPose();
