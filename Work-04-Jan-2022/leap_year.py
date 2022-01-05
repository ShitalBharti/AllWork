print("Write a program to determine If the given year is a Leap year.")
year=int(input("enter the year"))

res=year%4
if res==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")