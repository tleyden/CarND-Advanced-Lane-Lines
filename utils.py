import numpy as np
import matplotlib.pyplot as plt
import cv2

def show_images(images, cols=1, scale_factor=1.0, cv2ConvertTarget=None, titles=None):
    """

    Taken from: https://gist.github.com/soply/f3eec2e79c165e39c9d540e916142ae1
    and adapted to add a scale_factor param.

    Display a list of images in a single figure with matplotlib.

    Parameters
    ---------
    images: List of np.arrays compatible with plt.imshow.

    cols (Default = 1): Number of columns in figure (number of rows is
                        set to np.ceil(n_images/float(cols))).

    titles: List of titles corresponding to each image. Must have
            the same length as titles.
    """
    assert ((titles is None) or (len(images) == len(titles)))
    n_images = len(images)
    if titles is None: titles = ['Image (%d)' % i for i in range(1, n_images + 1)]
    fig = plt.figure()
    for n, (image, title) in enumerate(zip(images, titles)):
        a = fig.add_subplot(cols, np.ceil(n_images / float(cols)), n + 1)
        print("num dimensions: {}".format(image.ndim))
        if image.ndim == 2:
            plt.gray()
            plt.imshow(image, cmap='gray')
        else:
            converted = image
            if cv2ConvertTarget is not None:
                converted = cv2.cvtColor(image, cv2ConvertTarget)
            plt.imshow(converted)
        a.set_title(title, fontsize=24)
    size = np.array([6, 4]) * n_images * scale_factor
    fig.set_size_inches(size)
    plt.show()