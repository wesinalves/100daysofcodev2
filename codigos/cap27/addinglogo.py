# Python Journey - Chapter 27
# Adding logo to a image

# Resizes all images in current working directory to fit
# in a 300x300 square, and adds hope.png to the lower-right corner.

import os
from PIL import Image

SQUARE_FIT_SIZE = 300
dir = input("directory of the photos? ")
LOGO_FILENAME = input("filename of the logo ")

logo_image = Image.open(os.path.join(dir,LOGO_FILENAME))
logo_image = logo_image.resize((30,15))
logo_width, logo_height = logo_image.size

# Loop over all files in the working directory.

os.makedirs(os.path.join(dir,'withlogo'), exist_ok=True)
for filename in os.listdir(dir):
    if not (filename.endswith('.png') or filename.endswith('.JPG')) or filename == LOGO_FILENAME:
        continue
    
    im = Image.open(os.path.join(dir,filename))
    width, height = im.size

    # Check if image needs to be resized.

    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        
        # Resize the image.
        print("resizing %s..." % (filename))
        im = im.resize((width,height))

    # Add the logo.
    print("adding the logo to %s..." % (filename))
    im.paste(logo_image, (width - logo_width, height - logo_height), logo_image)

    # Save changes.
    im.save(os.path.join(dir,'withlogo', filename))


