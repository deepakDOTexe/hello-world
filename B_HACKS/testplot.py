from tkinter import *

root = Tk()

f=open("eval.txt","r")
line=[]
line.append(f.readline())
while line[len(line)-1]:
      line[len(line)-1]=line[len(line)-1].split(" ")
      line.append(f.readline())

f.close()
print(line)
line_new=[]
for i in range(len(line[0])):
      line_new.append(["Student "+str(i+1)])
      
for i in range(len(line)):
      for j in range(len(line[i])):
            line_new[j].append(line[i][j])
print(line_new)

# height = len(line_new)+1
# width = len(line)
for i in range(len(line_new)): #Rows
    for j in range(len(line[i])+1): #Columns
        b = Label(root, text=line_new[i][j])
        b.grid(row=i, column=j,sticky=N+E+S+W)

mainloop()