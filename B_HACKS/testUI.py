from tkinter import *
# import tkinter.messagebox
root=Tk()

# root.title('Name')
num_que=Button(root,text="Number of Questions")
num_que.pack(side=TOP)

#*********************
# def enterNumQ():
#     tkinter.messagebox.showinfo("Enter Data","Enter number of Questions to be checked")
#     answer=tkinter.messagebox.askquestion("Question 1","Do you like me?")
#     if answer=="yes":
#         print("Aww I knew it would be a yes")
#*********************
label=Label(root,text="Enter number of Questions to be checked")
label.pack(fill=X)

e = Entry(root)
e.pack()
e.focus_set()

b = Button(root,text='Submit')
b.pack(side=BOTTOM)


root.mainloop()