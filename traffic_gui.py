
import tkinter as tk

import event_handlers

from event_queue import process_events
from event_producers import (
    start_system,
    timer_expired,
    pedestrian_button,
    emergency_detected
)


class TrafficLightGUI:

    GREEN_TIME = 3000
    YELLOW_TIME = 2000
    RED_TIME = 3000

    def __init__(self, root):

        self.root = root
        self.root.title("EDP Smart Traffic Light System")
        self.root.geometry("850x700")
        self.root.configure(bg="#151923")
        self.root.resizable(False, False)

        self.running = False
        self.started = False
        self.timer_id = None

        self.create_interface()
        self.update_interface()

    def create_interface(self):

        title = tk.Label(
            self.root,
            text="SMART TRAFFIC LIGHT SYSTEM",
            font=("Arial", 22, "bold"),
            bg="#151923",
            fg="white"
        )
        title.pack(pady=15)

        subtitle = tk.Label(
            self.root,
            text="AUTOMATIC EVENT-DRIVEN CONTROL",
            font=("Arial", 11),
            bg="#151923",
            fg="#aab3c5"
        )
        subtitle.pack()

        main_frame = tk.Frame(
            self.root,
            bg="#151923"
        )
        main_frame.pack(pady=20)

        self.canvas = tk.Canvas(
            main_frame,
            width=220,
            height=390,
            bg="#151923",
            highlightthickness=0
        )
        self.canvas.grid(row=0, column=0, padx=25)

        control_frame = tk.Frame(
            main_frame,
            bg="#222938",
            padx=20,
            pady=15
        )
        control_frame.grid(row=0, column=1, sticky="n")

        tk.Label(
            control_frame,
            text="CONTROL PANEL",
            font=("Arial", 14, "bold"),
            bg="#222938",
            fg="white"
        ).pack(pady=10)

        self.create_button(
            control_frame,
            "START SYSTEM",
            "#16a34a",
            self.start
        )

        self.pause_button = self.create_button(
            control_frame,
            "PAUSE SYSTEM",
            "#64748b",
            self.pause_resume
        )

        self.create_button(
            control_frame,
            "PEDESTRIAN REQUEST",
            "#d97706",
            self.pedestrian
        )

        self.create_button(
            control_frame,
            "EMERGENCY VEHICLE",
            "#dc2626",
            self.emergency
        )

        self.status_label = tk.Label(
            self.root,
            text="SYSTEM OFF",
            font=("Arial", 14, "bold"),
            bg="#151923",
            fg="white"
        )
        self.status_label.pack(pady=5)

        self.timer_label = tk.Label(
            self.root,
            text="Automatic timer: stopped",
            font=("Arial", 10),
            bg="#151923",
            fg="#aab3c5"
        )
        self.timer_label.pack(pady=3)

        tk.Label(
            self.root,
            text="EVENT MONITOR",
            font=("Arial", 12, "bold"),
            bg="#151923",
            fg="white"
        ).pack(pady=5)

        self.log = tk.Text(
            self.root,
            height=9,
            width=90,
            bg="#0d1117",
            fg="#00ff99",
            font=("Consolas", 9),
            state="disabled"
        )
        self.log.pack(pady=10)

        self.draw_traffic_light()

    def create_button(self, parent, text, color, command):

        button = tk.Button(
            parent,
            text=text,
            font=("Arial", 10, "bold"),
            bg=color,
            fg="white",
            activebackground=color,
            activeforeground="white",
            width=23,
            height=2,
            relief="flat",
            command=command
        )

        button.pack(pady=8)

        return button

    def log_event(self, message):

        self.log.configure(state="normal")
        self.log.insert("end", message + "\n")
        self.log.see("end")
        self.log.configure(state="disabled")

    def add_event(self, producer):

        producer()

        processed = process_events(
            event_handlers.handle_event
        )

        for event, messages in processed:

            self.log_event(
                f"[QUEUE] {event['type']}"
            )

            for message in messages:
                self.log_event(f"[EVENT] {message}")

        self.draw_traffic_light()
        self.update_status()

    def start(self):

        if self.started:
            return

        self.started = True
        self.running = True

        self.add_event(start_system)

        self.log_event("Automatic traffic control started")

        self.schedule_next_timer()

    def schedule_next_timer(self):

        if not self.running:
            return

        state = event_handlers.traffic_light.get_state()

        if (
            event_handlers.emergency_active
            or event_handlers.pedestrian_crossing
        ):
            delay = self.RED_TIME

        elif state == "YELLOW":
            delay = self.YELLOW_TIME

        elif state == "RED":
            delay = self.RED_TIME

        else:
            delay = self.GREEN_TIME

        self.timer_label.config(
            text=f"Next automatic event in {delay // 1000} seconds"
        )

        self.timer_id = self.root.after(
            delay,
            self.automatic_tick
        )

    def automatic_tick(self):

        self.timer_id = None

        if not self.running:
            return

        self.log_event("Automatic timer expired")

        self.add_event(timer_expired)

        self.schedule_next_timer()

    def pause_resume(self):

        if not self.started:
            return

        if self.running:

            self.running = False

            if self.timer_id is not None:
                self.root.after_cancel(self.timer_id)
                self.timer_id = None

            self.pause_button.config(text="RESUME SYSTEM")

            self.timer_label.config(text="Automatic timer: paused")

            self.log_event("System paused")

        else:

            self.running = True

            self.pause_button.config(text="PAUSE SYSTEM")

            self.log_event("System resumed")

            self.schedule_next_timer()

    def pedestrian(self):

        if self.started:
            self.add_event(pedestrian_button)

    def emergency(self):

        if self.started:
            self.add_event(emergency_detected)

    def draw_traffic_light(self):

        self.canvas.delete("all")

        self.canvas.create_rectangle(
            45, 20, 175, 350,
            fill="#292f3b",
            outline="#596273",
            width=3
        )

        state = event_handlers.traffic_light.get_state()

        lights = [
            ("RED", 85, "#ff3030", "#641919"),
            ("YELLOW", 190, "#ffcc00", "#665000"),
            ("GREEN", 295, "#00e676", "#075c36")
        ]

        for name, y, active_color, inactive_color in lights:

            color = (
                active_color
                if state == name
                else inactive_color
            )

            self.canvas.create_oval(
                75, y - 35,
                145, y + 35,
                fill=color,
                outline="#111827",
                width=3
            )

        self.canvas.create_rectangle(
            100, 350, 120, 385,
            fill="#596273",
            outline=""
        )

    def update_status(self):

        if not self.started:
            message = "SYSTEM OFF"

        elif event_handlers.emergency_active:
            message = "EMERGENCY PRIORITY - RED"

        elif event_handlers.pedestrian_crossing:
            message = "PEDESTRIAN CROSSING ACTIVE"

        elif event_handlers.pedestrian_waiting:
            message = "PEDESTRIAN WAITING"

        else:
            message = (
                "TRAFFIC LIGHT: "
                + event_handlers.traffic_light.get_state()
            )

        self.status_label.config(text=message)

    def update_interface(self):

        self.draw_traffic_light()
        self.update_status()

        self.root.after(250, self.update_interface)


if __name__ == "__main__":

    root = tk.Tk()
    app = TrafficLightGUI(root)
    root.mainloop()
