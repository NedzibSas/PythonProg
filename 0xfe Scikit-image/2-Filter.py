from skimage import data, io, filters
from skimage.color import rgb2gray
img = io.imread('baboon.png')
img_grayscale = rgb2gray(img)
edges = filters.sobel(img_grayscale)
io.imshow(edges)
io.show()
