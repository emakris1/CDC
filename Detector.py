# Class for detecting white objects in images

# Test Procedure:
# from Detector import Detector
# c = Detector()
# test = c.detect(<path_to_image>)
# if test:
#       print("The image contains the object!")
# else:
#       print("The image does not contain the object.")

from PIL import Image

class Detector:

        def detect(self, image):
                pix = image.load()
                size = image.size

                # Check image for ten adjacent pixels whose rgb values all average out above 200.
                # Only checks horizontally adjacent pixels, not vertically or diagonally adjacent ones.
                for j in range(0,size[1]):
                    count = 0
                    for i in range(0,size[0]):
                        avg = (pix[i,j][0] + pix[i,j][1] + pix[i,j][2])/3
                        if avg > 200:
                            count += 1
                            if count == 10:
                                return True
                        else:
                            count = 0

                return False
