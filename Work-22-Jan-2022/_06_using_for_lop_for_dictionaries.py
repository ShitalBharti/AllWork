colors={'r':"red",'g':"green",'w':"white",'b':"blue"}
for k in colors:
    print(k)
for k in colors:
    print(colors[k])
for k,v in colors.items():
    print('{}:{}.'.format(k,v))
#python programe to show the usage of for loop to retrieve elements of dictionary
#using for loop with dictionaries
dict1={"rakshitha":"r",'vinith':'r','ranjitha':"sr","chandana":"s"}
for keys in dict1:
    print(keys)
for values in dict1:
    print(dict1[values])
print(dict.get("rakshitha",0))