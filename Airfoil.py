class Airfoil:
    name: str = ""
    points: list[tuple[float,float]] = []

    def add_point(self, point: tuple[float,float]):
        self.points.append(point)
    
    def get_scaled_points(self, chord_mm: float):
        scaled_points = []
        for p in self.points:
            scaled_point = (p[0] * chord_mm, p[1] * chord_mm)
            if (len(scaled_points) == 0 or scaled_point != scaled_points[-1]):
                scaled_points.append(scaled_point)
        
        return scaled_points
