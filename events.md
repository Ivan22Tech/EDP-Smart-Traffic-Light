# Events Documentation

This document describes all events used in the
Smart Traffic Light System.

| Event | Producer | Handler Action |
|---|---|---|
| SYSTEM_START | System | Starts traffic light |
| TIMER_EXPIRED | Timer | Changes light state |
| PEDESTRIAN_REQUEST | Pedestrian Button | Registers crossing request |
| EMERGENCY_DETECTED | Emergency Sensor | Activates emergency priority |

## Event Description

### 1. SYSTEM_START
Generated when the application starts.

### 2. TIMER_EXPIRED
Generated when the traffic light timer expires.

### 3. PEDESTRIAN_REQUEST
Generated when a pedestrian presses the crossing button.

### 4. EMERGENCY_DETECTED
Generated when an emergency vehicle is detected.
