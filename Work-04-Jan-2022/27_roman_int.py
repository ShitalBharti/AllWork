print("Roman to Integer")

num={1:'I',5:'V',10:'X',50:'L',100:'C',500:'D',1000:'M'}
n=0
l=[]
value=input("enter the number")

for i in value:
    l.append(i)

for k in l:
    for i ,j in num.items():
        if k==j:
            n +=i
print(f"from Roman {value} into Integer {n}")
