# Generated from Airfoil.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,4,46,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,4,0,11,8,0,11,
        0,12,0,12,1,0,3,0,16,8,0,1,1,3,1,19,8,1,1,1,1,1,1,1,4,1,24,8,1,11,
        1,12,1,25,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,4,
        3,41,8,3,11,3,12,3,42,1,3,1,3,0,0,4,1,1,3,2,5,3,7,4,1,0,5,3,0,48,
        57,65,90,97,122,1,0,45,45,1,0,48,49,1,0,48,57,3,0,9,10,13,13,32,
        32,50,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,1,10,1,0,0,
        0,3,18,1,0,0,0,5,27,1,0,0,0,7,40,1,0,0,0,9,11,7,0,0,0,10,9,1,0,0,
        0,11,12,1,0,0,0,12,10,1,0,0,0,12,13,1,0,0,0,13,15,1,0,0,0,14,16,
        3,5,2,0,15,14,1,0,0,0,15,16,1,0,0,0,16,2,1,0,0,0,17,19,7,1,0,0,18,
        17,1,0,0,0,18,19,1,0,0,0,19,20,1,0,0,0,20,21,7,2,0,0,21,23,5,46,
        0,0,22,24,7,3,0,0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,
        1,0,0,0,26,4,1,0,0,0,27,28,5,65,0,0,28,29,5,73,0,0,29,30,5,82,0,
        0,30,31,5,70,0,0,31,32,5,79,0,0,32,33,5,73,0,0,33,34,5,76,0,0,34,
        35,1,0,0,0,35,36,6,2,0,0,36,37,1,0,0,0,37,38,6,2,1,0,38,6,1,0,0,
        0,39,41,7,4,0,0,40,39,1,0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,43,
        1,0,0,0,43,44,1,0,0,0,44,45,6,3,1,0,45,8,1,0,0,0,6,0,12,15,18,25,
        42,2,1,2,0,6,0,0
    ]

class AirfoilLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NAME = 1
    FLOAT = 2
    AIRFOIL = 3
    WS = 4

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "NAME", "FLOAT", "AIRFOIL", "WS" ]

    ruleNames = [ "NAME", "FLOAT", "AIRFOIL", "WS" ]

    grammarFileName = "Airfoil.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[2] = self.AIRFOIL_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def AIRFOIL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            1
     


