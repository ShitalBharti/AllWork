
def divideIntegers(dividend,divisor):
    temp = 0
    count = 0
    flag = False
    if divisor < 0 or dividend < 0:
        if divisor < 0 and dividend < 0:
            divisor = -(divisor)
            dividend = -(dividend)
        elif divisor < 0:
            divisor = -(divisor)
            flag = True
        elif dividend < 0:
            dividend = -(dividend)
            flag = True

    while temp <= dividend:
        if dividend-temp < divisor:
            break
        temp = temp + divisor
        count += 1

    print(temp)
    if flag == True:
        print(-(count))
    else:
        print(count)

dividend = int(input("Enter dividend: "))
divisor = int(input("Enter divisor: "))
divideIntegers(dividend,divisor)