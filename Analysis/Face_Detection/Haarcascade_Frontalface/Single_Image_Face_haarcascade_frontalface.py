import  cv2

detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gimage = cv2.imread ("image.jpg")
gryimg = cv2.cvtColor(gimage, cv2.COLOR_BGR2GRAY)
face = detect.detectMultiScale(gryimg, 1.25,3)


for (x,y,w,h) in face :
    cv2.rectangle(gimage, (x,y), (x+w, y+h), (0,255,0), 2)
cv2.imshow ("detect images", gimage)
cv2.waitKey(2000)
cv2.destroyAllWindows()