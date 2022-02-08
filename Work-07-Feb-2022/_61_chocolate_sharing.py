

def birthday(s, d, m):
    
    count=0
    
    for x in range(len(s)):
        for y in range(x,len(s)):
            str1=s[x:y+1]
            if len(str1)==m and sum(str1)==d:
                print(s[x:y+1])
                count+=1
            
        
    print(count)
    
# birthday([2,2,1,3,2],4,2)#2
# birthday([1 ,2, 1, 3, 2],3,2)#2
# birthday([1 ,1,1,1,1,1],3,2)#0
# birthday([4],4,1)#1
# birthday([2, 5 ,1, 3 ,4 ,4, 3 ,5, 1 ,1, 2 ,1, 4 ,1 ,3 ,3, 4 ,2, 1],18,7)#3
birthday([3,5, 4, 1, 2, 5, 3, 4, 3, 2, 1, 1, 2, 4, 2, 3, 4, 5, 3, 1, 2, 5, 4, 5, 4, 1, 1, 5, 3, 1, 4, 5, 2, 3, 2, 5, 2, 5, 2, 2, 1, 5, 3, 2, 5, 1, 2, 4, 3, 1, 5, 1, 3, 3, 5],18,6)#10