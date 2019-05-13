from tkinter import *
import tkinter.messagebox
import webbrowser

myApp=Tk()
myApp.title("AutoCheckMyAnswer")


#*************Instruction Tab*************

instruction_frame=Frame(myApp)
instruction_frame.pack(side=TOP,fill=X,expand=1)
def showInstructions():
    webbrowser.open("instructions.txt")
instr_button=Button(instruction_frame,text="Instructions",width=15,height=10,fg="purple",bg="yellow",command=showInstructions)
instr_button.pack(side=LEFT,padx=10,pady=10,expand=True)

#*****************************************
#***********Secondary Window 1**************
def window_for_no_of_questions():
    #new window to enter no. of questions

    
    def confirm():                     #confirm button for upload
        students = entry_field.get()   #students stores no. of students
        print(students)
        def destroy_popups():
            popup.destroy()
            master.destroy()
        
        popup = Tk()
        popup.wm_title("!")
        
        B1 = Button(popup, text="Done !!",bg="green",fg="yellow", command = destroy_popups)
        B1.pack()
        popup.mainloop()
    
    #menu to enter no. of questions
    master=Tk()
    label=Label(master,text="Enter No.of Questions",fg="purple")
    label.grid(row=0,column=0,sticky=N+E+S+W)

    entry_field=Entry(master)
    entry_field.grid(row=0,column=1,sticky=N+E+S+W)

    entry_field.focus_set()
    
    entry_button = Button(master,text="Confirm",bg="green",fg="yellow",command=confirm)
    entry_button.grid(row=1,column=1,sticky=N+E+S+W)
    
    wait_label=Label(master,text="Please wait for 5-6 minutes a popup will appear after processing is finished")
    wait_label.grid(row=2,column=0,columnspan=2,sticky=N+E+S+W)

    master.mainloop()

#***********************************************************
#***********Secondary Window 2**************
def window_for_no_of_students():
    #new window to enter no. of questions

    
    def confirm():                     #confirm button for upload
        students = entry_field.get()   #students stores no. of students
        print(students)
        def destroy_popups():
            popup.destroy()
            master.destroy()
        
        popup = Tk()
        popup.wm_title("!")
        
        B1 = Button(popup, text="Done !!", bg="green",fg="yellow",command = destroy_popups)
        B1.pack()
        popup.mainloop()
    
    #menu to enter no. of questions
    master=Tk()
    label=Label(master,text="Enter No.of Students",fg="purple")
    label.grid(row=0,column=0,sticky=N+E+S+W)

    entry_field=Entry(master)
    entry_field.grid(row=0,column=1,sticky=N+E+S+W)

    entry_field.focus_set()
    
    entry_button = Button(master,text="Confirm",bg="green",fg="yellow",command=confirm)
    entry_button.grid(row=1,column=1,sticky=N+E+S+W)
    
    wait_label=Label(master,text="Please wait for 5-6 minutes a popup will appear after processing is finished")
    wait_label.grid(row=2,column=0,columnspan=2,sticky=N+E+S+W)

    master.mainloop()

#***********************************************************

firstFrame=Frame(myApp)
firstFrame.pack(fill=BOTH,expand=1)
# firstFrame.grid(row=0, column=0, sticky=N+S+E+W)
secondFrame=Frame(myApp)
secondFrame.pack(fill=BOTH,expand=1)
# secondFrame.grid(row=1, column=0, sticky=N+S+E+W)

for x in range(2):
    Grid.columnconfigure(firstFrame, x, weight=1)

for y in range(2):
    Grid.rowconfigure(firstFrame, y, weight=1)

for x in range(2):
    Grid.columnconfigure(secondFrame, x, weight=1)

for y in range(2):
    Grid.rowconfigure(secondFrame, y, weight=1)

button1=Button(firstFrame,text="Model Answers",width=15,height=10,fg="purple",bg="yellow",command=window_for_no_of_questions)
button1.grid(row=0,column=0,sticky=N+E+S+W)
# addButton(firstFrame,"Modal Answers",window_for_no_of_questions)
button2=Button(firstFrame,text="Students' Answers",width=15,height=10,fg="purple",bg="yellow",command=window_for_no_of_students)
button2.grid(row=0,column=1,sticky=N+E+S+W)
# addButton(firstFrame,"Students' Answers",window_for_no_of_students)
button3=Button(secondFrame,text="Evaluate",width=15,height=10,fg="purple",bg="yellow",command=window_for_no_of_questions)
button3.grid(row=1,column=0,sticky=N+E+S+W)
# addButton(secondFrame,"Evaluate",window_for_no_of_questions)
button4=Button(secondFrame,text="Results",width=15,height=10,fg="purple",bg="yellow",command=window_for_no_of_questions)
button4.grid(row=1,column=1,sticky=N+E+S+W)
# addButton(secondFrame,"Results",window_for_no_of_questions)

myApp.mainloop()