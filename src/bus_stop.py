class BusStop:
    def __init__(self, input_name):
        self.name = input_name
        self.queue = []

    def queue_length(self):
        return len(self.queue)

    def add_to_queue(self, person_waiting):
        self.queue.append(person_waiting)

    def clear_queue(self):
        self.queue = []
