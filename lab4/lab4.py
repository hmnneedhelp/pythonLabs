print('Введите высоту')
h=int(input())
print("Введите радиус")
r=int(input())
pi=3.14
v=int(pi*(r**2)*h)
print("Плотность равна "+str(v))
ropb=11.35
rocu=8.9
cu=(v*rocu)
pb=(v*ropb)
print("масса для меди "+str(cu))
print('масса для свинца '+str(pb))
