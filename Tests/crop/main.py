# Importing Image class from PIL module
from PIL import Image
 
# Opens a image in RGB mode
im = Image.open(r"/media/coder/Linux\ Media/MyProjects/codeshot/Tests/001\ oct\ 26/img-1.png")
 
# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size
 
# Setting the points for cropped image
left = 5
top = height / 4
right = 164
bottom = 3 * height / 4
 
# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop(left, top, right, bottom)
 
# Shows the image in image viewer
im1.show()