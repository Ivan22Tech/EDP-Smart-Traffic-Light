
# System Architecture

## 1. Overview

The Smart Traffic Light System follows an Event-Driven Programming (EDP) architecture.

The application reacts to events instead of relying only on sequential execution.

The project has two implementations:

- Python software implementation.
- ESP32 hardware simulation.

Both implementations demonstrate automatic traffic control, pedestrian requests and emergency handling.

---

## 2. Python Architecture

The Python implementation is divided into separate modules.

### Event Producers

Event producers generate events when something happens.

Examples:

- System startup.
- Timer expiration.
- Pedestrian button request.
- Emergency vehicle detection.

### Event Queue

The event queue stores events until they are processed.

It provides a separation between event production and event handling.

### Event Handlers

Event handlers process events and execute the corresponding actions.

Examples:

- Changing traffic light states.
- Activating pedestrian crossing.
- Handling emergency priority.
- Updating the graphical interface.

### Python Architecture Diagram

```text
+---------------------------+
|       Event Producers     |
|                           |
| - Timer                   |
| - Pedestrian Request      |
| - Emergency Detection     |
| - System Startup          |
+-------------+-------------+
              |
              v
+---------------------------+
|        Event Queue        |
|                           |
|     Local Event Queue     |
+-------------+-------------+
              |
              v
+---------------------------+
|       Event Handlers      |
|                           |
| - Timer Handler           |
| - Pedestrian Handler      |
| - Emergency Handler       |
+-------------+-------------+
              |
              v
+---------------------------+
|      Traffic Light        |
|                           |
|   RED / YELLOW / GREEN    |
+-------------+-------------+
              |
              v
+---------------------------+
|       Tkinter GUI         |
|                           |
|   Visual State Updates    |
+---------------------------+
```

---

## 3. ESP32 Hardware Architecture

The ESP32 implementation uses Arduino C++.

It consists of:

### Event Producers

- Timer expiration detection.
- Pedestrian button detection.
- Emergency command detection through Serial Monitor.

### Event Processing

The ESP32 checks incoming events and processes them using event-handling functions.

The current implementation processes events directly in the main loop rather than using a separate FIFO event queue.

### Event Handlers

The main event-handling function processes timer events.

Other functions handle pedestrian requests and emergency detection.

### Hardware Outputs

The RGB LED represents the traffic light.

The pedestrian push button generates pedestrian request events.

### ESP32 Architecture Diagram

```text
+---------------------------+
|       Event Producers     |
|                           |
| - Timer Detection         |
| - Pedestrian Button       |
| - Serial Emergency Input  |
+-------------+-------------+
              |
              v
+---------------------------+
|    Event Processing      |
|                           |
| - checkButton()           |
| - pedestrianRequest()     |
| - emergencyDetected()     |
+-------------+-------------+
              |
              v
+---------------------------+
|       Event Handlers      |
|                           |
| - handleTimerEvent()      |
| - changeLight()           |
+-------------+-------------+
              |
              v
+---------------------------+
|       ESP32 Outputs       |
|                           |
| - RGB LED                 |
| - Serial Monitor          |
+---------------------------+
```

---

## 4. Hardware Configuration

| Component | GPIO |
|---|---|
| Red LED | 25 |
| Green LED | 26 |
| Blue LED | 27 |
| Pedestrian Button | 14 |
| RGB Common Cathode | GND |

Each RGB color connection uses a 220Ω resistor.

The RGB LED operates in common-cathode mode:

- LOW = OFF
- HIGH = ON

The pedestrian button uses INPUT_PULLUP.

---

## 5. Traffic Light State Machine

The normal traffic sequence is:

```text
GREEN
  |
  | TIMER_EXPIRED
  v
YELLOW
  |
  | TIMER_EXPIRED
  v
RED
  |
  | TIMER_EXPIRED
  v
GREEN
```

### State Durations

| State | Duration |
|---|---:|
| GREEN | 3 seconds |
| YELLOW | 2 seconds |
| RED | 3 seconds |
| Pedestrian Crossing | 5 seconds |

---

## 6. Pedestrian Event Flow

1. The pedestrian presses the push button.
2. The system generates PEDESTRIAN_REQUEST.
3. The request is marked as pending.
4. The current traffic sequence continues.
5. The traffic light reaches RED.
6. Pedestrian crossing is activated.
7. The system waits five seconds.
8. Crossing is completed.
9. GREEN is activated again.

---

## 7. Emergency Event Flow

1. The user sends the E command through Serial Monitor.
2. The system detects EMERGENCY_DETECTED.
3. Emergency priority is activated.
4. The traffic light immediately changes to RED.
5. The emergency timer starts.
6. After three seconds, emergency priority is cleared.
7. GREEN is activated again.

---

## 8. Event-Driven Programming Principles

The project demonstrates:

- Event producers generating events.
- Event queues in the Python implementation.
- Event handling.
- Separation of application components.
- State management.
- Timer-based events.
- User-generated events.
- Priority-based emergency handling.

The ESP32 version is a hardware-oriented implementation of the same traffic control concept.
