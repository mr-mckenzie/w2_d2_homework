class Bus:
    def __init__(self, input_route_number, input_destination):
        self.route_number = input_route_number
        self.destination = input_destination
        self.passengers = []

    def drive(self):
        return "Brum brum"
    
    def passenger_count(self):
        return len(self.passengers)
    
    def pick_up(self, passenger_being_picked_up):
        self.passengers.append(passenger_being_picked_up)

    def drop_off(self, passenger_to_drop_off):
        self.passengers.remove(passenger_to_drop_off)

    def empty_bus(self):
        self.passengers = []

    def pick_up_from_stop(self, input_bus_stop):
        
        for person_waiting in input_bus_stop.queue:
            self.pick_up(person_waiting)

        input_bus_stop.clear_queue()
