import glob, cv2

detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
gimage = glob.glob ("*.jpg")

for timage in gimage :
    image = cv2.imread (timage)
    gryimg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face = detect.detectMultiScale(gryimg, 1.25,3)
    for (x,y,w,h) in face :
        cv2.rectangle(image, (x,y), (x+w, y+h), (0,255,0), 2)
    cv2.imshow ("detect images", image)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()