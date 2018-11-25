# steganography
Steganography project for my cryptography class.

## Usage
To hide text within an image

```python3 encrypt.py path/to/image path/to/file/containing/message number_of_bits_to_use```

To recover a message

```python3 decrypt.py path/to/encrypted/image number_of_bits_to_use```

## Examples
Encrypt the wikipedia page for steganography with 3 bits in the cat image

```python3 encrypt.py cat_image.jpg wiki_steganography 3```

Decrypt the previous image

```python3 decrypt.py encrypted.png 3```
