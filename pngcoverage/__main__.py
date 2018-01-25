import sys
import png
from .RandomPNG import RandomPNGGenerator

def main():
    pngGen = RandomPNGGenerator()
    pngGen.generatePNG()
    args = sys.argv[1:]
    pngGen.saveImage("hello.png")

if __name__ == '__main__':
    main()
