from antlr4 import *
from AirfoilLexer import AirfoilLexer
from AirfoilParser import AirfoilParser
from AirfoilListener import AirfoilListener
from Airfoil import Airfoil

class AirfoilBuilderListener(AirfoilListener):
    airfoil: Airfoil

    def __init__(self):
        self.airfoil = Airfoil();
    
    def exitName(self, ctx):
        self.airfoil.name = " ".join(map(str, ctx.NAME()))

    def exitPoint(self, ctx):
        x = float(ctx.x().getText())
        y = float(ctx.y().getText())
        point = (x, y)
        self.airfoil.add_point(point)


class DatParser:

    def parse_airfoil_file(self, filename: str) -> Airfoil:
        filename = filename
        airfoil_filestream = FileStream(filename)
        lexer = AirfoilLexer(airfoil_filestream)
        stream = CommonTokenStream(lexer)
        parser = AirfoilParser(stream)
        airfoil_builder_listener = AirfoilBuilderListener()

        tree = parser.airfoil();
        walker = ParseTreeWalker();

        walker.walk(airfoil_builder_listener, tree)

        return airfoil_builder_listener.airfoil