try:
     x = int(input("Enter a number: "))
     y = 1/x
finally:
    print("We are not catching the exception")
print("Inverse is:: ",y)