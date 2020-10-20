import tkinter as T
from tkinter import *
from PIL import ImageTk, Image 
from tkinter import filedialog 
from pickle import load
import numpy as np
import matplotlib.pyplot as plt
import argparse
import pyttsx3
import warnings
import cv2
from matplotlib import cm

window = Tk()
window.title("Photo Editor")
window.geometry("1000x600")
window.configure(bg="mint cream")
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=4)
window.rowconfigure(2, weight=4)
window.rowconfigure(3, weight=1)
window.columnconfigure(1, weight=1)


def openfilename(): 
	filename = filedialog.askopenfilename(title ='Choose Image') 
	return filename 

def open_img(): 
	x = openfilename() 
	global image
	img_path = x
	img = Image.open(x) 
	img = img.resize((200, 200), Image.ANTIALIAS) 
	img = ImageTk.PhotoImage(img) 
	panel = Label(window, image = img) 
	panel.image = img 
	panel.grid(row = 1, column=1,sticky="ns")
	image = cv2.imread(img_path)
	
def canny_edge():
	thresholdval1 = 50
	thresholdval2 = 100
	canny = cv2.Canny(image, thresholdval1, thresholdval2)
	updateImage(canny)
	
def median_blur():
	matrix = 3
	blur = cv2.medianBlur(image, matrix)
	updateImage(blur)

def gaussian_blur():
	matrix = (7,7)
	blur = cv2.GaussianBlur(image, matrix,0)
	updateImage(blur)

def bilateral_blur():
	dimpixel = 7
	color = 100
	space = 100
	filter = cv2.bilateralFilter(image,dimpixel,color,space)
	updateImage(filter)
	
def thresholding():
	threshold_value = 100
	(T_value,binary_threshold) = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
	updateImage(binary_threshold)

def updateImage(update_image):
	PIL_image = Image.fromarray(np.uint8(update_image)).convert('RGB')
	im = PIL_image.resize((200, 200), Image.ANTIALIAS) 
	im = ImageTk.PhotoImage(im) 
	panel = Label(window, image = im) 
	panel.image = im 
	panel.grid(row = 1, column=1,sticky="ns")

#Buttons
fr_buttons = T.Frame(window,bd=2,bg="mint cream")
btn_choose = T.Button(fr_buttons, text="Choose Image", bg="peach puff", command = open_img)

btn_thresh = T.Button(fr_buttons, text="Thresholding", bg="peach puff",command = thresholding)
btn_median_blur = T.Button(fr_buttons, text="Median Blur", bg="peach puff",command = median_blur)
btn_gaussian_blur = T.Button(fr_buttons, text="Gaussian Blur", bg="peach puff",command = gaussian_blur)
btn_canny = T.Button(fr_buttons, text="Canny Edge Detector", bg="peach puff",command = canny_edge)
btn_bilateral = T.Button(fr_buttons, text="Bilateral Blur", bg="peach puff",command = bilateral_blur)

btn_choose.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_thresh.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_median_blur.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_gaussian_blur.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_canny.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btn_bilateral.grid(row=5, column=0, sticky="ew", padx=5, pady=5)

fr_buttons.grid(row=1, column=0, sticky="ns")

#Main Content
fr_main = T.Frame(window, bd=2,bg="mint cream")
lbl1 = Label(fr_main, text="Simple Photo Editor", bg="mint cream", fg="black", font="none 16 italic")
lbl1.grid(row=0, column=1,sticky="ew")
fr_main.grid(row=0,column=1,sticky="ns")


#Footer
fr_foot = T.Frame(window, bd=2,bg="mint cream")
lbl2 = Label(fr_foot, text="Developed by Harika B V",bg="mint cream", fg="gray25", font="oxygen 10 bold")
lbl2.grid(row=0, column=1,sticky="ew")

fr_foot.grid(row=3,column=1,sticky="ns")

window.mainloop()
