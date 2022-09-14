'''
* 파이썬 다중 상속 주의점 *
파이썬은 클래스/메서드 탐색 순서는 MRO(Method Resolution Order)를 따른다.
다중 상속 시, 부모클래스 나열할때 우선순위는 왼쪽 -> 오른쪽 순서로 높다.
동일 메서드가 둘 이상의 부모에 존재하면 왼쪽 클래스의 메서드가 실행된다.
클래스명.mro() 를 통해 순서 확인이 가능하다.
'''
class A:
    pass

# print(A.mro())

class B(A):
    pass

# print(B.mro())
    pass

class C(A):
    pass

#print(C.mro())

class D(B, C):
    pass

print(D.mro())

class E(C,B):
    pass

print(E.mro())

class F(D,E):
    pass

print(F.mro())