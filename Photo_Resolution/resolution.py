def jpeg_res(filename):                                #This function prints the resolution of the jpeg image file passed into it

  
   
   with open(filename,'rb') as img_file:                # open image for reading in binary mode

       
       img_file.seek(163)                               # height of image (in 2 bytes) is at 164th position

      
       a = img_file.read(2)                              # read the 2 bytes

      
       height = (a[0] << 8) + a[1]                         # calculate height

       
       a = img_file.read(2)                           # next 2 bytes is width

      
       width = (a[0] << 8) + a[1]                       # calculate width
       
       

   print("The resolution of the image is",width,"x",height)

jpeg_res("img1.jpg")
