"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
 Print the average of the marks array for the student name provided, showing 2 places after the decimal.
"""
n=int(input("Enter the no of student"))
data={}
for i in range(n):
    name=input("enter the name")
    marks=[]
    for j in range(3):
        score=int(input("Enter the marks"))
        marks.append(score)
    data[name]=marks
print(data)

query=input("Please enter the name")
total = 0
for i,j in data.items():

    if i==query:
        for k in j:
            total +=k

aver=float(total/3)
format_data="{:.2f}".format(aver)
print(format_data)
