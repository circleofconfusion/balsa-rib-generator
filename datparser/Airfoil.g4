grammar Airfoil;

airfoil: name points ;

name: NAME+;
points : point+ ;
point : x y ;
x : FLOAT ;
y : FLOAT ;
NAME : [0-9a-zA-Z]+ ;
FLOAT : [-]?[0-1]'.'[0-9]+ ;
WS : [ \t\r\n]+ -> skip;