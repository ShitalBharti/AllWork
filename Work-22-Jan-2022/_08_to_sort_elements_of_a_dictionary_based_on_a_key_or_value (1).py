colors={10:"red",34:"yellow",67:"white",98:"orange"}
#sort the dictionary by keys from 0th element
c1=sorted(colors.items(),key=lambda t:t[0])
print(c1)
c2=sorted(colors.items(),key=lambda t:t[1])
print(c2)