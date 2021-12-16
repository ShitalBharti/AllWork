# to de-serialize object
import _10_Employee, pickle

f = open('C:\\Users\\Admin\\Desktop\\emp.dat','rb')

print("employees details:")

while True:
    try:
        emp = pickle.load(f)  # to store file data again into object, create object of class
        emp.display()         # to call display() method from class

    except:
        print("End of file reached....")
        break

    f.close()
