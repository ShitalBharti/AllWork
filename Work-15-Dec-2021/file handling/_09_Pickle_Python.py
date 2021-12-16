"""
-> It is used to store some employee details like employee id (int), name (string), salary(float) in a structured manner.
-> create a class and store data in objects.
-> object is converted to byte stream and than stored into a file.
-> This is called as object serialization or pickle.

-> Read file, byte stream is converted back into a class object. It means, unpickling or de-serialization.
"""

# to serialize object
import _10_Employee, pickle

f = open('C:\\Users\\Admin\\Desktop\\emp.dat','wb')

no = int(input("How many employees?"))

for i in range(no):
    id = int(input("Enter id:"))
    name = input("Enter name:")
    sal = float(input("Enter salary:"))

    emp = _10_Employee.Employee(id,name,sal)  # create object of Employee class and initalize value using intializer

    pickle.dump(emp,f)  # to store object emp into file f

    f.close()









