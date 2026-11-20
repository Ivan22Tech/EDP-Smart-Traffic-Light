from queue import Queue

event_queue = Queue()

def publish_event(event):
    event_queue.put(event)
    print(f"[QUEUE] Event added: {event['type']}")

def process_events(handler):
    while not event_queue.empty():
        event = event_queue.get()
        handler(event)
        event_queue.task_done()
