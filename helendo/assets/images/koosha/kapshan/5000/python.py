from PIL import Image
import os


folders = os.listdir('./')
print(folders)
os.mkdir('newpic')

for folder in folders:
    files = os.listdir(folder + '/')
    print (files)


    for file in files :    
        print(file)
        image = Image.open(file)
        image = image.convert('RGB')
        file = file.replace('.webp','')
        file = file.replace('.webp','')
        print(file)

        image.save('newpic/' + file+'.webp', 'webp' , optimize=True , quality=25)



