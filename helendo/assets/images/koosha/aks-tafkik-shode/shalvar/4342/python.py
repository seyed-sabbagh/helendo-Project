from PIL import Image
import os


files = os.listdir('./')
print(files)
os.mkdir('newpic')
for file in files :    
    print(file)
    image = Image.open(file)
    image = image.convert('RGB')
    file = file.replace('.webp','')
    file = file.replace('.webp','')
    print(file)

    image.save('newpic/' + file+'.webp', 'webp' , optimize=True , quality=25)



