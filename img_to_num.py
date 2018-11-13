from PIL import Image
import sys

def convert_base_10(array, base):
    n = 0
    for index, x in enumerate(reversed(array)):
        n += base**index * x

    return n

def get_sig_block(pixels):
    """Returns the block of values in a pixel list that
       are significant. This is all numbers until the array contains of 0
       [(0, 0, 0), (0, 0, 4), (5, 0, 0), (7, 0, 0), (0, 0, 0)] would return 
       [4, 5, 0, 0, 7, 0, 0, 0, 0, 0]"""

    
    number = []
    # The queue represents the 0's we've seen without seeing a non-zero number
    # we don't want to add the 0's that come before our number because that will
    # waste CPU time and memory. Also representing the number like 000000248432 feels weird
    queue = []
    # Iterate backwards through pixels
    for pixel in reversed(pixels):
        # Iterate backwards through each pixel
        for value in reversed(pixel):
            # If not 0 we put everything on the queue into the number
            # and then put the number on as well
            if value != 0:
                number.extend(queue)
                queue = []
                number.append(value)
            # If it is zero, we add it to the queue until we see a non zero number
            else:
                queue.append(value)

    return list(reversed(number))


path = sys.argv[1]

img = Image.open(path)

pixels = img.getdata()

print(convert_base_10(get_sig_block(pixels), 256))











