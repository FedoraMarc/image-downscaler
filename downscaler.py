from os import listdir, mkdir
from os.path import exists
from PIL import Image
from sys import argv

if (len(argv) != 3):
    print('Two arguments must be given: The input directory and the target resolution.')
    quit()

filenames = listdir(argv[1])
target_res = int(argv[2])

outputpath = './output/'
extensions = ('.png', '.jpg', '.jpeg')

if (exists(outputpath) == False):
    mkdir(outputpath)

for filename in filenames:
    if (filename.endswith(extensions)):
        print('Processing ' + filename)
        image = Image.open(argv[1] + filename)
        downscaled_image = image.resize((target_res, target_res))
        downscaled_image.save(outputpath + filename)
