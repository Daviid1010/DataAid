import cv2
import pytesseract

try:
    from PIL import Image
except ImportError:
    import Image

import os

print(os.getcwd())

print(pytesseract.image_to_string(Image.open('Images/reciept.jpg')))
print("--------------------------------------------------------")

#img = cv2.imread(r'swissPic.jpg')
#print(pytesseract.image_to_string(img))
# OR explicit beforehand converting
#print(pytesseract.image_to_string(Image.fromarray(img)))
