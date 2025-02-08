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
        4,0,3,29,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,1,0,4,0,9,8,0,11,0,12,0,10,
        1,1,3,1,14,8,1,1,1,1,1,1,1,4,1,19,8,1,11,1,12,1,20,1,2,4,2,24,8,
        2,11,2,12,2,25,1,2,1,2,0,0,3,1,1,3,2,5,3,1,0,5,4,0,45,45,48,57,65,
        90,97,122,1,0,45,45,1,0,48,49,1,0,48,57,3,0,9,10,13,13,32,32,32,
        0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,1,8,1,0,0,0,3,13,1,0,0,0,5,23,
        1,0,0,0,7,9,7,0,0,0,8,7,1,0,0,0,9,10,1,0,0,0,10,8,1,0,0,0,10,11,
        1,0,0,0,11,2,1,0,0,0,12,14,7,1,0,0,13,12,1,0,0,0,13,14,1,0,0,0,14,
        15,1,0,0,0,15,16,7,2,0,0,16,18,5,46,0,0,17,19,7,3,0,0,18,17,1,0,
        0,0,19,20,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,4,1,0,0,0,22,24,
        7,4,0,0,23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,
        26,27,1,0,0,0,27,28,6,2,0,0,28,6,1,0,0,0,5,0,10,13,20,25,1,6,0,0
    ]

class AirfoilLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NAME = 1
    FLOAT = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "NAME", "FLOAT", "WS" ]

    ruleNames = [ "NAME", "FLOAT", "WS" ]

    grammarFileName = "Airfoil.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


