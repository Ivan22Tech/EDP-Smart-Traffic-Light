
from event_queue import publish_event


def start_system():
    publish_event("SYSTEM_START")


def timer_expired():
    publish_event("TIMER_EXPIRED")


def pedestrian_button():
    publish_event("PEDESTRIAN_REQUEST")


def emergency_detected():
    publish_event("EMERGENCY_DETECTED")
