from tkinter import *
import random 

root = Tk()
root.title("Password generator")
root.geometry("500x500")

label = Label(root)

array3d = [[[1,2,3,4,5,6], ["Head", "Tail"], ["A", "B", "C", "D", "E", "F", "G", "H"]]]
print(array3d[0][1][1])

def newpassword():
    random_number_1 = random.randint(0,5)
    random_number_2 = random.randint(0,1)
    random_number_3 = random.randint(0,7)
    
    letter_1 = str(array3d[0][0][random_number_1])
    letter_2 = array3d[0][1][random_number_2]
    letter_3 = array3d[0][2][random_number_3]
    label["text"] = letter_1 + "" + letter_2 + "" + letter_3

btn = Button(root, text = "Generate New password!", command=newpassword)
btn.place(relx = 0.5, rely = 0.5, anchor=CENTER)

label.place(relx = 0.5, rely = 0.6, anchor=CENTER)

root.mainloop()