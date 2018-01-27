import sys
import png
from .RandomPNGrgba import RandomPNGGeneratorRGBA
from .RandomPNGl import RandomPNGGeneratorL
from .RandomPNGla import RandomPNGGeneratorla
from .RandomPNGrgb import RandomPNGGeneratorRGB

def main():
    pngGenRGBA = RandomPNGGeneratorRGBA()
    if len(sys.argv) != 3:
        print("USAGE: outFileName count")
        exit(0)
    pngGenRGBA.renderImages(sys.argv[1], int(sys.argv[2]))
    pngGenGrey = RandomPNGGeneratorL()
    pngGenGrey.renderImages(sys.argv[1], int(sys.argv[2]))
    pngGenGreyAlpha = RandomPNGGeneratorla()
    pngGenGreyAlpha.renderImages(sys.argv[1], int(sys.argv[2]))
    pngGenRGB = RandomPNGGeneratorRGB()
    pngGenRGB.renderImages(sys.argv[1], int(sys.argv[2]))

if __name__ == '__main__':
    main()
