from PIL import Image

# input image
# the path has to be correct
frontPageImg = Image.open(r'./input.jpg')

frontPage = frontPageImg.convert('RGB')

# output pdf
# change the name of your pdf
frontPage.save(r'./input.pdf')
