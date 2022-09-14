'''
 * 연산자 operator *
    산술      : + - * / %
    대입      : =
    복합대입  : += -= *= /= %=
    비교      : > >= < <= == !=
    논리      : and or
    멤버      : in / not in
    식별      : is / is not
'''
num1 = 10
num2 = 3
print(not(num1 != num2))

lst = [1,2,3,4,5]
print(10 not in lst)
a = 10
b = 10
print(a is not b)
print(id(a))
print(id(b))
