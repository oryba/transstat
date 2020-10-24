class Route:
    def __init__(self, idx, _type, name, vehicles: list = None):
        self.type = _type
        self.name = name
        self.idx = idx
        self.vehicles = vehicles

    def __repr__(self):
        return f"Route {self.type}{self.name}"


class Vehicle:
    def __init__(self, idx, number, _type):
        self.idx = idx
        self.number = number
        self.type = _type

    def __repr__(self):
        return f"Vehicle {self.number}"


class TransRecord:
    def __init__(self, number: str, model: str, status: str, _type: type):
        self.number = number
        self.model = model
        self.status = status
        self.type = _type

    def __repr__(self):
        return f"{self.type} {self.model} #{self.number} ({self.status})"
