#include <Arduino.h>
#include "config.h"
#include "serial_link.h"

void serialLinkBegin() {
  Serial.begin(SERIAL_BAUD);
}

PiCommand pollPiCommand() {
  // TODO: read available bytes into a buffer without blocking.
  // When a '\n' arrives, parse the line, clear the buffer and return the command.
  // What if the buffer fills up before a newline arrives?
  return PiCommand::None;
}

void sendPose(float x, float y, float heading) {
  // TODO: print one POSE line in the protocol format.
}

void sendState(const char* stateName) {
  // TODO
}
