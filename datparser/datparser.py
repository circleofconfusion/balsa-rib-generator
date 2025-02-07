from antlr4 import *
from AirfoilLexer import AirfoilLexer
from AirfoilParser import AirfoilParser
from AirfoilListener import AirfoilListener
from Airfoil import Airfoil, Point

class AirfoilBuilderListener(AirfoilListener):
    airfoil: Airfoil

    def __init__(self):
        self.airfoil = Airfoil();
    
    def exitName(self, ctx):
        self.airfoil.name = " ".join(map(str, ctx.NAME()))

    def exitPoint(self, ctx):
        point = Point(float(ctx.x().getText()), float(ctx.y().getText()))
        self.airfoil.add_point(point)


filename = '/home/shane/RC Vehicles/BalsaRibGenerator/datparser/airfoils/eppler331.dat'
airfoil_filestream = FileStream(filename)
lexer = AirfoilLexer(airfoil_filestream)
stream = CommonTokenStream(lexer)
parser = AirfoilParser(stream)
airfoil_builder_listener = AirfoilBuilderListener()


tree = parser.airfoil();

walker = ParseTreeWalker();

walker.walk(airfoil_builder_listener, tree)

airfoil = airfoil_builder_listener.airfoil

print(airfoil.get_xs())
print(airfoil.get_ys())
print(list(map(str, airfoil.points)))