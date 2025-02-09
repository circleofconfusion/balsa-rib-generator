from DatParser import DatParser
from cadquery import *


def main():
    root_parser = DatParser()
    tip_parser = DatParser()
    root_airfoil = root_parser.parse_airfoil_file("airfoils/prandtl_root.DAT")
    tip_airfoil = tip_parser.parse_airfoil_file("airfoils/prandtl_tip.DAT")

    root_chord = 150
    tip_chord = 100
    half_wingspan = 915
    num_rib_bays = 20
    rib_thickness = 3.175
    rib_spacing = (half_wingspan - rib_thickness * (num_rib_bays + 1)) / num_rib_bays
    root_points = root_airfoil.get_scaled_points(root_chord)
    tip_points = tip_airfoil.get_scaled_points(tip_chord)

    wing = Workplane("front").spline(root_points).wire() \
        .workplane(offset=half_wingspan).spline(tip_points).wire().loft(combine=True, ruled=True)

    bays = Workplane("XY").workplane(offset=rib_thickness).box(root_chord, 100, rib_spacing, centered=False) 

    for i in (range(1,num_rib_bays)):
        bays = bays.faces(">Z").workplane(offset=rib_thickness).box(root_chord, 100, rib_spacing, centered=False)
        
    bays = bays.translate((0,-50,0))
    wing = wing.cut(bays)
    
    wing.export("output/rib.svg", opt={"strokeWidth":0.01, "projectionDir":[0,0,1], "strokeColor":(255,255,255), "marginLeft":50})
    # wing.export("output/rib.svg", opt={"strokeWidth":0.1, "strokeColor":(255,255,255), "marginLeft":50})

if __name__ == '__main__':
    main()