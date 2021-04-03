import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from IPython.display import Image
from sklearn.cluster import KMeans
import  PIL
import cv2 as cv
from scipy import ndimage, misc
import cv2

from puzzle_piece import PuzzlePiece

class Puzzle:
    def __init__(self, image_path):
        self.image_path = image_path
        self.contoured_image = None
        self.image = cv.imread(self.image_path)
        self.hsv = cv.cvtColor(self.image, cv.COLOR_BGR2HSV)

    # Elegantly extract useful functions.
    # def help_find_green_screen(self):
    #     pass

    def create_pieces(self, contoured_image, contours):

        self.contoured_image = contoured_image
        self.labeled_pieces = np.copy(self.contoured_image)
        self.contours = contours

        # Initialize pieces.
        self.pieces = [PuzzlePiece(i, c) for i, c in enumerate(self.contours)]

        # Label pieces on image.
        for piece in self.pieces:
            cx, cy = piece.cx, piece.cy
            cv2.putText(self.labeled_pieces, text= str(piece.index), org=(cx-20,cy+10),
                fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=0.8, color=(255, 0, 255),
                thickness=2, lineType=cv2.LINE_AA)

        # Let pieces extract images of them self.
        for piece in self.pieces:
            piece.extract_image(self.labeled_pieces)



    def solve(self):
        pass