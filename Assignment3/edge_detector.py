from PIL import Image
from PIL import ImageFilter
from scipy import ndimage
import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# The script is run from the terminal with the command 'ipython2 edge_detector.py path', where path is the path to the image
im = Image.open(sys.argv[1]) 

# Horizontal (resp. vertical) size of image in pixels
(lenx, leny) = im.size 

# Write function to operate Gaussian blur on image, with radius arbitrarily set to a thousandth of the largest dimension of
# the image (this is to avoid issues with blurring particularly large or resized images)

def blur(im, scale=1000):
    '''Return Gaussian-blurred image with radius set to 1/1000 of largest dimesion of the image.'''

    rad = max(lenx, leny) / scale
    return im.filter(ImageFilter.GaussianBlur(rad))

# We obtain an RGB array from the image to be able to carry gradient and other processing operations
def rgb_data(im):
    '''Convert PIL image array into an array of RGB values'''
    px = list(blur(im.convert("RGB")).getdata()) # converting from PIL datatype to ordinary sequence
    return [px[(n*lenx):((n+1)*lenx)] for n in range(leny)] # partition 1D ordinary sequence to RGB array

rgb = rgb_data(im)

# We obtain an array with the brightness of each pixel by summing the corresponding RGB values
def brightness_data(rgb):
    '''Return brightness array from rgb data'''
    return [[sum(pixel) for pixel in row] for row in rgb]

brightness = brightness_data(rgb)

# This is the core of the code. We select for edge pixels by computing the gradient magnitude.
# The gradient magnitude is computed by convolving with the first derivative of a Gaussian
# kernel with sigma arbitrarily set to 0.5. Note: We use gaussian_gradient_magnitude to compute the
# gradient directionally (as opposed to radially as gaussian_filter with order 1 does).
def edges(brightness, name, sig=0.5):
    '''Compute gradient magnitude from brightness array and select for edges and save image as name.png.'''
    edge_data = ndimage.filters.gaussian_gradient_magnitude(brightness, sig)

    figure = plt.imshow(edge_data, cmap=cm.binary) # binary colormap used to gradient magnitude

    plt.axis("off")
    figure.axes.get_xaxis().set_visible(False)
    figure.axes.get_yaxis().set_visible(False)
    plt.savefig("sigma%s_%s.png" % (int(10*sig), name), bbox_inches="tight", pad_inches=0)
    plt.clf()

    return edge_data

# We try different sigmas (default value arbitrarily set to 0.5 above) for the first derivative of Gaussian 
# kernel used to obtain the gradient magnitude to optimize edge detection. Name of saved picture is
# provided by second argument of terminal command running the script. Best performance on the image used
# is obtained using sigma=0.4, with 0.1 and 0.2 not generating an image at all.

for sig in [0.1, 0.2, 0.4, 0.5, 0.8, 1, 2, 4, 8]:
    edge_data = edges(brightness, sys.argv[2], sig)

