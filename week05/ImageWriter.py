import cv2
import random
import sys


class IWimage():
    def __init__(self, fn, p):
        self.filename = fn
        self.windowname = fn+str(random.randint(1, 10))
        self.picShown = False
        self.pic = p
        self.height = 0
        self.width = 0
        self.error = True
        if type(p) != type(None):
            self.error = False
            self.height, self.width, _ = p.shape
##
# This function loads the image name passed in.
# The function will pass back a reference to the
# picture which needs to be stored for any future processing.
# This function will not show the image


def loadPicture(filename):

    pic = IWimage(filename, cv2.imread(filename, cv2.IMREAD_COLOR))
    if pic.error:
        print(f"Error: Could not open {filename}", file=sys.stderr)
        return None
    return pic

##
# This function shows the image passed in as parameter.


def showPicture(pic):
    if pic == None or type(pic.pic) == type(None):
        return
    cv2.imshow(pic.windowname, pic.pic)
    cv2.waitKey(1)

##
# This function shows the image passed in as parameter.


def updatePicture(pic):
    if pic == None or type(pic.pic) == type(None):
        return
    cv2.imshow(pic.windowname, pic.pic)
    cv2.waitKey(1)

##
# This function returns the width of the picture as an integer.


def getWidth(pic):
    if pic == None:
        return 0
    return pic.width

##
# This function returns the height of the picture as an integer.


def getHeight(pic):
    if pic == None:
        return 0
    return pic.height


##
# This function returns the color at location x, y of the picture.
# The color is returned as a list of three values
# representing the red, green, and blue component of the color.
def getColor(pic, x, y):
    if pic == None or type(pic.pic) == type(None):
        return None
    if getHeight(pic) > y and getWidth(pic) > x:
        cl = pic.pic[y][x]
        return [int(cl[2]), int(cl[1]), int(cl[0])]
    else:
        return None
##
# Sets the color of the location x, y to color passed in.
# The color is a list of three elements representing the
# red, green, and blue component of the color


def setColor(pic, x, y, col):
    if pic == None or type(pic.pic) == type(None):
        return
    if (len(col) == 3 and 0 <= col[0] <= 255
        and 0 <= col[1] <= 255 and 0 <= col[2] <= 255
            and getWidth(pic) > x and getHeight(pic) > y):
        pic.pic[y][x] = [col[2], col[1], col[0]]


##
# This function will save the picture passed in as a file
# using the name passed in the variable filename.
# Make sure that the string filename has the proper
# file extension for an image. File names can have
# extensions "gif", "jpg", "bmp".
def savePicture(pic, filename):
    if pic == None or type(pic.pic) == type(None):
        return
    cv2.imwrite(filename, pic.pic)

##
# This function closes the window. This is important for
# clean up at the end of working with an image.


def closeWindow(pic):
    if pic == None or type(pic.pic) == type(None):
        return
    cv2.destroyWindow(pic.windowname)
