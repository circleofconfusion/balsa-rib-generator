
class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __eq__(self, point):
        return self.x == point.x and self.y == point.y


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
    
    def get_scaled_points(self, chord_mm: int):
        scaled_points = []
        for p in self.points:
            scaled_point = Point(p.x * chord_mm, p.y * chord_mm)
            if (len(scaled_points) == 0 or scaled_point != scaled_points[-1]):
                scaled_points.append(scaled_point)
        
        return scaled_points
