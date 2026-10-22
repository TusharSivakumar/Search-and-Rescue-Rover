# Serial protocol (Pi ↔ microcontroller)

Draft — change it as you design the system. Record every change in the build log.

- Physical link: USB serial, 115200 baud
- One message per line, ASCII, ending in `\n`
- Format: `TYPE,field1,field2,...`

## Pi → microcontroller

| Message | Fields | Meaning |
| --- | --- | --- |
| `VICTIM` | TODO (e.g. bearing in the image?) | Camera sees a victim |
| `STOP` | — | Stop motors |
| `RESUME` | — | Resume exploring |
| TODO | | |

## Microcontroller → Pi

| Message | Fields | Meaning |
| --- | --- | --- |
| `POSE` | TODO (x, y, heading? units?) | Odometry estimate |
| `STATE` | TODO | Current avoidance state |
| `ACK` | TODO | Message received |
| TODO | | |

## Open questions

- What happens if a message is corrupted or cut off halfway?
- How often should `POSE` be sent?
- Who decides what the rover does after a victim is found: the Pi or the microcontroller?
