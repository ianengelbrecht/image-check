#checks the barcodes in the dataset against the file names in the image directory and reports differences...
#TODO: remember to remove underscore values...
import os
import csv

fileCleanBarcodeField = 'barcode_cleaned'
fileDir = r'C:\Users\i.vandermerwe\Downloads'
fileName = r'PRU-Quick-Guide-OpenRefine-Final.csv'

imageDir = r'F:\Herbarium imaging\PRU\final\QuickGuide\RAW'

imagePaths = os.scandir(imageDir)
imageFiles = list(map(lambda x: os.path.basename(x), imagePaths))
imageNames = list(map(lambda x: os.path.splitext(x)[0], imageFiles))
imageNamesSansUnderscores = list(map(lambda x: x.split('_')[0], imageNames))
imagesBarcodes = set(imageNamesSansUnderscores)

fileBarcodes = set()
with open(os.path.join(fileDir, fileName)) as f:
  reader = csv.DictReader(f)
  for item in reader:
    fileBarcodes.add(item[fileCleanBarcodeField])

imagesNotInFile = imagesBarcodes.difference(fileBarcodes)
recordsWithNoImage = fileBarcodes.difference(imagesBarcodes)

print('Images not in file:')
print(' '.join(list(imagesNotInFile)))
print()
print('Records with no image:')
print(' '.join(list(recordsWithNoImage)))
print()
print('all done!')