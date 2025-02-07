from DatParser import DatParser
from cadquery import *


def main():
    dat_parser = DatParser()
    root_airfoil = dat_parser.parse_airfoil_file("airfoils/clarky.DAT")
    tip_airfoil = dat_parser.parse_airfoil_file("airfoils/clarkz.DAT")

    root_chord = 150
    tip_chord = 100
    half_wingspan = 750
    root_points = root_airfoil.get_scaled_points(root_chord)
    tip_points = tip_airfoil.get_scaled_points(tip_chord)

    result = Workplane("front").polyline(root_points).close() \
        .workplane(offset=half_wingspan).polyline(tip_points).close().loft(combine=True,ruled=True) \
        .faces(">Z").workplane(-half_wingspan/2).split(keepBottom=True, keepTop=True)


    result.export("rib.dxf")

if __name__ == '__main__':
    main()