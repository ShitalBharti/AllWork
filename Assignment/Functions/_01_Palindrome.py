def checkPalindrome():
    string = input("Enter String:")
    init_str_list = list(string)
    print(init_str_list)
    fin_str_list = init_str_list.copy()
    fin_str_list.reverse()
    print(fin_str_list)
    if init_str_list == fin_str_list:
        print("Palindrome")
    else:
        print("Not Palindrome")


checkPalindrome()