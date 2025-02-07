from antlr4 import *
from AirfoilLexer import AirfoilLexer
from AirfoilParser import AirfoilParser

# with open('/home/shane/RC Vehicles/BalsaRibGenerator/datparser/airfoils/eppler331.dat', encoding='UTF-8', ) as airfoil_file:
filename = '/home/shane/RC Vehicles/BalsaRibGenerator/datparser/airfoils/eppler331.dat'
airfoil_filestream = FileStream(filename)
lexer = AirfoilLexer(airfoil_filestream)
stream = CommonTokenStream(lexer)
parser = AirfoilParser(stream)

tree = parser.airfoil();

print(tree.toStringTree(recog=parser))