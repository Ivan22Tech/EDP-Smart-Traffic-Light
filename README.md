
# 🚦 Smart Traffic Light System

## Event-Driven Programming (EDP) Project

**Project:** Event-Driven Smart Traffic Light System  
**Developer:** Ivan Sadek  
**Technology:** Python, Arduino C++, ESP32, Wokwi

---

## 1. Project Description

The Smart Traffic Light System is an Event-Driven Programming project that simulates an intelligent traffic intersection.

The system uses events to control traffic lights automatically and respond to external requests, including pedestrian crossings and emergency vehicles.

The project has two implementations:

1. **Python Application:** A graphical traffic light simulator using Tkinter and an event-driven architecture.
2. **ESP32 Hardware Simulation:** An Arduino-based implementation using an ESP32, RGB LED and pedestrian push button, simulated with Wokwi.

---

## 2. Main Features

- Automatic traffic light sequencing.
- Red, yellow and green traffic states.
- Pedestrian crossing requests.
- Emergency vehicle priority.
- Event producers and event handlers.
- Local event queue in the Python implementation.
- RGB LED hardware simulation.
- Serial Monitor event logging.
- Automatic timer-based transitions.

---

## 3. Project Structure

```text
EDP-Smart-Traffic-Light/
│
├── hardware/
│   ├── sketch.ino
│   └── diagram.json
│
├── main.py
├── traffic_gui.py
├── traffic_light.py
├── event_queue.py
├── event_handlers.py
├── event_producers.py
│
├── events.md
├── architecture.md
└── README.md
```

The `hardware` folder contains the ESP32 Arduino implementation and the Wokwi circuit diagram.

---

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main application |
| Tkinter | Graphical user interface |
| Arduino C++ | ESP32 implementation |
| ESP32 | Hardware controller |
| Wokwi | Hardware simulation |
| GitHub | Source code and documentation |

---

## 5. How to Run the Python Application

### Requirements

- Python 3 installed.
- Windows, Linux or macOS.

### Installation

Clone the repository:

```bash
git clone https://github.com/Ivan22Tech/EDP-Smart-Traffic-Light.git
```

Open the project directory:

```bash
cd EDP-Smart-Traffic-Light
```

Run the application:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

---

## 6. How to Run the ESP32 Version

The hardware implementation is designed for the Wokwi ESP32 simulator.

### Steps

1. Open the ESP32 project in Wokwi.
2. Open `sketch.ino`.
3. Upload or paste the Arduino code.
4. Check the RGB LED and push button connections.
5. Start the simulation.
6. Monitor events through the Serial Monitor.

### Hardware Components

- ESP32 development board.
- One RGB LED (common cathode).
- Three 220Ω resistors.
- One push button.

### GPIO Configuration

| Component | ESP32 GPIO |
|---|---|
| RGB Red | GPIO 25 |
| RGB Green | GPIO 26 |
| RGB Blue | GPIO 27 |
| Pedestrian Button | GPIO 14 |
| RGB Common Cathode | GND |

The pedestrian button uses the ESP32 internal pull-up resistor (`INPUT_PULLUP`).

---

## 7. Event-Driven Behavior

### Automatic Traffic Control

The system automatically changes traffic light states using timer events.

```text
GREEN → YELLOW → RED → GREEN
```

### Pedestrian Request

When the pedestrian button is pressed:

1. A pedestrian request is detected.
2. The request is stored as pending.
3. The system completes its current traffic sequence.
4. The traffic light changes to RED.
5. Pedestrian crossing is activated.
6. After five seconds, crossing is completed and GREEN returns.

### Emergency Vehicle

The ESP32 implementation accepts the `E` command through the Serial Monitor.

When an emergency is detected:

1. The emergency event is triggered.
2. Emergency priority is activated.
3. The traffic light immediately changes to RED.
4. After the emergency timer, normal operation resumes.

---

## 8. Testing Results

The following features were tested in the Wokwi simulation:

| Test | Result |
|---|---|
| ESP32 initialization | Successful |
| RGB LED operation | Successful |
| Automatic traffic sequence | Successful |
| Pedestrian button detection | Successful |
| Pedestrian crossing activation | Successful |
| Pedestrian crossing completion | Successful |
| Emergency detection | Successful |
| Emergency priority | Successful |

---

## 9. Event-Driven Architecture

The Python implementation uses a local event queue to manage events.

The ESP32 implementation uses event-producing functions, timer-based event handling and direct event processing.

See:

- [Architecture](architecture.md)
- [Events Documentation](events.md)

---

## 10. Project Objective

The main objective is to demonstrate the principles of Event-Driven Programming through a practical traffic control application.

The project demonstrates how software and hardware can respond to events, process requests, manage different traffic states and prioritize emergency situations.

---

**Author:** Ivan Sadek  
**Project:** Event-Driven Smart Traffic Light System
