import png
import random
import os.path
import shutil

class BitDepthGenerator(object):
    """generates and saves psuedorandom pngs"""
    
    def generatePNG(self):
        width = random.randint(1, 500)
        height = random.randint(1, 500)
        pixelArray = [[[0,0,0] for x in range(width)] for y in range(height)]
        for x in range(height):
            for y in range(width):
                red = random.randint(0, 255)
                blue = random.randint(0, 255)
                green = random.randint(0, 255)
                alpha = random.randint(0,100)
                pixelArray[x][y] = (red, blue, green, alpha)
        return pixelArray
     
     
    def saveImage(self, fileName, depth):
         pixelArray = self.generatePNG()
         imageObject = png.from_array(pixelArray, "RGBA;" + str(depth))
         imageObject.save(fileName)
         
    
    def renderImages(self, fileName, count):
        outFolder = "pngcoverage-output-depth"
        if os.path.exists(outFolder):
            shutil.rmtree(outFolder)
        os.makedirs(outFolder)
        for depth in range(8, 16):
            """iterate through bit depths 8 16, print rgba img with each"""
            outDir = outFolder + "/" + fileName + str(depth) + ".png"
            print(outDir)
            self.saveImage(outDir, depth)
        
