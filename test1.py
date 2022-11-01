from tools import *



#def mohit(x,y,z):
   # return x+y+z




x, y, z = input('enter a number: ').split(',')
x = int(x)
y = int(y)
z = int(z)


if x==y==z:
    print('parallelogy')
elif x==y or x==z or y==z:
    print('sagheyn')

else:
    print('no')


print(mohit(x,y,z))
print(masahat(x,y,z))