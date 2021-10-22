# For User arguments
import sys

# b64 Processing
import base64

# CLI Arguments
# eg: imgb64.py img.jpg
str(sys.argv)

with open(sys.argv[1], "rb") as imgjpg:
    imgb64 = base64.b64encode(imgjpg.read())
print(imgb64)