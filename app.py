import numpy as np
import cv2

# TODO: Separate stuff to be modular, because I'm fuckin' great at that shit, ey.

app_name = "m'app"
file_name = "test.png"
# TODO: Change this from trackbar. Maybe 1 trackbar per filter, I dunno. Or subwindows with more options.
# This is a stupid way to do it, but tutorials.
num_filters = 1

def dummy(value):
    pass

# Read in an  image, then make it grayscale
# TODO: File selecting
# TODO: Weighted average instead of straight average.
# Grayscale destroys information, so we need 2 copies of the image
color_original = cv2.imread(file_name)
gray_original = cv2.cvtColor(color_original, cv2.COLOR_BGR2GRAY)

# Create the UI; window and trackbars
cv2.namedWindow(app_name)

#
# TRACKBARS
#
# arguments: trackbarName, windowName, initValue, maxValue, onChangeHandler
cv2.createTrackbar('Contrast', app_name, 1, 100, dummy)
cv2.createTrackbar('Brightness', app_name, 50, 100, dummy)
cv2.createTrackbar('Grayscale', app_name, 0, 1, dummy) # TODO: Grayscale scaling 0-255?
cv2.createTrackbar("Filters", app_name, 0, num_filters, dummy)

#
# MAIN UI LOOP
#
while True:
    # TODO: Read all trackbar values
    grayscale = cv2.getTrackbarPos("Grayscale", app_name)
    # TODO: Apply filters
    # TODO: Apply brightness/contrast
    # TODO: Buttons to open/save/close
    # wait for keypress, this seems like a shit way, just use buttons at this point
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
    elif key == ord('s'):
        # TODO: Save image
        pass

    # Show image
    if grayscale:
        cv2.imshow(app_name, gray_original)
    else:
        cv2.imshow(app_name, color_original)
        
# window cleanup
cv2.destroyAllWindows()