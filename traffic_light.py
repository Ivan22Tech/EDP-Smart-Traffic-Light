
class TrafficLight:

    def __init__(self):
        self.state = "OFF"

    def change_state(self, new_state):
        self.state = new_state
        print(f"[TRAFFIC LIGHT] Light is now {new_state}")

    def get_state(self):
        return self.state

