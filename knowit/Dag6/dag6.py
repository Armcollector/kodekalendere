import imageio
import PIL
import numpy as np

im = imageio.imread(r'C:\git\kodekalendere\knowit\Dag6\mush.png')
orig_shape = im.shape
im = im.reshape(-1,3)

for i in range(len(im)-1,0,-1):
    im[i] = im[i]^im[i-1]

im = im.reshape(orig_shape)


PIL.Image.fromarray(c)