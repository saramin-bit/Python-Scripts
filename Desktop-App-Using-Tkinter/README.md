## What is Tkinter?
Tkinter is the standard GUI library for Python. Python when combined with Tkinter provides a fast and easy way to create GUI applications. Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

## Steps to develop a desktop app using Python Tkinter

1.  Import tkinter- Creating a window
```
import tkinter as tk
```
2. Creating a window
```
root = tk.Tk()
root.title("Desktop Application")
root.geometry("750x500")
```
3. Creating a label
```
label = tk.Label(root, width=22, text="Addition of two numbers", anchor='w')
label.config(font=("Raleway",16))
label.pack(side=tk.TOP, pady = 30)
```
4. Creating  entry text fields
```
row = tk.Frame(root)
label = tk.Label(row, width=22, text="Number 1", anchor='w')
label.config(font=("Raleway",16))
 
validation = row.register(only_numbers)
number1 = tk.Entry(row, validate="key", validatecommand=(validation, %S'))
number1.config(font=("Raleway",16))
 
row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
label.pack(side=tk.LEFT)
number1.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
 
row2 = tk.Frame(root)
label2 = tk.Label(row2, width=22, text="Number 2", anchor='w')
label2.config(font=("Raleway",16))
validation = row2.register(only_numbers)
number2 = tk.Entry(row2, validate="key", 
validatecommand=(validation, '%S'))
number2.config(font=("Raleway",16))
 
row2.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
label2.pack(side=tk.LEFT)
number2.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
```
5. Adding a function for input validation
```
def only_numbers(char):
 return char.replace(".", "0", 1).isdigit()
```
6. Adding a button for addition
```
b1 = tk.Button(root, width = 15, text='Add', background = "Light green", command=(lambda: add_val()))
b1.config(font=("Raleway", 18))   
b1.pack(side=tk.RIGHT, padx=5, pady=5)
```

7.  Adding a function for finding sum
```
def add_val():
 added_val = int(number1.get()) +  int(number2.get())
 label3 = tk.Label(root, width=60, text =  "SUM " + str(added_val), anchor = 'w')
 label3.config(font=("Raleway",18))
 label3.pack(side=tk.LEFT, padx=150, ipady = 100)
```


