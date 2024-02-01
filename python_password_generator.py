#1. Import the necessary modules, here are random and tkinter modules

import random   # To randomly generate a password we use this module. Random is a built-in module used to generate a random subset or a substring of a list, array or string. In our case, it will generate a random string containing characters from the original string.
from tkinter import messagebox  # In case the user fails to provide inputs, we must raise a prompt. Thus we use messagebox to raise such prompts.
from tkinter import *


# 2. Define Password generator function

def generate_password():  # Declaration of a function to generate a random password in python
  try:   # Read the user inputs, length and repeat from the entry widgets using get().
    repeat = int(repeat_entry.get())
    length = int(length_entry.get())
  except: # In case the user fails to enter both the inputs, the code will enter the except block and display an error prompt.
    messagebox.showerror(message="Please key in the required inputs") #  display the error message, which is set to the message variable. 
    return  # If the code enters the except block and to prevent the code after except block from executing, add a return statement

  #Check if user allows repetition of characters
  if repeat == 1: #  Checks if the user allows for repetition of characters in the password. 
    password = random.sample(character_string,length) # If repeat==1, then use sample for unique characters without repetition and choice if repetition is allowed. 
  else:
    password = random.choices(character_string,k=length)

  #Since the returned value is a list, we convert to a sting using join
  password=''.join(password)

  #Declare a string variable
  password_v = StringVar()
  password="Created password: "+str(password)

  #Assign the password to the declared string variables
  password_v.set(password)

  #Create a read only entry box to view the output, position using place
  password_label = Entry(password_gen, bd=0, bg="gray85", textvariable=password_v, state="readonly")
  password_label.place(x=10, y=140, height=50, width=320)


# 3. Define character string:

#Define a string containing letters, symbols and numbers
character_string = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"


#4. Define the user interface:

password_gen  = Tk()  # Invoke the class tkinter using Tk(). This contains provisions to handle user events and widgets.
password_gen.geometry("350x200") #  Define the dimensions of the frame of the application in the format lengthxbreadth
password_gen.title("Python Password Generator") # An optional parameter to set the title of the application.


# 5. Add input widgets

''' Use labels to add non-editable text of an application. '''

#Mention the title of the app
title_label = Label(password_gen, text="Python Password Generator", font=('Ubuntu Mono',12))
title_label.pack()  # Any widget or label will be visible only after positioning it on the window or screen of the app. 

#Read length 
length_label = Label(password_gen, text="Enter length of password: ")
length_label.place(x=20,y=30) # Any widget or label will be visible only after positioning it on the window or screen of the app. 
length_entry = Entry(password_gen, width=3) # To read user input, we use Entry widget
length_entry.place(x=190,y=30)  # Any widget or label will be visible only after positioning it on the window or screen of the app. 

#Read repetition
repeat_label = Label(password_gen, text="Repetition? 1: no repetition, 2: otherwise: ")
repeat_label.place(x=20,y=60) # Any widget or label will be visible only after positioning it on the window or screen of the app. 
repeat_entry = Entry(password_gen, width=3) # To read user input, we use Entry widget
repeat_entry.place(x=300,y=60)  # Any widget or label will be visible only after positioning it on the window or screen of the app. 


# 6. Button to call the translate function:

#Generate password
password_button = Button(password_gen, text="Generate Password", command=generate_password)
password_button.place(x=100,y=100)

#Exit and close the app
password_gen.mainloop()