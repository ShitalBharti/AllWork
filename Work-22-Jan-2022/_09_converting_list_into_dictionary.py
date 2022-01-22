#converting list into dictionary
countries=["india","usa","uk","indonesia"]
cities=["delhi","newyark","london","bali"]
z=zip(countries,cities)
d=dict(z)
print(d)
print('{:15s} -- {:15s}'.format('Country','Capital'))
for k in d:
    print('{:15s} -- {:15s}'.format(k,d[k]))