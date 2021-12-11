def reverseString():
    string = input("Enter a string:")
    list_str = list(string)
    list_str.reverse()
    print(list_str)
    rev = ''
    for item in list_str:
        rev = rev + item
    print(rev)

reverseString()