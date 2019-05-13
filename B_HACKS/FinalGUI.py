################################################################### GUI #######################################################################

from tkinter import *
import tkinter.messagebox
import webbrowser
myApp=Tk()
myApp.title("AutoCheckMyAnswer")
#****************************************
def result():
    import matplotlib
    matplotlib.use('TkAgg')
    import numpy as np
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
    import tkinter

    root=Tk()
    root.title("Results")

    f=open("eval.txt","r")
    line=[]
    line.append(f.readline())
    while line[len(line)-1]:
        line[len(line)-1]=line[len(line)-1].split(" ")
        line.append(f.readline())
    print(line)
    f.close()

    from prettytable import PrettyTable

    head=[" "]
    for j in range(len(line)):
        for i in range(len(line[j])):
            head.append("Que "+str(i+1))

    t=PrettyTable(head)

    line_new=[]
    for i in range(len(line[0])):
        line_new.append(["Student "+str(i+1)])
        
    for i in range(len(line)):
        for j in range(len(line[i])):
                line_new[j].append(line[i][j])
    # print(line_new)

    for i in line_new:
        t.add_row(i)
    # print (t)

    label=Label(root,text=t)
    label.config(font=("Courier", 44))
    label.pack()

    root.mainloop()
#*****************************************
def window_for_exit():

    def yes_delete_everything():                  
        #code for exit
        myApp.destroy()
        master.destroy()
    def no_exit():
        myApp.destroy()
        master.destroy()

    master=Tk()
    master.title(" ")
    option_label = Label(master,text="Do You Want To exit deleting all the data ?",bg="green",fg="yellow")
    option_label.config(font=("Helvetica",17))
    option_label.grid(row=0,column=0,columnspan=2,sticky=N+E+S+W)
    
    yes_button=Button(master,text="Yes",command=yes_delete_everything)
    yes_button.config(font=("Helvetica",14))
    yes_button.grid(row=2,column=0,sticky=N+E+S+W)

    no_button=Button(master,text="NO",command=no_exit)
    no_button.config(font=("Helvetica",14))
    no_button.grid(row=2,column=1,sticky=N+E+S+W)
    

    master.mainloop()

#***********Secondary Window 1**************
def window_for_no_of_questions():
    #new window to enter no. of questions
    global no_of_questions
    # global students
    
    def confirm():                     #confirm button for upload
        global no_of_questions
        
        question = entry_field.get()
        no_of_questions=int(question)
        # model_things()   #students stores no. of students
        print(no_of_questions)
        def destroy_popups():
            popup.destroy()
            master.destroy()
        
        popup = Tk()
        popup.wm_title(" ")
        
        B1 = Button(popup, text="Done !!",bg="green",fg="yellow", command = destroy_popups)
        B1.config(font=("Helvetica",14))
        B1.pack(padx=50,pady=50)
        popup.mainloop()
    
    #menu to enter no. of questions
    master=Tk()
    master.title(" ")
    label=Label(master,text="Enter No.of Questions",fg="purple")
    label.config(font=("Helvetica", 17))
    label.grid(row=0,column=0,sticky=N+E+S+W)

    entry_field=Entry(master)
    entry_field.config(font=("Helvetica", 17))
    entry_field.grid(row=0,column=1,sticky=N+E+S+W)

    entry_field.focus_set()
    
    entry_button = Button(master,text="Confirm",bg="green",fg="yellow",command=confirm)
    entry_button.config(font=("Helvetica", 17))
    entry_button.grid(row=1,column=1,sticky=N+E+S+W)
    
    wait_label=Label(master,text="Please wait for 5-6 minutes a popup will appear after processing is finished",fg="blue")
    wait_label.config(font=("Helvetica", 14))
    wait_label.grid(row=2,column=0,columnspan=2,sticky=N+E+S+W)

    master.mainloop()

#***********************************************************

def window_for_evaluate():

    global no_of_questions
    global no_of_students
    # print(no_of_questions)
    # print(no_of_students)
    def confirm():                  
        global no_of_questions
        global no_of_students
        generatescore()
        def destroy_popups():
            popup.destroy()
            master.destroy()
        
        popup = Tk()
        popup.wm_title(" ")
        
        B1 = Button(popup, text="Done !!",bg="green",fg="yellow", command = destroy_popups)
        B1.config(font=("Helvetica",14))
        B1.pack(padx=50,pady=50)
        popup.mainloop()

    master=Tk()
    master.title(" ")
    entry_button = Button(master,text="Generate Students Score",bg="green",fg="yellow",command=confirm)
    entry_button.config(font=("Helvetica", 17))
    entry_button.grid(row=0,column=0,columnspan=2,sticky=N+E+S+W)
    
    wait_label=Label(master,text="Please wait for 5-6 minutes a popup will appear after Evaluation is finished")
    wait_label.config(font=("Helvetica", 17))
    wait_label.grid(row=1,column=0,columnspan=2,sticky=N+E+S+W)

    master.mainloop()

