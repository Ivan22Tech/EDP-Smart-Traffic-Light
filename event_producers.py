from event_queue import publish_event

def start_system():
    publish_event({"type": "SYSTEM_START"})

def timer_expired():
    publish_event({"type": "TIMER_EXPIRED"})

def pedestrian_button():
    publish_event({"type": "PEDESTRIAN_REQUEST"})

def emergency_detected():
    publish_event({"type": "EMERGENCY_DETECTED"})
