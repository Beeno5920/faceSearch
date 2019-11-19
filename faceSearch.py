import zipfile
from zipfile import ZipFile

from PIL import Image
import pytesseract
import cv2 as cv
import numpy as np

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')

imageText = {}
imageFace = {}


def getImagesFromZipFile(file):
    imagesDict = {}
    with ZipFile(file) as myzip:
        fileLst = myzip.namelist()
        ZipFile.extractall(myzip)
        for file in fileLst:
            imagesDict[file] = Image.open(file).convert('RGB')
    return imagesDict


def getText(images):
    for imgName in images.keys():
        img = images[imgName]
        imageText[imgName] = pytesseract.image_to_string(img)


def findFaces(images):
    for imageName in images.keys():
        CVImage = np.array(images[imageName])
        convertedImg = cv.cvtColor(CVImage, cv.COLOR_BGR2GRAY)
        boundingBox = face_cascade.detectMultiScale(convertedImg, 1.3, 5)
        faceLst = []
        for x, y, w, h in boundingBox:
            imgCopy = images[imageName].copy()
            face = imgCopy.crop((x, y, x + w, y + h)).resize((100, 100))
            faceLst.append(face)
        imageFace[imageName] = faceLst


def search(keyword, images):
    for imageName in images:
        if keyword in imageText[imageName]:
            if len(imageFace[imageName]) > 0:
                print("Results found in file {}".format(imageName))
                h = len(imageFace[imageName]) // 5 + 1
                contactSheet = Image.new('RGB', (500, 100 * h))
                x = y = 0
                for face in imageFace[imageName]:
                    contactSheet.paste(face, (x, y))
                    if x + 100 >= contactSheet.width:
                        x = 0
                        y += 100
                    else:
                        x += 100
                #display(contactSheet)
                contactSheet.show()
            else:
                print("Results found in file {} \nBut there were no faces in that file".format(imageName))
        else:
            print("No results in file {}".format(imageName))


def main():
    # testing images.zip file
    images = getImagesFromZipFile("readonly/small_img.zip")
    getText(images)
    findFaces(images)
    print("===Searching 'Mark' in the small images===")
    search("Mark", images)


if __name__ == '__main__':
    main()