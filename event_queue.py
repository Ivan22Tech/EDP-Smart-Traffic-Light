
from queue import Queue

event_queue = Queue()


def publish_event(event_type):
    event = {"type": event_type}

    event_queue.put(event)

    print(f"[QUEUE] Event added: {event_type}")


def process_events(handler):
    processed = []

    while not event_queue.empty():
        event = event_queue.get()

        print(f"[HANDLER] Processing {event['type']}")

        messages = handler(event)

        processed.append((event, messages))

        event_queue.task_done()

    return processed
