from event_queue import process_events
from event_handlers import handle_event

from event_producers import (
    start_system,
    timer_expired,
    pedestrian_button,
    emergency_detected
)

def main():

    print("=" * 40)
    print("   SMART TRAFFIC LIGHT SYSTEM")
    print("   Event-Driven Programming Project")
    print("=" * 40)

    # Start the traffic system
    start_system()
    process_events(handle_event)

    # Traffic timer events
    timer_expired()
    process_events(handle_event)

    timer_expired()
    process_events(handle_event)

    # Pedestrian requests crossing
    pedestrian_button()
    process_events(handle_event)

    timer_expired()
    process_events(handle_event)

    # Emergency vehicle detected
    emergency_detected()
    process_events(handle_event)

    print("\nSimulation completed successfully!")

if __name__ == "__main__":
    main()
