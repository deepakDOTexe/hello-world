from tkinter import *
     


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
        
        B1 = Button(popup, text="Done !!", command = destroy_popups)
        B1.pack()
        popup.mainloop()
    
    #menu to enter no. of questions
    master=Tk()
    label=Label(master,text="Enter No.of Questions",bg="blue",fg="white")
    label.grid(row=1,column=1)

    entry_field=Entry(master)
    entry_field.grid(row=1,column=2)

    entry_field.focus_set()
    
    entry_button = Button(master,text="Confirm",command=confirm)
    entry_button.grid(row=2,column=2)
    
    wait_label=Label(master,text="Please wait for 5-6 minutes a popup will appear after processing is finished")
    wait_label.grid(row=3,column=2)

    master.mainloop()



root=Tk()

button1=Button(root,text="Button1",command=window_for_no_of_questions)
button1.pack()
root.mainloop()
