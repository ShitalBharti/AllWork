'''Write a program to find number of occurrences of each vowel present in
the given string'''
word=input("enter the word")
vowels={'a','e','i','o','u'}
dict1={}
for i in word:
    if i in vowels:
       dict1[i]= dict1.get(i,0)+1
for k,v in (dict1.items()):
    print(k,"occured",v,"times")
