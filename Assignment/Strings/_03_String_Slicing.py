class StringSlicing:
    def sliceString(self):
        st2 = str(input("enter the string for slicing : "))
        start = int(input("Enter start : "))
        end = int(input("Enter end : "))
        sliced_string = st2[start:end + 1]
        print(sliced_string)

obj = StringSlicing()
obj.sliceString()