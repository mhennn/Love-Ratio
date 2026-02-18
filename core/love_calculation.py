HOURS_PER_DAY = 24
AVAILABLE_TIME_PER_DAY = 16

class RatioCalculation:
    def __init__(self):
        pass

    def interaction_ratio(self, days, hours):
        self.convert_days = int(days) * HOURS_PER_DAY
        self.hours_talking = int(days) * int(hours)

        self.talking_ratio = (int(self.hours_talking) / int(self.convert_days)) * 100
        return f"{self.talking_ratio:.2f}%"
    
    def available_life(self, hours):
        self.available_life_ratio = (int(hours) / AVAILABLE_TIME_PER_DAY) * 100
        return f"{self.available_life_ratio:.2f}%"