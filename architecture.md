
# System Architecture

## EDP Smart Traffic Light System

## 1. Overview

The application simulates a smart traffic intersection using
Event-Driven Programming.

It uses Python, Tkinter and a local event queue.

The system supports:
- Automatic traffic light switching.
- Pedestrian crossing requests.
- Emergency vehicle priority.
- Graphical monitoring and control.

## 2. Architecture Components

### A. Event Producers

Event producers generate events when an action occurs.

Examples:

- Start System button.
- Automatic timer.
- Pedestrian Request button.
- Emergency Vehicle button.

Implemented in:

event_producers.py

### B. Event Queue

The application uses Python queue.Queue to store events
until they are processed.

Implemented in:

event_queue.py

The queue operates locally without requiring a network.

### C. Event Handlers

Event handlers receive events and decide what action
the application should perform.

Examples:

- Change GREEN to YELLOW.
- Change YELLOW to RED.
- Activate pedestrian crossing.
- Activate emergency priority.

Implemented in:

event_handlers.py

### D. Traffic Light Controller

The TrafficLight class stores and changes the current
traffic light state.

Possible states:

- OFF
- GREEN
- YELLOW
- RED

Implemented in:

traffic_light.py

### E. Graphical User Interface

Tkinter provides the visual interface.

It displays:

- Traffic light colors.
- System status.
- Pedestrian status.
- Emergency status.
- Event monitor.

Implemented in:

traffic_gui.py

### F. Main Application

main.py launches the graphical application.

## 3. Architecture Diagram

```text
             EVENT PRODUCERS
                    |
          +---------+---------+
          |         |         |
        START     TIMER    PEDESTRIAN
          |         |       EMERGENCY
          +---------+---------+
                    |
                    v
              EVENT QUEUE
              (queue.Queue)
                    |
                    v
              EVENT HANDLERS
                    |
                    v
             TRAFFIC LIGHT
               CONTROLLER
                    |
                    v
              GUI DISPLAY
                (Tkinter)
```

## 4. Automatic Timer

The application uses Tkinter's after() function
to schedule automatic timer events.

The timer generates TIMER_EXPIRED events without
blocking the graphical interface.

Traffic light timing:

- GREEN: 3 seconds
- YELLOW: 2 seconds
- RED: 3 seconds

The sequence repeats automatically.

## 5. Pedestrian Event Flow

1. A pedestrian presses the request button.
2. PEDESTRIAN_REQUEST is generated.
3. The event enters the local queue.
4. The handler records the request.
5. When the traffic light reaches RED, crossing becomes active.
6. The next timer event finishes the crossing.

## 6. Emergency Event Flow

1. An emergency vehicle is detected through the GUI button.
2. EMERGENCY_DETECTED is generated.
3. The event enters the local queue.
4. The handler activates emergency priority.
5. The traffic light changes immediately to RED.
6. The next timer event clears emergency priority.

## 7. Technologies

- Python 3.13
- Tkinter
- Python queue.Queue
- Event-Driven Programming
- Visual Studio Code
- Git and GitHub

## 8. Conclusion

The project demonstrates Event-Driven Programming through
event producers, a local event queue and event handlers.

It combines automatic scheduling with graphical interaction
to simulate a smart traffic light system.
