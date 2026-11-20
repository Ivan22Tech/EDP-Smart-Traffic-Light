# System Architecture

## 1. Project Overview

The Smart Traffic Light System is an Event-Driven
Programming application that simulates a traffic
intersection.

## 2. Event Producers

The system has four event producers:

- System startup
- Traffic timer
- Pedestrian button
- Emergency sensor

## 3. Event Queue

A local FIFO (First In, First Out) event queue
implemented using Python's queue.Queue.

All events are stored before being processed.

## 4. Event Handlers

The event handler processes incoming events.

It can:

- Start the traffic lights.
- Change traffic light states.
- Register pedestrian requests.
- Activate emergency priority.

## 5. Event Flow

Event Producer
      |
      v
   Event Queue
      |
      v
  Event Handler
      |
      v
 Traffic Light

## 6. Future Hardware Integration

The application can be extended using:

- ESP32 microcontroller
- Red LED
- Yellow LED
- Green LED
- Pedestrian push button
- Emergency detection sensor
