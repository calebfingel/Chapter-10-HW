import random

class insect:

    def __init__(self):
       self.wings = 2
       self.legs = 2
       self.miles = 0

    def flight(self):
        self.miles = random.ranint(1,10)

    def get_flight_length(self):
        return self.miles