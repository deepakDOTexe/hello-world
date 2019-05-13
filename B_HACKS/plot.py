import matplotlib.pyplot as plt

f=open("eval.txt","r")
line=[]
line.append(f.readline())
while line[len(line)-1]:
      line[len(line)-1]=line[len(line)-1].split(" ")
      line.append(f.readline())

f.close()
##
##z=line.pop(len(line)-1)
##print(line)
##for i in range(len(line)):
##      for j in range(len(line[i])):
##            if line[i][j][-1]=="\n":
##                  line[i][j]=line[:len(line[i][j])-1]
##            if  line[i][j].isnumeric():
##                  line[i][j]=line[:len(line[i][j])-1]

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
print(line_new)
for i in line_new:
      t.add_row(i)
print (t)
