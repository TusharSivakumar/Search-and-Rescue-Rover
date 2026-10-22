// Motor driver control.
#pragma once

// Set up the driver pins. Call once from setup().
void motorsBegin();

// Set each wheel's speed. Suggested convention: -255 (full reverse) to
// 255 (full forward), 0 = stop. TODO: decide and document your convention.
void setMotorSpeeds(int left, int right);

// Stop both motors.
void stopMotors();
