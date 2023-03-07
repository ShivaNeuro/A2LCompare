# import all components
# from the tkinter library
from A2LCompare import DiffCreator
from tkinter import *
import tkinter
import time
  
# import filedialog module
from tkinter import filedialog
  
# Function for opening the
# file explorer window

FileNames = []

def SelectA2L_File1():
    global FileNames
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.a2l*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer1.configure(text="A2LFile1: "+filename)
    FileNames.append(filename)

def SelectA2L_File2():
    global FileNames
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.a2l*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer2.configure(text="A2LFile2: "+filename)
    FileNames.append(filename)



def Compare():
    Diff = DiffCreator(FileNames[0],FileNames[1],'a2l')
    html_file = open('A2L_Compare_Report.html','w')
    html_file.write('Newly Added Variables'+'<br />')
    for i in Diff.NewVar():
        message = i
        html_file.write(message+"<br />")
    html_file.write("<br />")
    html_file.write("<br />")
    html_file.write('Removed Variables'+'<br />')
    for j in Diff.OldVar():
        message = j
        html_file.write(message+"<br />")
    html_file.close()
    time.sleep(10)
    tkinter.Label(window,text = 'Completed Comparision of A2L Files',fg='Green').grid(row = 4, column = 0)
    tkinter.Label(window,text = 'HTML Report Generated',fg='Green').grid(row = 5, column = 0) 
                                                                                                  
# Create the root window
window = Tk()
  
# Set window title
window.title('A2L_CAN_Compare')
  
# Set window size
window.geometry("800x300")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer1 = Label(window,
                            text = "",
                            width = 100, height = 4,
                            fg = "blue")

label_file_explorer2 = Label(window,
                            text = "",
                            width = 100, height = 4,
                            fg = "blue")  
      
button_explore1 = Button(window,
                        text = "Browse A2L_File1",
                        command = SelectA2L_File1)

button_explore2 = Button(window,
                        text = "Browse A2L_File2",
                        command = SelectA2L_File2)


button_compare = Button(window,
                        text = "Compare",
                        command = Compare)
  
button_exit = Button(window,
                     text = "Exit",
                     command = exit)
  

label_file_explorer1.grid(column = 1, row = 2)
label_file_explorer2.grid(column = 1, row = 3)  
button_explore1.grid(column = 0, row = 2)
button_explore2.grid(column = 0, row = 3)
button_compare.grid(column = 1, row = 4)
button_exit.grid(column = 1,row = 5)

              

  
# Let the window wait for any events
window.mainloop()
