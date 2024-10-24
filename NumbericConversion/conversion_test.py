# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer
a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

#a= int(a)
#print(a) ValueError: invalid literal for int() with base 10: ' 101.1 '. converting to int gives error message
a=float(a)
print(a)
#converting to a float first then to int works. 
a=int(float(a))
print(a)
b=int(b)
print(b)
b=float(b)
print(b)
print(d[6:])
print(c[0:3])
a.strip
print(a)
d.strip(" ")
print(d)
# for split it removes