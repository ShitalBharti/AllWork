#Handling precision values
#precision limit=5
#using round : syntax:  round(variable_name,point)
a=123345.12354658769
ans=round(a,5)
print(ans)

#using % operator
ans1='%.2f'% a
print('ans1',ans1)

#using format

ans2='{0:.6f}'.format(a)
print('ans2',ans2)


