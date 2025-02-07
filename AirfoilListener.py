# Generated from Airfoil.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AirfoilParser import AirfoilParser
else:
    from AirfoilParser import AirfoilParser

# This class defines a complete listener for a parse tree produced by AirfoilParser.
class AirfoilListener(ParseTreeListener):

    # Enter a parse tree produced by AirfoilParser#airfoil.
    def enterAirfoil(self, ctx:AirfoilParser.AirfoilContext):
        pass

    # Exit a parse tree produced by AirfoilParser#airfoil.
    def exitAirfoil(self, ctx:AirfoilParser.AirfoilContext):
        pass


    # Enter a parse tree produced by AirfoilParser#name.
    def enterName(self, ctx:AirfoilParser.NameContext):
        pass

    # Exit a parse tree produced by AirfoilParser#name.
    def exitName(self, ctx:AirfoilParser.NameContext):
        pass


    # Enter a parse tree produced by AirfoilParser#points.
    def enterPoints(self, ctx:AirfoilParser.PointsContext):
        pass

    # Exit a parse tree produced by AirfoilParser#points.
    def exitPoints(self, ctx:AirfoilParser.PointsContext):
        pass


    # Enter a parse tree produced by AirfoilParser#point.
    def enterPoint(self, ctx:AirfoilParser.PointContext):
        pass

    # Exit a parse tree produced by AirfoilParser#point.
    def exitPoint(self, ctx:AirfoilParser.PointContext):
        pass


    # Enter a parse tree produced by AirfoilParser#x.
    def enterX(self, ctx:AirfoilParser.XContext):
        pass

    # Exit a parse tree produced by AirfoilParser#x.
    def exitX(self, ctx:AirfoilParser.XContext):
        pass


    # Enter a parse tree produced by AirfoilParser#y.
    def enterY(self, ctx:AirfoilParser.YContext):
        pass

    # Exit a parse tree produced by AirfoilParser#y.
    def exitY(self, ctx:AirfoilParser.YContext):
        pass



del AirfoilParser