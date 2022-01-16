def isPower_of_Three(n):
    if (n <= 0):
        return False
    if (n % 3 == 0):
        return isPower_of_Three(n // 3)
    if (n == 1):
        return True
    return False


# Driver code
num1 = 243
if (isPower_of_Three(num1)):
    print("Yes")
else:
    print("No")

num2 = 6
if (isPower_of_Three(num2)):
    print("Yes")
else:
    print("No")
