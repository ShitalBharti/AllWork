def kangaroo(x1, v1, x2, v2):
    # Write your code here
    kangro1=[x for x in range(x1,x1*100,v1)]
    kangro2=[x for x in range(x2,x2*1000,v2)]
    print(kangro1)
    print(kangro2)
    try:
        for x in range(len(kangro1)):
            if kangro1[x] == kangro2[x]:
                
                return "YES"
        else:
            
            return "NO"
            
            
    except:
        return "NO"
    
                
# print(kangaroo(0,3,4,2))
print(kangaroo(2081,8403,9107,8400))