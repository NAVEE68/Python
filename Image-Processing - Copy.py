#Image Procession
import numpy as np
from scipy import ndimage

from scipy import misc
f=misc.face()
misc.imsave('face2.png',f)



import matplotlib.pyplot as plt
plt.imshow(f)
#Creating numpy array from image.. First we need to craete the PNG
face=misc.imread('face.png')
type(face)
face.shape
face.dtype

#Opening a raw file
face.tofile('face.raw')#Create the raw file
face_from_raw=np.fromfile('face.raw',dtype=np.uint8) #Opening face
face_from_raw.shape
face_from_raw.shape=(768,1024,3)


f=misc.face(gray=True)#Retrieve a grayscale image

import matplotlib.pyplot as plt
plt.imshow(f,cmap=plt.cm.gray)
plt.imshow(f,cmap=plt.cm.Blues)
plt.imshow(f,cmap=plt.cm.Greens)


#Changing contrast
plt.imshow(f,cmap=plt.cm.gray,vmin=30,vmax=200)






