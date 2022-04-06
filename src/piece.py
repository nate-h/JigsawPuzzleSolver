import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from IPython.display import Image
from sklearn.cluster import KMeans
import PIL
import cv2 as cv
from scipy import ndimage, misc
import cv2


class Piece:
    def __init__(self, index, contour):

        self.index = index
        self.contour = contour

        # Calculate center, area, perimeter.
        M = cv2.moments(self.contour)
        self.area = M["m00"]
        self.cx = int(M["m10"] / self.area)
        self.cy = int(M["m01"] / self.area)
        self.arc_length = cv2.arcLength(self.contour, True)

        # Bounding box.
        self.x, self.y, self.w, self.h = cv2.boundingRect(self.contour)
        padding = 10
        self.x -= padding
        self.y -= padding
        self.w += 2 * padding
        self.h += 2 * padding

        # Min Rect.
        # rect = cv2.minAreaRect(cnt)
        # box = cv2.boxPoints(rect)
        # box = np.int0(box)
        # im = cv2.drawContours(im,[box],0,(0,0,255),2)

    def extract_images(self, labeled_pieces, grayScaleMasked, imgRGB):
        """Extract image of self."""
        self.imgRGB = imgRGB[self.y : self.y + self.h, self.x : self.x + self.w, :]
        self.image = labeled_pieces[
            self.y : self.y + self.h, self.x : self.x + self.w, :
        ]
        self.grayScaleMasked = grayScaleMasked[
            self.y : self.y + self.h, self.x : self.x + self.w
        ]

    @property
    def dims(self):
        return self.x, self.y, self.w, self.h

    def approxPoly(self, epsilon):
        pass
