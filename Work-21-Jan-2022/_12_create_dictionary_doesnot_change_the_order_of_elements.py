#create an ordered dictionary
from collections import OrderedDict
d=OrderedDict()
d[10]='A',
d[11]='B',
d[13]='C',
d[12]='D',
d[14]='E',
for i,j in d.items():
    print(i,j)