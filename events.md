
# Events Documentation

## 1. Introduction

This document describes the events used in the Smart Traffic Light System.

The project uses Event-Driven Programming to respond to timer events, pedestrian requests and emergency vehicle detection.

The Python implementation uses a local event queue.

The ESP32 implementation uses event detection and direct event processing.

---

## 2. Event List

| Event | Producer | Description |
|---|---|---|
| SYSTEM_START | Main Application | Initializes the traffic light system |
| TIMER_EXPIRED | Timer | Indicates that the current traffic state duration has ended |
| PEDESTRIAN_REQUEST | Push Button | Indicates that a pedestrian wants to cross |
| EMERGENCY_DETECTED | Serial Monitor / Emergency Input | Indicates an emergency vehicle |
| CROSSING_ACTIVATED | Pedestrian Handler | Activates pedestrian crossing |
| CROSSING_COMPLETED | Pedestrian Handler | Indicates that pedestrian crossing has finished |

---

## 3. Event Descriptions

### SYSTEM_START

**Producer:** Main Application

Triggered when the application starts.

Actions:
- Initialize traffic light states.
- Initialize event processing.
- Activate the initial GREEN state.

### TIMER_EXPIRED

**Producer:** Timer

Triggered when the current traffic light duration expires.

Actions:
- Process the timer event.
- Change the traffic light state.
- Continue the automatic traffic sequence.

Normal sequence:

```text
GREEN → YELLOW → RED → GREEN
```

### PEDESTRIAN_REQUEST

**Producer:** Pedestrian Push Button

Triggered when a pedestrian presses the button.

Actions:
- Detect the button press.
- Generate a pedestrian request.
- Mark the request as pending.
- Wait until the traffic light reaches RED.

### CROSSING_ACTIVATED

**Producer:** Pedestrian Handler

Triggered when the traffic light reaches RED and a pedestrian request is pending.

Actions:
- Activate pedestrian crossing.
- Keep the traffic light RED.
- Start the pedestrian crossing timer.

### CROSSING_COMPLETED

**Producer:** Pedestrian Handler

Triggered when the pedestrian crossing timer expires.

Actions:
- Complete the crossing.
- Clear the crossing state.
- Return the traffic light to GREEN.

### EMERGENCY_DETECTED

**Producer:** Emergency Input

Triggered when an emergency command is received.

In the ESP32 implementation, the emergency command is:

```text
E
```

Actions:
- Detect the emergency command.
- Activate emergency priority.
- Immediately change the traffic light to RED.
- Start the emergency timer.
- Resume normal operation after the emergency period.

---

## 4. Event Processing Examples

### Automatic Traffic Sequence

```text
SYSTEM_START
     |
     v
GREEN
     |
TIMER_EXPIRED
     |
     v
YELLOW
     |
TIMER_EXPIRED
     |
     v
RED
     |
TIMER_EXPIRED
     |
     v
GREEN
```

### Pedestrian Request

```text
BUTTON PRESSED
     |
     v
PEDESTRIAN_REQUEST
     |
     v
REQUEST PENDING
     |
     v
TRAFFIC LIGHT RED
     |
     v
CROSSING_ACTIVATED
     |
     v
WAIT 5 SECONDS
     |
     v
CROSSING_COMPLETED
     |
     v
TRAFFIC LIGHT GREEN
```

### Emergency Detection

```text
SERIAL COMMAND: E
     |
     v
EMERGENCY_DETECTED
     |
     v
EMERGENCY PRIORITY
     |
     v
TRAFFIC LIGHT RED
     |
     v
WAIT 3 SECONDS
     |
     v
EMERGENCY CLEARED
     |
     v
TRAFFIC LIGHT GREEN
```

---

## 5. Event Handling Responsibilities

| Handler / Function | Responsibility |
|---|---|
| Event Queue | Stores events in the Python implementation |
| Event Handlers | Processes events |
| checkButton() | Detects pedestrian button presses |
| pedestrianRequest() | Generates pedestrian requests |
| emergencyDetected() | Activates emergency priority |
| handleTimerEvent() | Processes timer expiration |
| changeLight() | Changes traffic light states |
| setLight() | Controls RGB LED outputs |

---

## 6. Event Logging

The ESP32 Serial Monitor displays event messages.

Example:

```text
[QUEUE] Event added: TIMER_EXPIRED
[HANDLER] Processing TIMER_EXPIRED
[TRAFFIC LIGHT] YELLOW

[QUEUE] Event added: TIMER_EXPIRED
[HANDLER] Processing TIMER_EXPIRED
[TRAFFIC LIGHT] RED

[PEDESTRIAN] Crossing activated
[PEDESTRIAN] Crossing completed

[EVENT] EMERGENCY_DETECTED
[TRAFFIC LIGHT] RED
[EMERGENCY] Priority activated!
```

Note: The ESP32 version currently uses these queue-style log messages for visibility, but does not implement a separate FIFO event queue.

---

## 7. Conclusion

The event system allows the Smart Traffic Light System to react to different situations.

It demonstrates how events can control traffic light states, handle pedestrian requests and prioritize emergency situations.

The project applies Event-Driven Programming concepts in both a Python software application and an ESP32 hardware simulation.
