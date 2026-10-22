// Line-based messages to/from the Pi. Format: docs/serial-protocol.md
#pragma once

enum class PiCommand {
  None,
  Victim,
  Stop,
  Resume,
  // TODO: add commands as the protocol grows
};

// Call once from setup().
void serialLinkBegin();

// Check for a complete line from the Pi without blocking.
// Returns PiCommand::None if no full message has arrived yet.
PiCommand pollPiCommand();

// Send the current pose / state to the Pi.
void sendPose(float x, float y, float heading);
void sendState(const char* stateName);
