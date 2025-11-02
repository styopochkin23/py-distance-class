class Distance:
    def __init__(self, km):
        self.km = km
    def __str__(self):
        return f"Distance: {self.km} kilometers"
    def __repr__(self):
        return f"Distance(km={self.km})"
    def __add__(self, other):
        return Distance(self.km + other.km)
    def __iadd__(self, other):
        test = self + other
        return f"{self.km} is {test}"
    def __mul__(self, other):
        return self.km * other.km
    def __truediv__(self, other):
        return self.km / other.km
    def __lt__(self, other):
        return self.km < other.km
    def __gt__(self, other):
        return self.km > other.km
    def __eq__(self, other):
        return self.km == other.km
    def __le__(self, other):
        return self.km <= other.km
    def __ge__(self, other):
        return self.km >= other.km

