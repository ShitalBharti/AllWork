def add(a,b): # formal arguments
    c = a+b
    print(c)

x = 10; y= 15
add(x,y)   # actual arguments

"-------Types of Actual arguments:---"

# positional arguments

def attach(s1,s2):
    s3 = s1 + s2
    print("Total String: "+s3)

attach('New','York')

# keyword arguments

def grocery(item,price):
    print("Item: ",item)
    print("Price: ",price)

grocery(item='Sugar',price=45.60)

# Default Arguments

def grocery(item, price = 40.00):
    print("Item: ", item)
    print("Price: ", price)

grocery(item='Salt',price=45.60)  # overwrite the default value
grocery(item='Grapes')              # will take the default value

# variable Length Arguments

def show_el(*args):  # arguments in form of tuple
    for item in args:
        print(item)
show_el(1,2,3,4)

def show_el(**kwargs):  # arguments in form of dictionary
    for item in kwargs.items():
        print(item)
show_el(name='shital', age = 25)