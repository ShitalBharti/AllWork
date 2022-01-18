"""
Assignment Operators: =,+=,-=,*=,/=,%=,//=,**=,&=,|=, >>=,<<=,^=
"""
a = 10
print(a)
a += 3  # -> a=a+3
print(':a+=3->',a)    # Augmented Assignment Operator
a -= 4  # -> a=a-4
print(':a-=4->',a)
a *= 3  # -> a=a*3
print(':a*3->',a)
a /= 2  # -> a=a/2
print(':a/=2->',a)
a %= 4  # -> a=a%4
print(':a%=4->',a)
a //= 2  # -> a=a//2
print(':a//=2->',a)
a **= 2  # -> a=a**2
print(':a**=2->',a)
a = 7
a &= 3  # -> a=a&3
print(':a&=3->',a)
a = 6
a |= 3  # -> a=a|3
print(':a|=3->',a)
a ^= 3  # -> a=a^3
print(':a^=3->',a)
a >>= 2  # -> a=a>>2
print(':a>>=2->',a)
a <<= 3  # -> a=a<<3
print(':a<<=3->',a)
