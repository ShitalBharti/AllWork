def printTable():
    number = int(input("Enter number:"))
    table_list = []
    for i in range(1,11):
        table_list.append(number * i)
    print("Table:{}".format(table_list))

printTable()