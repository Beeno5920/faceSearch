# faceSearch
A python program that can find human faces from the given images base on the keyword and show them.

## How it works?
This program uses the libraries Pillow, pytesseract, open-cv and zipfile. It first extract the zip file and obtains the images
inside it. Then it applies OCR on those images to get the texts in the images. If the texts contain the keyword needed to
search, it will use the functions provided by "open-cv" library to find and crop the human faces from the images. Finally a 
contact sheet contains those faces will be generated for each input images.

### Example:
Searching "Mark" on the images in small_img.zip:
Those images are:
[!a-0.png]https://github.com/Beeno5920/faceSearch/blob/master/a-0.png
[!a-1.png]https://github.com/Beeno5920/faceSearch/blob/master/a-1.png
[!a-2.png]https://github.com/Beeno5920/faceSearch/blob/master/a-2.png
[!a-3.png]https://github.com/Beeno5920/faceSearch/blob/master/a-3.png

And the corresponding search results are:
[!resultOfa-0.png]https://github.com/Beeno5920/faceSearch/blob/master/resultOfa-0.png
[!resultOfa-1.png]https://github.com/Beeno5920/faceSearch/blob/master/resultOfa-1.png
[!resultOfa-2.png]https://github.com/Beeno5920/faceSearch/blob/master/resultOfa-2.png
[!resultOfa-3.png]https://github.com/Beeno5920/faceSearch/blob/master/resultOfa-3.png
