from AirfoilListener import AirfoilListener
from Airfoil import Airfoil

class AirfoilBuilderListener(AirfoilListener):
    airfoil: Airfoil

    def __init__(self):
        self.airfoil = Airfoil()
    
    def exitName(self, ctx):
        self.airfoil.name = " ".join(map(str, ctx.NAME()))

    def exitPoint(self, ctx):
        x = float(ctx.x().getText())
        y = float(ctx.y().getText())
        point = (x, y)
        self.airfoil.add_point(point)