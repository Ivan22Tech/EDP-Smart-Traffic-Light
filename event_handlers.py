
from traffic_light import TrafficLight

traffic_light = TrafficLight()

pedestrian_waiting = False
pedestrian_crossing = False
emergency_active = False


def handle_event(event):
    global pedestrian_waiting
    global pedestrian_crossing
    global emergency_active

    event_type = event["type"]
    messages = []

    if event_type == "SYSTEM_START":

        traffic_light.change_state("GREEN")
        messages.append("System started: GREEN light")

    elif event_type == "PEDESTRIAN_REQUEST":

        if not pedestrian_crossing:
            pedestrian_waiting = True
            messages.append("Pedestrian crossing requested")

    elif event_type == "TIMER_EXPIRED":

        if emergency_active:
            emergency_active = False
            traffic_light.change_state("GREEN")
            messages.append("Emergency cleared: GREEN light")

        elif pedestrian_crossing:
            pedestrian_crossing = False
            traffic_light.change_state("GREEN")
            messages.append("Pedestrian crossing finished")

        elif traffic_light.get_state() == "GREEN":

            traffic_light.change_state("YELLOW")
            messages.append("GREEN changed to YELLOW")

        elif traffic_light.get_state() == "YELLOW":

            traffic_light.change_state("RED")
            messages.append("YELLOW changed to RED")

        elif traffic_light.get_state() == "RED":

            if pedestrian_waiting:
                pedestrian_waiting = False
                pedestrian_crossing = True
                messages.append("PEDESTRIAN CROSSING ACTIVE")
            else:
                traffic_light.change_state("GREEN")
                messages.append("RED changed to GREEN")

    elif event_type == "EMERGENCY_DETECTED":

        emergency_active = True
        pedestrian_crossing = False

        traffic_light.change_state("RED")

        messages.append("EMERGENCY PRIORITY ACTIVATED")
        messages.append("Traffic stopped for emergency vehicle")

    return messages

