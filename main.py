
import tkinter as tk
from traffic_gui import TrafficLightGUI


def main():
    root = tk.Tk()
    app = TrafficLightGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
