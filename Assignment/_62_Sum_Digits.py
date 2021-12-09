# compute sum of digits of a given string
class DigitMissingError(Exception):
    """Raised when the input value is not contain digits"""
    pass

string = input("Enter String containing digits:")
try:
    if string.isalpha() == True:
        raise DigitMissingError
    elif string.isalnum() == True:
        total = 0.0
        for i in string:
           if i.isdigit():
               total = total + float(i)
        print("Sum of digits is:",total)
    else:
        raise DigitMissingError

except DigitMissingError:
    print("Digits are missing in given string")