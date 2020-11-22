from PIL import Image

ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']
ascii_width = 100
img_path = '/home/code/myImg/sample4.jpg'
output_path = 'output.txt'

# open the image
image = Image.open(img_path)

# resize the image
width, height = image.size
ratio = height / width
ratio /= 1.85 # some font correction
ascii_height = int(ratio * ascii_width)
resized_image = image.resize((ascii_width, ascii_height))

# make the image grayscale
gray_image = resized_image.convert('L')

# get the pixels
pixels = gray_image.getdata()

# now make it ASCII!
factor = 255 / (len(ascii_chars)-1)
ascii_image_data = ''.join([ascii_chars[int(pixel/factor)] for pixel in pixels])

# format in given aspect ratio
pixel_count = len(ascii_image_data)
ascii_image = '\n'.join(ascii_image_data[i:(i+ascii_width)] for i in range(0, pixel_count, ascii_width))

# It is DONE!
print('DONE!')

# save the image
with open(output_path, 'w') as f:
    f.write(ascii_image)
