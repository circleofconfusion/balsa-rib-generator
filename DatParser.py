from antlr4 import *
from AirfoilLexer import AirfoilLexer
from AirfoilParser import AirfoilParser
from AirfoilBuilderListener import AirfoilBuilderListener
from Airfoil import Airfoil


class DatParser:
    airfoil_builder_listener: AirfoilBuilderListener

    def __init__(self):
        self.airfoil_builder_listener = AirfoilBuilderListener()

    def parse_airfoil_file(self, filename: str) -> Airfoil:
        filename = filename
        airfoil_filestream = FileStream(filename)
        lexer = AirfoilLexer(airfoil_filestream)
        stream = CommonTokenStream(lexer)
        parser = AirfoilParser(stream)

        tree = parser.airfoil();
        walker = ParseTreeWalker();

        walker.walk(self.airfoil_builder_listener, tree)

        return self.airfoil_builder_listener.airfoil