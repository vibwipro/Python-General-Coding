import pyzbar.pyzbar as pyzbar
import cv2, numpy as np

img = cv2.imread("QR-Code.png")

decode_img = pyzbar.decode(img)
#print (decode_img)

for obj in decode_img :
    print ("Data :", obj.data)

cv2.imshow("QR-Code", img)
cv2.waitKey(0)