class RaceCar:
    
    def __init__(self, color, fuel_remaining, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        for key, value in kwargs:
            setattr(self, key, value)
