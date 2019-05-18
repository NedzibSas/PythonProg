from skimage import io, color
img = io.imread('baboon.png')
dimensions = color.guess_spatial_dimensions(img)
print(dimensions)
