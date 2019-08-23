import numpy as np
import cv2

# TODO: Separate stuff to be modular, because I'm fuckin' great at that shit, ey.

app_name = "m'app"
file_name = "test.png"

# Save count; should probably do it so it saves based on active filters and their values, though...but following tutorial for now.
count = 1

def dummy(value):
    pass

# TODO: Change this from trackbar. Maybe 1 trackbar per filter, I dunno. Or subwindows with more options.
# This is a stupid way to do it, but tutorials.
# Define our convolution kernels.
# Identity, doesn't change anything at all.
identity_kernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
# A 5 surrounded by -1s; most weight on anchor point, less weight on surrounding.
sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
gaussian_kernel_1 = cv2.getGaussianKernel(3, 0)
gaussian_kernel_2 = cv2.getGaussianKernel(9, 0)
# Averaging kernel, this is actually good for me...maybe. These filters are actually fairly bad.
box_size = 715
box_kernel = np.ones((box_size, box_size), dtype=np.float32) / float(box_size ** 2)

kernels = [identity_kernel, sharpen_kernel, gaussian_kernel_1, gaussian_kernel_2, box_kernel]

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
cv2.createTrackbar("Filters", app_name, 0, len(kernels) - 1, dummy)
#
# MAIN UI LOOP
#
while True:
    grayscale = cv2.getTrackbarPos("Grayscale", app_name)
    contrast = cv2.getTrackbarPos("Contrast", app_name)
    brightness = cv2.getTrackbarPos("Brightness", app_name)
    # filters = cv2.getTrackbarPos("Filters", app_name)
    kernel_index = cv2.getTrackbarPos('Filters', app_name)
    # TODO: Apply filters
    color_modified = cv2.filter2D(color_original, -1, kernels[kernel_index])
    gray_modified = cv2.filter2D(gray_original, -1, kernels[kernel_index])
    # addWeighted needs a second useless image, for some reason.
    # The way this is working is we're adding the original to a dummy, then scaling it; its the
    # scaling that does the brightness, so no need for a second image, but the method in cv2 still
    # requires it.
    # Remember to take into account brightness starting at 50 on the tackbar.
    # color_modified = cv2.addWeighted(color_original, contrast, np.zeros_like(color_original), 0, brightness - 50)
    # gray_modified = cv2.addWeighted(gray_original, contrast, np.zeros_like(gray_original), 0, brightness - 50)
    color_modified = cv2.addWeighted(color_modified, contrast, np.zeros_like(color_original), 0, brightness - 50)
    gray_modified = cv2.addWeighted(gray_modified, contrast, np.zeros_like(gray_original), 0, brightness - 50)
    # TODO: Buttons to open/save/close

    # wait for keypress, this seems like a shit way, just use buttons at this point
    key = cv2.waitKey(10)
    if key == ord('q'):
        break
    elif key == ord('s'):
        save = gray_modified if grayscale else color_modified
        cv2.imwrite('output-{}.png'.format(count), save)
        count += 1

    # Show image
    if grayscale:
        cv2.imshow(app_name, gray_modified)
    else:
        cv2.imshow(app_name, color_modified)
        
# window cleanup
cv2.destroyAllWindows()