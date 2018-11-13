from PIL import Image
import sys, argparse

parser = argparse.ArgumentParser(description="Turn a number into an image. Number must be less than 256^(width * height * 3) - 1")
parser.add_argument("--n", required=True, type=int)
parser.add_argument("--imgout", required=True, metavar="/path/to/image.xxx", type=str)
parser.add_argument("--width", required=True, type=int)
parser.add_argument("--height", required=True, type=int)
args = parser.parse_args()

N = args.n



# Size of image in normal dimensions (width, height)
IMAGE_SIZE = (args.width, args.height)
# Size of image in a 1-D array which is width * hight * 3
# * 3 because each color channel needs its own spot
IMAGE_LENGTH = IMAGE_SIZE[0] * IMAGE_SIZE[1] * 3

if N > 256**(IMAGE_LENGTH)-1:
    raise Exception("Number too large for image of this size")

def remainder_division(n, divisor):
    return (n//divisor, n % divisor)


def base_conversion(n, base):
    tmp = n
    array = []
    while tmp >= base:
        tmp, remainder = remainder_division(tmp, base)
        array.insert(0, remainder)
    array.insert(0, tmp)
    return array

def group_pixels(array):
    if len(array) % 3 != 0:
        raise Exception("Array not groupable. Length must be a multiple of 3")
    new_array = []
    for x in range(0,len(array),3):
        new_array.append((array[x], array[x+1], array[x+2]))

    return new_array




base256 = base_conversion(N, 256)


data = [0] * (IMAGE_LENGTH - len(base256))
data.extend(base256)

grouped = group_pixels(data)

img = Image.new("RGB", IMAGE_SIZE)

img.putdata(grouped)

img.save(args.imgout)



