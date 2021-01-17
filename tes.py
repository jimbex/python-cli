# adds image processing capabilities
from PIL import Image
# will convert the image to text string
import pytesseract as pt
# assigning an image from the source path
img = Image.open('image test.jpeg')
# converts the image to result and saves it into result variable
result = pt.image_to_string(img)
print(result)