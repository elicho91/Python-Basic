# 싱속
class Student1:
    def python(self):
        print("재밌는 파이썬!!!!")
class Student2:
    def c(self):
        print("지루한 C언어....")
class Student3:
    def java(self):
        print("자바는 이제 그만~")
        
# 상속 받는 클래스 : 다중상속 가능
class Pikachu(Student1, Student2, Student3):
    pass

pika = Pikachu()
pika.java()

class Person:
    __jumin = "101010-101010" # 은닉화
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("부모 생성자!!!")
    def show(self):
        print("부모")
        print("이름 : ", self.name)
        print("나이 : ", self.age)
 #--------------------------------------
 class Student(Person):
    # 오버라이딩
     def __init__(self, name, age, hakbun):
         super(). __init__(name, age) # 부모생성자 호출
         self.hakbun = hakbun
         print("자식생성자")

     def show(self):
         print("자식")
         super().show() # 부모 show()메서드 호출
         print("학번 : ", self.hakbun)
#------------------------------------------
pk = Student("피카츄", 20, 2022)
pk.show()

print(Person.jumin)
print(Person.jumin)





