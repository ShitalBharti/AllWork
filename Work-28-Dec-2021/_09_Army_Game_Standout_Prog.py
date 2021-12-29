"""
Q. n rows and m columns in a sheet of graph paper
each cell in graph is an army base
total army base = n.m
If a base contains at least one package inside or on top of its border fence, then it's
considered to be supplied.
Find out minimum no. of packages required that all army bases are supplied.
"""
import math

n = int(input("Enter rows: "))
m = int(input("Enter columns: "))
total_base = n * m
print("Total Base in an army: ",total_base)
pkg = math.ceil(n/2) * math.ceil(m/2)
print("Minimum packages required: ",pkg)

"""
Approach:
1 * 1 = 1 b 1 pkg
1 * 2 = 2 b 1 pkg
1 * 3 = 3 b 2 pkg
1 * 4 = 4 b 2 pkg
"""

(n+n%2)*(m+m%2)/4
mod_n = n%2
mod_m = m%2
res = (n+mod_n) * (m + mod_m)
print("Packages required",res/4)