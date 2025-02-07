
class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


def get_x(point: Point):
    return point.x

def get_y(point: Point):
    return point.y


class Airfoil:
    name: str
    points: list[Point]

    def add_point(self, point: Point):
        self.points.append(point)

    def get_xs(self):
        return map(get_x, self.points)
    
    def get_ys(self):
        return map(get_y, self.points)
