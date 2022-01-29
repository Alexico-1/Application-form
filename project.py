from cgitb import text
from distutils import command
from sqlite3 import Row
from tkinter import *
root = Tk()
def getvals():
    print("Accepted")
    

root.geometry("500x300")
#Heading
Label(root, text="Registration Form", font="ar 15 bold").grid(row=0, column=3)
#Field Name
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")
paymentmode = Label(root, text="Payment Mode")

#Packing field
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

#Variable for storing Data
namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
paymentmodevalue = StringVar
checkvalue = IntVar

#Creating entry field
nameentry = Entry(root, textvariable = namevalue)
phoneentry = Entry(root, textvariable = phonevalue)
genderentry = Entry(root, textvariable = gendervalue)
paymentmodeentry = Entry(root, textvariable = paymentmodevalue)
emergencyentry = Entry(root, textvariable = emergencyvalue)

#Packing entry field (for the above to appear on our form in grid)
nameentry.grid(row=1, column= 3)
phoneentry.grid(row=2, column= 3)
genderentry.grid(row=3, column= 3)
emergencyentry.grid(row=4, column= 3)
paymentmodeentry.grid(row=5, column= 3)

#Creating Checkbox
checkbtn = Checkbutton(text='remember me?', variable = checkvalue)
checkbtn.grid(row=6, column=3)

# SUbmit button
Button(text="Submit", command=getvals).grid(row=7, column=3)


root.mainloop()