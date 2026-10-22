"""Line-based messages to/from the microcontroller. Format: docs/serial-protocol.md"""


class SerialLink:
    def __init__(self, port, baud):
        # TODO: open the port with pyserial. Note: opening the port resets most
        # Arduinos, so wait for it to boot before sending.
        raise NotImplementedError

    def send(self, msg_type, *fields):
        """Send one message, e.g. send("VICTIM", 120)."""
        # TODO: format as one line and write it.
        raise NotImplementedError

    def poll(self):
        """Return a list of complete messages received since the last call (never blocks).

        Each message could be a (type, [fields]) tuple. TODO: decide.
        """
        raise NotImplementedError

    def close(self):
        raise NotImplementedError
