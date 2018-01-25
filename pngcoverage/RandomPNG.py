import png
import random


class RandomPNGGenerator(object):
    """generates and saves psuedorandom pngs"""
    
    def generatePNG(self):
        width = random.randint(1, 400)
        height = random.randint(1, 400)
        pixelArray = [[[0,0,0] for x in range(width)] for y in range(height)]
        for x in range(height):
            for y in range(width):
                red = random.randint(0, 255)
                blue = random.randint(0, 255)
                green = random.randint(0, 255)
                alpha = random.randint(0,100)
                pixelArray[x][y] = (red, blue, green, alpha)
        return pixelArray
     
     
    def saveImage(self, fileName):
         pixelArray = self.generatePNG()
         imageObject = png.from_array(pixelArray, 'RGBA')
         imageObject.save(fileName)
         