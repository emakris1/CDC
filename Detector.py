# Class for detecting white objects in images

class Detector:

        def detect(self, pix):
                # Check image for ten adjacent pixels whose rgb values all average out above 200.
                # Only checks horizontally adjacent pixels, not vertically or diagonally adjacent ones.
                for j in range(0,240):
                    count = 0
                    for i in range(0,432):
                        avg = (pix[i,j][0] + pix[i,j][1] + pix[i,j][2])/3
                        if avg > 200:
                            count += 1
                            if count == 10:
                                return True
                        else:
                            count = 0

                return False
