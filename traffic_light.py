class TrafficLight:
    def __init__(self):
        self.state = "RED"

    def change_state(self, new_state):
        self.state = new_state
        print(f"[TRAFFIC LIGHT] Light is now {self.state}")

    def get_state(self):
        return self.state
