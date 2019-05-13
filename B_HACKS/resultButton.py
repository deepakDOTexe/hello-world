def result():
    import matplotlib
    matplotlib.use('TkAgg')
    import numpy as np
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    from matplotlib.figure import Figure
    # from tkinter import *
    import tkinter

    root=Tk()

    f=open("eval.txt","r")
    line=[]
    line.append(f.readline())
    while line[len(line)-1]:
        line[len(line)-1]=line[len(line)-1].split(" ")
        line.append(f.readline())

    f.close()

    from prettytable import PrettyTable

    head=[" "]
    for i in range(len(line[0])):
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


