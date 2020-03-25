import os
import sys

if len(sys.argv) == 1:
    print("You need to provide a path to sort")
    sys.exit()
else:
    folderPath = os.path.join(os.path.normpath(sys.argv[1]),'')

contents = os.listdir(folderPath)

extensions = set()
for file in contents:
    if os.path.isfile(os.path.join(folderPath, file)):
        temp = os.path.splitext(file)
        if temp[1]:
            extensions.add(temp[1])

for ext in extensions:
    if not os.path.isdir(folderPath + ext[1:]):
        os.mkdir(folderPath + ext[1:])
        print('folder created: ' + ext[1:])
    else:
        print('folder already exists: ' + ext[1:])

    for file in contents:
        if ext in os.path.splitext(file):
            fullFilePath = os.path.join(folderPath + file)
            try:
                os.rename(fullFilePath,
                          (os.path.join(folderPath, ext[1:], file)))
                print('moved ' + file + ' to ' + ext[1:])
            except FileNotFoundError as exc:
                print(f'Cant find {fullFilePath}')
