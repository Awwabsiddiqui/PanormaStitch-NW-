import cv2
import os

mainFolder = 'Images'
myFolder = os.listdir(mainFolder)
for folder in myFolder:
    path = mainFolder +'/'+folder
    images=[]
    myList = os.listdir(path)

    for imgN in myList:
        cur=cv2.imread(f'{path}/{imgN}')
        cv2.imshow(cur)
        cur=cv2.resize(cur,(0,0,),None,0.2,0.2)
        images.append(cur)
    stitch=cv2.Stitcher.create()
    (status,result)=stitch.stitch(images)
    if(status==cv2.STITCHER_OK):
        print('Panorama')
        cv2.imshow(folder,result)
        cv2.waitKey(1)
    else:print('Nope')
cv2.waitKey(0)