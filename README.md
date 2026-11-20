
# Smart Traffic Light System

## Event-Driven Programming (EDP) Project

### 1. Project Description

The Smart Traffic Light System is a Python application that
simulates an intelligent traffic intersection using
Event-Driven Programming.

The application includes a graphical interface built with
Tkinter and a local event queue.

### 2. Features

- Automatic traffic light switching.
- GREEN, YELLOW and RED traffic light states.
- Pedestrian crossing requests.
- Emergency vehicle priority.
- Automatic timer events.
- Pause and resume functionality.
- Live event monitoring.
- Local event queue.

### 3. Technologies Used

- Python 3.13
- Tkinter
- queue.Queue
- Visual Studio Code
- GitHub

### 4. Project Structure

```text
EDP-Smart-Traffic-Light/
│
├── main.py
├── traffic_gui.py
├── traffic_light.py
├── event_queue.py
├── event_producers.py
├── event_handlers.py
│
├── events.md
├── architecture.md
├── README.md
│
└── .gitignore
```

### 5. Architecture

The system follows the Event-Driven Programming model.

**Event Producers:**
Generate events from buttons and automatic timers.

**Event Queue:**
Stores events locally using Python queue.Queue.

**Event Handlers:**
Process events and update the traffic light state.

**GUI:**
Displays the traffic light and application status.

### 6. Installation Requirements

- Windows, Linux or macOS.
- Python 3.13 or compatible Python 3 version.
- Git.

Tkinter is included with standard Windows Python installations.

### 7. How to Run

Clone the repository:

```bash
git clone https://github.com/Ivan22Tech/EDP-Smart-Traffic-Light.git
```

Open the project directory:

```bash
cd EDP-Smart-Traffic-Light
```

Run the application on Windows:

```bash
py -3.13 main.py
```

On systems where Python is available as python3:

```bash
python3 main.py
```

### 8. How to Use

1. Click START SYSTEM.
2. The traffic light starts with GREEN.
3. The lights change automatically:
   GREEN → YELLOW → RED → GREEN.
4. Use PAUSE SYSTEM to pause automatic switching.
5. Use RESUME SYSTEM to continue.
6. Use PEDESTRIAN REQUEST to request crossing.
7. Use EMERGENCY VEHICLE to activate emergency priority.
8. Monitor events in the Event Monitor panel.

### 9. Traffic Light Timing

| Light | Duration |
|-------|----------|
| GREEN | 3 seconds |
| YELLOW | 2 seconds |
| RED | 3 seconds |

### 10. Documentation

- events.md: Complete event descriptions.
- architecture.md: System architecture and event flow.

### 11. Author

Ivan Sadek

### 12. Project Purpose

This project demonstrates the principles of
Event-Driven Programming using a practical traffic
intersection simulation.
