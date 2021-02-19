class Coordination:
    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y

    def get_coordination(self):
        return self.x, self.y

    def set_coordination(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x: " + str(self.x) + " y: " + str(self.y)

    def __eq__(self, other):
        if isinstance(other, Coordination):
            return self.x == other.x and self.y == other.y
        return False
