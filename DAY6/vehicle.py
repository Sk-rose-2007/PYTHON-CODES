class vehicle:
    def start(self):
        print("The vehicle has started.")

class car(vehicle):
    def start(self):
        print("The car has started.")

v=car()
v.start()
v.start()