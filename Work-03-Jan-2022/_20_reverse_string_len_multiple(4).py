
def rev_string(string):
    if len(string) % 4 == 0:
        list_str = list(string)
        list_str.reverse()
        new_str = ''.join(list_str)
        return new_str
    else:
        return string

res = rev_string(input("Enter String: "))
print(res)