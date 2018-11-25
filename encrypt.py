#!/usr/bin/env python3

from PIL import Image
import numpy as np
import sys


args = sys.argv [1:]

image_path = args[0]

message_path = args[1]
message = ""
with open(message_path) as f:
    message = f.read()

bits = int(args[2])

binary_message = ""

for char in message:
    ascii_value = ord(char)
    binary_char = bin(ascii_value)[2:]
    if len(binary_char) <= 8:
        binary_char = binary_char.zfill(8)
        binary_message += binary_char

im = Image.open(image_path)
pixels = np.asarray(im)
pixels.flags.writeable = True

for ri, row in enumerate(pixels):
    for pi, pixel in enumerate(row):
        for vi, value in enumerate(pixel):
            if binary_message == "":
                break
            binary_value = bin(value)
            binary_value = binary_value[:-bits] + binary_message[:bits]
            int_value = int(binary_value,2)
            pixels[ri][pi][vi] = int_value
            binary_message = binary_message[bits:]


encrypted = Image.fromarray(pixels)
encrypted.save("encrypted.png")
            



