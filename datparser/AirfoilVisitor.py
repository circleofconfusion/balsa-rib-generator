# Generated from Airfoil.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .AirfoilParser import AirfoilParser
else:
    from AirfoilParser import AirfoilParser

# This class defines a complete generic visitor for a parse tree produced by AirfoilParser.

class AirfoilVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AirfoilParser#airfoil.
    def visitAirfoil(self, ctx:AirfoilParser.AirfoilContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AirfoilParser#name.
    def visitName(self, ctx:AirfoilParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AirfoilParser#points.
    def visitPoints(self, ctx:AirfoilParser.PointsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AirfoilParser#point.
    def visitPoint(self, ctx:AirfoilParser.PointContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AirfoilParser#x.
    def visitX(self, ctx:AirfoilParser.XContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AirfoilParser#y.
    def visitY(self, ctx:AirfoilParser.YContext):
        return self.visitChildren(ctx)



del AirfoilParser