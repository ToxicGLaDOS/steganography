#!/usr/bin/env python3

import sys
from PIL import Image
import numpy as np

# Get command line arguments
args = sys.argv[1:]
image_path = args[0]
bits = int(args[1])


# Open the image passed in
im = Image.open(image_path)
# Open the image as a 3-d array of pixels
pixels = np.asarray(im)

binary_message = ""
# Iterate through the rows of pixels, the pixels themselves, then each channel
for row in pixels:
    for pixel in row:
        for value in pixel:
            # Turn to a binary string and peel off the '0b' part
            binary_value = bin(value)[2:]
            # Fill it with 0's to make sure it's a 8 bit number
            binary_value = binary_value.zfill(8)
            # Add the last bits to message
            binary_message += binary_value[-bits:]

message = ""
# Iterate through the binary 8 at a time
for i in range(0, len(binary_message), 8):
    # Grab the 8 binary digits
    binary = binary_message[i:i+8]
    # Turn those 8 digits into a base-10 number then into the corresponding ascii character
    message += chr(int(binary,2))
    

print(message)


