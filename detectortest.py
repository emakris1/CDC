from GoProController import GoProController
from Detector import Detector

gpc = GoProController(device_name='wlan1')
gpc.connect('SARSGoPro', 'sarsgopro')
det = Detector()
imgs = []

for i in range(0,25):
    img = gpc.getImage('SARSGoPro', 'sarsgopro')
    if img:
        print('Image download successful!')
        imgs.append(img)
        if(len(imgs) == 9):
            break
    else:
        print('Image download failed. Trying again...')

if(len(imgs) > 0):
    for img in imgs:
        if(det.detect(img)):
            print('Object detected in Image ' + str(imgs.index(img)) + '!')
        else:
            print('Object not detected in Image ' + str(imgs.index(img)) + '.')

else:
    print('No images downloaded.')
