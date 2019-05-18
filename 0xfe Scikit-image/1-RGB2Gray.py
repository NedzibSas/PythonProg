import skimage.io as io
from skimage.color import rgb2gray
img = io.imread('baboon.png')
print (img.shape)
#convertir img a blanco y negro '2d'
img_grayscale = rgb2gray(img)
#Guardar img en blanco y negro
io.imsave('baboon-gs.png',img_grayscale)
#Mostrar img en blanco y negro
show_grayscale = io.imshow(img_grayscale)
io.show()
