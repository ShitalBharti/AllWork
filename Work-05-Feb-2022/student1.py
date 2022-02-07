from student import Student
s=Student()
#store data into teh instance
s.setid(100)
s.setname('Rakshitha')
s.setaddress('banglore')
s.setmarks(600)

#retrieve data from instance and display
print('id= ',s.getid())
print('name= ',s.getname())
print('address= ',s.getaddress())
print('marks= ',s.getmarks())

#
