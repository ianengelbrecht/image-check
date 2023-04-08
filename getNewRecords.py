# takes a list of records or barcodes captured and checks against the existing database which have not been captured
# makes use of the same db as the barcode hunter
# remember this won't be perfect because of duplicates in the database and in the dataset, unless those are corrected first

import os
import csv
import re
import dataset
from progress.bar import Bar

cleanedBarcodesField = 'barcode_cleaned'
barcodesFileDir = r'C:\Users\i.vandermerwe\Downloads'
barcodesFileName = r'PRU-Quick-Guide-OpenRefine-Final.csv'

connstr = r'sqlite:///C:\devprojects\brahms-barcode-hunter\brahms.sqlite'
db = dataset.connect(connstr)
tables = db.tables
table = db['specimens']

fileRecords = []
with open(os.path.join(barcodesFileDir, barcodesFileName)) as f:
  reader = csv.DictReader(f)
  for row in reader:
    fileRecords.append(row)

print(len(fileRecords), 'barcodes read from', barcodesFileName)

print('checking records in db...')
bar = Bar('', max=len(fileRecords))
recordsNotInDB = []
for fileRecord in fileRecords:
  bar.next()
  dbrecord = table.find_one(Barcode=fileRecord[cleanedBarcodesField])
  if dbrecord is None:
    recordsNotInDB.append(fileRecord)

bar.finish()
db.close()

if len(recordsNotInDB) > 0:
  print('saving records for data capture')
  
  writeFile = re.sub("\.csv$", "-DataCapture.csv", barcodesFileName, flags = re.I)
  keys = recordsNotInDB[0].keys()
  with open(os.path.join(barcodesFileDir, writeFile), 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(recordsNotInDB)

  print('all done!')
else:
  print('all records were found in the database...')
