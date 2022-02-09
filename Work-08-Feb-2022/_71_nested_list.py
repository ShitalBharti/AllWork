"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""
n=int(input("Enter the number of student"))
l=[]
for i in range(n):
    ne_list=[]
    name=input("enter the name")
    score=float(input("enter the score"))
    ne_list.append(name)
    ne_list.append(score)
    l.append(ne_list)

res=sorted(l,key = lambda x: x[1])
for i in range(len(res)):
    if i==1:
       print(res[i][0])
    elif i>1 and res[i][1]==res[i-1][1]:
        print(res[i][0])

