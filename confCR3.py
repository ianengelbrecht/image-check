#script to confirm all cr3 files from PRU are converted to DNG
import os

source_path = r'H:\Herbarium imaging\temp\2023'
dest_path = r'F:\Herbarium imaging\final\PRU\QuickGuide\RAW'

source_dirs = os.listdir(source_path)
dest_files = list(map(lambda x: os.path.splitext(x)[0], os.listdir(dest_path)))

missing = []
for dir in source_dirs:
  if '-02' in dir:
    full_path = os.path.join(source_path, dir)
    dir_files = list(map(lambda x: os.path.splitext(x)[0], os.listdir(full_path)))
    for file in dir_files:
      if file not in dest_files:
        missing.append(dir + '/' + file)

with open('result.txt', 'w') as f:
  for file in missing:
    f.write(file + '\n')

print('all done!') 