string = input("Enter String:")
myit = iter(string)

if next(myit):
    word = string.split(" ")
    print(word)