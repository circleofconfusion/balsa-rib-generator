
class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


class Airfoil:
    name: str = ""
    points: list[Point] = []

    def add_point(self, point: Point):
        self.points.append(point)

    def get_xs(self, chord: float = 1.0) -> list[float]:
        scaled_xs = []
        for p in self.points:
            scaled_xs.append(p.x * chord)
        return scaled_xs
    
    def get_ys(self, chord: float = 1.0) -> list[float]:
        scaled_ys = []
        for p in self.points:
            scaled_ys.append(p.y * chord)
        return scaled_ys
