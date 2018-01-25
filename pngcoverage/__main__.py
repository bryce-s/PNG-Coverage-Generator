import sys
import png
from .RandomPNG import RandomPNGGenerator

def main():
    pngGen = RandomPNGGenerator()
    pngGen.generatePNG
    if len(sys.argv) != 3:
        print("USAGE: outFileName count")
        exit(0)
    pngGen.renderImages(sys.argv[1], int(sys.argv[2]))

if __name__ == '__main__':
    main()
