# Generated from Airfoil.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,3,33,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,1,0,
        1,0,1,1,4,1,17,8,1,11,1,12,1,18,1,2,4,2,22,8,2,11,2,12,2,23,1,3,
        1,3,1,3,1,4,1,4,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,0,28,0,12,1,0,0,
        0,2,16,1,0,0,0,4,21,1,0,0,0,6,25,1,0,0,0,8,28,1,0,0,0,10,30,1,0,
        0,0,12,13,3,2,1,0,13,14,3,4,2,0,14,1,1,0,0,0,15,17,5,1,0,0,16,15,
        1,0,0,0,17,18,1,0,0,0,18,16,1,0,0,0,18,19,1,0,0,0,19,3,1,0,0,0,20,
        22,3,6,3,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,
        0,24,5,1,0,0,0,25,26,3,8,4,0,26,27,3,10,5,0,27,7,1,0,0,0,28,29,5,
        2,0,0,29,9,1,0,0,0,30,31,5,2,0,0,31,11,1,0,0,0,2,18,23
    ]

class AirfoilParser ( Parser ):

    grammarFileName = "Airfoil.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "NAME", "FLOAT", "WS" ]

    RULE_airfoil = 0
    RULE_name = 1
    RULE_points = 2
    RULE_point = 3
    RULE_x = 4
    RULE_y = 5

    ruleNames =  [ "airfoil", "name", "points", "point", "x", "y" ]

    EOF = Token.EOF
    NAME=1
    FLOAT=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class AirfoilContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def name(self):
            return self.getTypedRuleContext(AirfoilParser.NameContext,0)


        def points(self):
            return self.getTypedRuleContext(AirfoilParser.PointsContext,0)


        def getRuleIndex(self):
            return AirfoilParser.RULE_airfoil

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAirfoil" ):
                listener.enterAirfoil(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAirfoil" ):
                listener.exitAirfoil(self)




    def airfoil(self):

        localctx = AirfoilParser.AirfoilContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_airfoil)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 12
            self.name()
            self.state = 13
            self.points()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self, i:int=None):
            if i is None:
                return self.getTokens(AirfoilParser.NAME)
            else:
                return self.getToken(AirfoilParser.NAME, i)

        def getRuleIndex(self):
            return AirfoilParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = AirfoilParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 15
                self.match(AirfoilParser.NAME)
                self.state = 18 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def point(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AirfoilParser.PointContext)
            else:
                return self.getTypedRuleContext(AirfoilParser.PointContext,i)


        def getRuleIndex(self):
            return AirfoilParser.RULE_points

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPoints" ):
                listener.enterPoints(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPoints" ):
                listener.exitPoints(self)




    def points(self):

        localctx = AirfoilParser.PointsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_points)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.point()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PointContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def x(self):
            return self.getTypedRuleContext(AirfoilParser.XContext,0)


        def y(self):
            return self.getTypedRuleContext(AirfoilParser.YContext,0)


        def getRuleIndex(self):
            return AirfoilParser.RULE_point

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPoint" ):
                listener.enterPoint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPoint" ):
                listener.exitPoint(self)




    def point(self):

        localctx = AirfoilParser.PointContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_point)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.x()
            self.state = 26
            self.y()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class XContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(AirfoilParser.FLOAT, 0)

        def getRuleIndex(self):
            return AirfoilParser.RULE_x

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterX" ):
                listener.enterX(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitX" ):
                listener.exitX(self)




    def x(self):

        localctx = AirfoilParser.XContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_x)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(AirfoilParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class YContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FLOAT(self):
            return self.getToken(AirfoilParser.FLOAT, 0)

        def getRuleIndex(self):
            return AirfoilParser.RULE_y

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterY" ):
                listener.enterY(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitY" ):
                listener.exitY(self)




    def y(self):

        localctx = AirfoilParser.YContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_y)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(AirfoilParser.FLOAT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





