# Creating Tuple
tuple1 = (1,'Shital','A',10.5)
print(tuple1)

# Accessing tuple elements
tuple2 = (1,2,3,4,5,6)
print(tuple2[1])

# Unpack a tuple in several variables
tuple1 = (1,'Shital','A',10.5,True)
no = tuple1[0]
string = tuple1[1]
char = tuple1[2]
decimal = tuple1[3]
boolean = tuple1[4]
print("{}\n{}\n{}\n{}\n{}".format(no,string,char,decimal,boolean))

# add an item in a tuple
tup1=(2.5,1,'shi')
print(tup1)
print(type(tup1))
lis=list(tup1)
lis.append("hai")
print(lis)
print(type(lis))
tup=tuple(lis)
print(type(tup))
print(tup)

# convert a tuple to a string
tul_str = ('Shital','Bharti')
tul_str1 = str(tul_str)
print(type(tul_str1))  # -> string
print(tul_str1)

# get the 4th element and 4th element from last of a tuple
tup_1 = (1,2,3,4,5,6,7,8,9,10)
print("First 4th:",tup_1[3])
print("Length:",len(tup_1))
print("Last 4th:",tup_1[-4])



