#Which day's CSV files have duplicated barcodes?

import os, csv

csvDir = r'F:\Herbarium imaging\PRU\datasheets'

#get all the barcodes for each file
fileDict = {}
csvFiles = filter(lambda file: file.endswith('.csv'), os.listdir(csvDir))
for csvName in csvFiles:
    fileDate = csvName.split(' ')[0]
    fileDict[fileDate] = set()
    with open(os.path.join(csvDir, csvName), mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            fileDict[fileDate].add(row['barcode'])

#print the intersection matrix. Higher values mean more overlap
fileDates = list(fileDict.keys())
res = []

print('file1', 'file2', 'overlap')
for i in range(1, len(fileDates)):
  for j in range(i + 1, len(fileDates)):
    i_barcodes = set(fileDict[fileDates[i]])
    j_barcodes = set(fileDict[fileDates[j]])
    int = i_barcodes.intersection(j_barcodes)
    un = i_barcodes.union(j_barcodes)
    prop = round(len(int) / len(un), 2)
    if prop > 0.5:
      print(fileDates[i], fileDates[j], prop)