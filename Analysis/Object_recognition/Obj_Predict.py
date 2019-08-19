#### We will give an image as input and it will revert all images of similar Group
#### This code will search all similar images and publish it.

from PIL import Image
import numpy as np, sys
import matplotlib.pyplot as plt
from collections import Counter


def createfile():
    numberArrayExamples = open('objArEx.txt', 'a')
    numbersWeHave = ['g', 'l']
    versionsWeHave = range(1, 10)

    for e_fst in numbersWeHave:
        for e_Sec in versionsWeHave:
            # print str(eachNum)+'.'+str(eachVer)
            imgFilePath = 'images/Object/' + str(e_fst) + str(e_Sec) + '.jpg'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)
            eiar1 = str(eiar.tolist())
            lineToWrite = str(e_fst) + '::' + eiar1 + '\n'
            numberArrayExamples.write(lineToWrite)



def FindAllSimilarImages(filePath):
    matchedAr = []
    loadExamps = open('objArEx.txt', 'r').read()
    loadExamps = loadExamps.split('\n')

    i = Image.open(filePath)
    iar = np.array(i)
    iarl = iar.tolist()
    print (type(iar))
    print((iar))

    iQue = str(iarl)
    print (iQue)

    for e_Exp in loadExamps:
        #print ((eachExample))

        if len(e_Exp) > 3:
            splitEx = e_Exp.split('::')
            currentNum = splitEx[0]
            currentAr = splitEx[1]
            iar2 = np.array(currentAr)
            eachPixEx = currentAr.split('],')
            eachPixInQ = iQue.split('],')

            x,y = 0,0

            while x < len(eachPixEx):
                if eachPixEx[x] == eachPixInQ[x]:
                    matchedAr.append((currentNum))
                    y +=1
                x += 1
            if (x == y ) :
                f_currentNum = currentNum
            else :
                y = 0



    print(matchedAr)
    x = Counter(matchedAr)
    print(x)

    versionsWeHave = range(1, 10)

    for e_Ver in versionsWeHave:
            # print str(eachNum)+'.'+str(eachVer)
            imgFilePath = 'images/Object/' + str(f_currentNum) + str(e_Ver) + '.jpg'
            ei = Image.open(imgFilePath)
            eiar = np.array(ei)

            fig = plt.figure()
            ax = plt.subplot2grid((2, 2), (0, 0), rowspan=1, colspan=4)
            ax.imshow(eiar)
            plt.show()



######## function 'createfile' is called to create ObjArEx.txt file
######## It has arrays of all pictures
#createfile ()

#### We have used 60 x 60 Frame photo
#### We will give an image as input and it will revert all images of similar Group
FindAllSimilarImages('images/Obj_test2.jpg')
