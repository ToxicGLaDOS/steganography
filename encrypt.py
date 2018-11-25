#!/usr/bin/env python3

from PIL import Image
import numpy as np
import sys

# Get command line arguments
args = sys.argv [1:]

image_path = args[0]

message_path = args[1]
message = ""

# Open the file that is passed in
with open(message_path) as f:
    message = f.read()

bits = int(args[2])

binary_message = ""

# Iterate through the characters in the message we want to hide
for char in message:
    # Turn each character into it's base-10 ascii value
    ascii_value = ord(char)
    # Turn that base-10 int into a binary string with the '0b' pulled off
    binary_char = bin(ascii_value)[2:]
    # If the character is outside of ascii we ignore it
    if len(binary_char) <= 8:
        # Fill the binary with zeros to the left to ensure it's an 8-bit number '1001' -> '00001001'
        binary_char = binary_char.zfill(8)
        # Add that 8-bit binary number to the binary_message
        binary_message += binary_char
# Open the image
im = Image.open(image_path)
# Open the image as a 3-d array of pixels
pixels = np.asarray(im)
# Make the array writable
pixels.flags.writeable = True

# Iterate through the rows, then each pixel in each row, and then each channel in each pixel
for ri, row in enumerate(pixels):
    for pi, pixel in enumerate(row):
        for vi, value in enumerate(pixel):
            # We can stop once the binary has been fully encoded
            if binary_message == "":
                break
            # Turn the channel value into a binary number
            binary_value = bin(value)
            # Change the last bits of the value into the bits we want to encode
            binary_value = binary_value[:-bits] + binary_message[:bits]
            # Turn the now changed number back into a base-10 int
            int_value = int(binary_value,2)
            # Overwrite the old value of that channel
            pixels[ri][pi][vi] = int_value
            # Pull off the first bits of the message we want to encode
            binary_message = binary_message[bits:]

# Save the updated 3-d array as an image
encrypted = Image.fromarray(pixels)
encrypted.save("encrypted.png")
            