#***********Secondary Window 2******************************
def window_for_no_of_students():
    #new window to enter no. of students
    global no_of_questions
    global no_of_students
    
    def confirm():                     #confirm button for upload
        student = entry1_field.get()   #students stores no. of students
        # print(students)
        global no_of_questions
        global no_of_students
        no_of_students=int(student)
    
        # print(nstud)
        # student_things()
        # print(type(nstud),nstud+3)
        def destroy_popups():
            popup1.destroy()
            master1.destroy()
        
        popup1 = Tk()
        popup1.wm_title(" ")
        
        B2 = Button(popup1, text="Done !!", bg="green",fg="yellow",command = destroy_popups)
        B2.config(font=("Helvetica",14))
        B2.pack(padx=50,pady=50)
        popup1.mainloop()
    
    #menu to enter no. of questions
    master1=Tk()
    label1=Label(master1,text="Enter No.of Students",fg="purple")
    label1.config(font=("Helvetica",17))
    label1.grid(row=0,column=0,sticky=N+E+S+W)

    entry1_field=Entry(master1)
    entry1_field.config(font=("Helvetica",17))
    entry1_field.grid(row=0,column=1,sticky=N+E+S+W)

    entry1_field.focus_set()
    
    entry1_button = Button(master1,text="Confirm",bg="green",fg="yellow",command=confirm)
    entry1_button.config(font=("Helvetica",17))
    entry1_button.grid(row=1,column=1,sticky=N+E+S+W)
    
    wait_label1=Label(master1,text="Please wait for 5-6 minutes a popup will appear after processing is finished")
    wait_label1.config(font=("Helvetica",14))
    wait_label1.grid(row=2,column=0,columnspan=2,sticky=N+E+S+W)

    master1.mainloop()

#***********************************************************

instruction_frame=Frame(myApp)
instruction_frame.pack(fill=BOTH,expand=1)
def showInstructions():
    webbrowser.open("instructions.txt")

firstFrame=Frame(myApp)
firstFrame.pack(fill=BOTH,expand=1)

secondFrame=Frame(myApp)
secondFrame.pack(fill=BOTH,expand=1)

for x in range(3):
    Grid.columnconfigure(firstFrame, x, weight=1)

for y in range(3):
    Grid.rowconfigure(firstFrame, y, weight=1)

for x in range(3):
    Grid.columnconfigure(secondFrame, x, weight=1)

for y in range(3):
    Grid.rowconfigure(secondFrame, y, weight=1)

for x in range(3):
    Grid.columnconfigure(instruction_frame, x, weight=1)

for y in range(3):
    Grid.rowconfigure(instruction_frame, y, weight=1)

instr_button=Button(instruction_frame,text="Instructions",width=15,height=10,fg="purple",bg="yellow",command=showInstructions)
instr_button.config(font=("Helvetica", 17))
instr_button.grid(row=0,column=0,sticky=N+E+S+W)

quit_button=Button(instruction_frame,text="Quit",width=15,height=10,fg="purple",bg="yellow",command=window_for_exit)
quit_button.config(font=("Helvetica", 17))
quit_button.grid(row=0,column=1,sticky=N+E+S+W)

button1=Button(firstFrame,text="Model Answers",width=15,height=10,fg="purple",bg="yellow",command=window_for_no_of_questions)
button1.config(font=("Helvetica", 17))
button1.grid(row=1,column=0,sticky=N+E+S+W)

button2=Button(firstFrame,text="Students' Answers",width=15,height=10,fg="purple",bg="yellow",command=window_for_no_of_students)
button2.config(font=("Helvetica", 17))
button2.grid(row=1,column=1,sticky=N+E+S+W)

button3=Button(secondFrame,text="Evaluate",width=15,height=10,fg="purple",bg="yellow",command=window_for_evaluate)
button3.config(font=("Helvetica", 17))
button3.grid(row=2,column=0,sticky=N+E+S+W)

button4=Button(secondFrame,text="Results",width=15,height=10,fg="purple",bg="yellow",command=result)
button4.config(font=("Helvetica", 17))
button4.grid(row=2,column=1,sticky=N+E+S+W)
myApp.mainloop()


################################################################### GUI END #######################################################################



############################################################ UTILIZING THE ABOVE FUNCTIONS AND GENERATING SCORE########################################################################




############################################################ UTILIZING THE ABOVE FUNCTIONS END AND GENERATING SCORE ########################################################################
