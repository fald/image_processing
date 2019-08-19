import numpy as np
import cv2

# TODO: Separate stuff to be modular, because I'm fuckin' great at that shit, ey.

app_name = "m'app"
# TODO: Change this from trackbar. Maybe 1 trackbar per filter, I dunno. Or subwindows with more options.
# This is a stupid way to do it, but tutorials.
num_filters = 1

def dummy(value):
    pass

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
        

cv2.waitKey(0)
# window cleanup
cv2.destroyAllWindows()