import wget

height = input("How tall would you like the Picsum image to be?")
height = int(height)
while type(height) != int:
    height = input("The integer you inputted for the height was not a integer in digits. Please input the integer in digits as an integer.")

width = input("How wide would you like the Picsum image to be?")
while type(height) != int:
    width = input("The integer you inputted for the width was not a integer in digits. Please input the integer in digits as an integer.")

image_url = "https://picsum.photos/%s/%d/" % (width, height)
image_filename = wget.download(image_url)

print("Image successfully downloaded: ", image_filename)
print("Job done.")