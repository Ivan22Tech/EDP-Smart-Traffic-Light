from traffic_light import TrafficLight

traffic_light = TrafficLight()
pedestrian_waiting = False

def handle_event(event):
    global pedestrian_waiting

    event_type = event["type"]

    print(f"[HANDLER] Processing {event_type}")

    if event_type == "SYSTEM_START":
        traffic_light.change_state("GREEN")

    elif event_type == "TIMER_EXPIRED":

        if traffic_light.get_state() == "GREEN":
            traffic_light.change_state("YELLOW")

        elif traffic_light.get_state() == "YELLOW":
            traffic_light.change_state("RED")

        elif traffic_light.get_state() == "RED":
            if pedestrian_waiting:
                print("[PEDESTRIAN] Crossing enabled")
                pedestrian_waiting = False

            traffic_light.change_state("GREEN")

    elif event_type == "PEDESTRIAN_REQUEST":
        pedestrian_waiting = True
        print("[PEDESTRIAN] Crossing request received")

    elif event_type == "EMERGENCY_DETECTED":
        traffic_light.change_state("RED")
        print("[EMERGENCY] Emergency priority activated!")
