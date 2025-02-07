from DatParser import DatParser
import matplotlib.pyplot as plt



def main():
    dat_parser = DatParser()
    airfoil = dat_parser.parse_airfoil_file("airfoils/clarkz.DAT")

    chord = 6

    fig, ax = plt.subplots()

    ax.set_ylim(-chord/2, chord/2)
    ax.set_xlim(-0.1, chord + 1)
    ax.plot(airfoil.get_xs(chord), airfoil.get_ys(chord), scalex=False, scaley=False)

    plt.show()

if __name__ == "__main__":
    main()
