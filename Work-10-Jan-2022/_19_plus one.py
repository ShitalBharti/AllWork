result = []
digits=[1,2,3,4,5]
str_digits = ''.join(str(i) for i in digits)
int_digits = int(str_digits) + 1
str_digits = str(int_digits)
for i in str_digits:
    result.append(int(i))
    print(result)

'''def plusOne(digits):
    num = 0
    for i in range(len(digits)):
    	num += digits[i] * pow(10, (len(digits)-1-i))
    return [int(i) for i in str(num+1)]
digits=[1,2,3,4]
print(plusOne(digits))'''