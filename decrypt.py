#!/usr/bin/env python3

import sys
from PIL import Image
import numpy as np
args = sys.argv[1:]
image_path = args[0]
bits = int(args[1])



im = Image.open(image_path)
pixels = np.asarray(im)

binary_message = ""
for row in pixels:
    for pixel in row:
        for value in pixel:
            binary_value = bin(value)[2:]
            binary_value = binary_value.zfill(8)
            binary_message += binary_value[-bits:]

message = ""
for i in range(0, len(binary_message), 8):
    binary = binary_message[i:i+8]
    message += chr(int(binary,2))
    

print(message)


