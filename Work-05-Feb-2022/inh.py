from teacher import Teacher
t=Teacher()
#store data into the instance
t.setid(55)
t.setname("Rakshitha")
t.setaddress("Rajajinagar")
t.setsalary(25000)
#retrieve data from instance and dispaly
print('id= ',t.getid())
print('name= ',t.getname())
print('address= ',t.getaddress())
print('salary= ',t.getsalary())