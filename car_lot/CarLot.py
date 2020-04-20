import Logger
import definitions

class CarLot:
    employees = []
    vehicles = []

    def __init__(self, employees=[], vehicles=[]):
        self.employees = employees
        self.vehicles = vehicles

    def set_employees(self, employees):
        self.employees = employees

    def get_employees(self):
        pass

