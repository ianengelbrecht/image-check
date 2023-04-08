#remove DNG files on the main drive so that we can replace them with the CR3s from the backup
import os

backup_path = r'H:\Herbarium imaging\temp\2023'
main_RAWS_path = r'F:\Herbarium imaging\final\PRU\QuickGuide\RAW'

#read
backup_dirs = os.listdir(backup_path)

print('removing files stored as dng where cr3 exists...')
counter = 0
for dir in backup_dirs:
  if '-02' in dir:
    full_path = os.path.join(backup_path, dir)
    backup_raws = list(map(lambda x: os.path.splitext(x)[0], os.listdir(full_path)))
    for raw in backup_raws:
      file = os.path.join(main_RAWS_path, raw + '.dng')
      if os.path.isfile(file):
        os.remove(file)
        counter = counter + 1

print(counter, 'files removed')
print('all done...')