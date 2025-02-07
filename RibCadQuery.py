from DatParser import DatParser
from cadquery import *
from cadquery.vis import show
from Airfoil import Point

def pointToTuple(point: Point):
    return (point.x, point.y);


def main():
    dat_parser = DatParser()
    airfoil = dat_parser.parse_airfoil_file("airfoils/clarkz.DAT")

    chord_mm = 150
    points = list(map(pointToTuple, airfoil.get_scaled_points(chord_mm)))

    result = Workplane("XY").polyline(points)


    result = result.close()

    # show(result, edges=True)
    result.export("rib.svg", opt={"projectionDir":[0,0,1], "marginLeft":10, "width":170, "height":50})

if __name__ == '__main__':
    main()