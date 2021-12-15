# convert a list of tuples into a dictionary

# 1. Using for loop
iptuple_list = [('Shital',1),('Vitthal',2),('Shubham',3),('Shilpa',4),('Ajju',5)]
print("Original list of tuples:",iptuple_list)
opdict = {}
for item in iptuple_list:
    for i in item:
        if item.index(i) == 0:
            key = i
        else:
            value = i
    opdict[key] = value
print("Dictionary output:",opdict)

print("-----------------------------------------------")

# 2. Using dict method
iptuple_list = [('Shital',11),('Vitthal',12),('Shubham',13),('Shilpa',14),('Ajju',15)]
print("Original list of tuples:",iptuple_list)
opdict = {}
opdict = dict(iptuple_list)
print("Dictionary output:",opdict)