''' File to Clean data(image file that are not openable) using os.remove'''

import os
import cv2
subdirs = []
images=[]
total = 0
subdirs = os.listdir('dataset/train/')
# print(subdirs)
for item in subdirs:
    if(item!='.DS_Store'):
        print('\n------------------\n')
        print('\nChecking for: ' + str(item))
        print('\n------------------\n')
        images = os.listdir('dataset/test/' + str(item) + '/')
        total+=(len(images))
        print('Containes ' + str(len(images)) + ' images')
        for i in images:
            if(not(i.endswith('.png') or i.endswith('.gif') or i.endswith('.jpeg') or i.endswith('.jpg') or i.endswith('.png') or i.endswith('.gif') or i.endswith('.jpeg') or i.endswith('.JPG') or i.endswith('.png') or i.endswith('.gif') or i.endswith('.jpeg') or i.endswith('.JPEG') or i.endswith('.png') or i.endswith('.gif') or i.endswith('.jpeg') or i.endswith('.PNG'))):
                print('Removing: ' + str(i))
                '''The files removed by the next command cant be recovered by any 
                means, check the path carefully'''
                # os.remove('dataset/train/' + str(item) + '/' + str(i))
print('Total Images = ', total)