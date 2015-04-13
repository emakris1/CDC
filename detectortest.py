from GoProController import GoProController
from Detector import Detector

gpc = GoProController(device_name='wlan1')
gpc.connect('SARSGoPro', 'sarsgopro')
det = Detector()
imgs = []

for i in range(0,25):
    if(gpc.getImage('SARSGoPro', 'sarsgopro')):
        print('Image download successful!')
        img = Image.open('image.png')
        pix = img.load()
        imgs.append(pix)
        if(len(imgs) == 9):
            break
    else:
        print('Image download failed. Trying again...')

if(len(imgs) > 0):
    for pix in imgs:
        if(det.detect(pix)):
            print('Object detected in Image ' + str(imgs.index(pix)) + '!')
        else:
            print('Object not detected in Image ' + str(imgs.index(pix)) + '.')

else:
    print('No images downloaded.')
