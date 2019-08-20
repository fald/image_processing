#   image processing
#   Image filters a-la instagram or whatever I come up with
#   Also I have 0 experience with image filters, so maybe it won't
#   be that creative or interesting, but its new to me.

# Filter ideas:
#   Pixelating; take average color over area and make a 'low res' image
#   Bubbling: Pixelating, but rounded
#   Random Pix/Bub: Randomize size and position of bubbles

# Learning goals:
#   Matrices
#   Color models
#   Brightness/Contrast
#   Convolution
#   OpenCV UI

# Tutorial uses spyder, woo.
# Did some convolution examples; no code to show for it, but had to do with code, so its being marked for my git spree >=(

# Ex: Image = [[0,0,0], [0,0,0], [255,255,255], [255,255,255]], Kernel=[[1,2,1],[0,0,0],[-1,-2,-1]], pad image for edges, apply kernel
# end up with [[0,0,0], [-1020, -1020, -1020], [-1020, -1020, -1020], [0,0,0]] => hard edge in middle