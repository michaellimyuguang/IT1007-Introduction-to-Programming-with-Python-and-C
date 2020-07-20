from scipy import misc,ndimage
import matplotlib.pyplot as plt
import numpy as np


def blur_image(filename):
    pic = misc.imread(filename)
    blurred_pic = ndimage.gaussian_filter(pic, sigma=(5,5,1))

    plt.imshow(blurred_pic)
    plt.imsave("blur_image_output.jpg",blurred_pic)
    plt.show()


