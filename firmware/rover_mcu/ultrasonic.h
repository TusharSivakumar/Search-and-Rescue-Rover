// HC-SR04 ultrasonic distance sensors.
#pragma once

// Set up trig/echo pins. Call once from setup().
void ultrasonicBegin();

// Distance from sensor `index` in cm, or a negative value if there was no echo.
// TODO: decide what "no echo" returns and how callers handle it.
float readDistanceCm(int index);

// Read every sensor into `out` (length NUM_ULTRASONIC).
// Fire them one at a time so they don't hear each other's pings.
void readAllDistances(float out[]);
