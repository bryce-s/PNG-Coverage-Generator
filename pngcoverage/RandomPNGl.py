import png
import random
import os.path
import shutil

class RandomPNGGeneratorL(object):
    """generates and saves psuedorandom pngs"""
    
    def generatePNG(self):
        width = random.randint(1, 500)
        height = random.randint(1, 500)
        pixelArray = [[[0] for x in range(width)] for y in range(height)]
        for x in range(height):
            for y in range(width):
                grey = random.randint(0, 255)
                pixelArray[x][y] = (grey)
        return pixelArray
     
     
    def saveImage(self, fileName):
         pixelArray = self.generatePNG()
         imageObject = png.from_array(pixelArray, 'L')
         imageObject.save(fileName)
         
    
    def renderImages(self, fileName, count):
        outFolder = "pngcoverage-output-l"
        if os.path.exists(outFolder):
            shutil.rmtree(outFolder)
        os.makedirs(outFolder)
        for x in range(count):
            outDir = outFolder + "/" + fileName + str(x) + ".png"
            print(outDir)
            self.saveImage(outDir)
        
