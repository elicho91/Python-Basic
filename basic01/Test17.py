'''
* 생성자 init 메서드 *
'''
class Person:
    # 클래스 변수
    name = ""
    age = 0
    def __init__(self, name, age): # 생성자
        # 인스턴스 변수
        self.name = name
        self.age = age
        print("생성자 호출!!")
#---------------------------------
person = Person("raichu", 10)
print(person.name)
print(person.age)

class Npc:
    count = 0 # Npc가 만들어질때마다 Npc의 수를 카운팅할 변수

    def __init__(self, name):
        self.name = name
        print("{} 만들어지는 중....".format(self.name))
        Npc.count += 1

    def die(self):
        print("{}가 죽었습니다....ㅠㅠ".format(self.name))
        Npc.count -= 1

    def showInfo(self):
        print("생존하고 있는 NPC는 {}명 입니다.".format(Npc.count))

#-----------------------------------------------------------------------
#elf1 = Npc("엘프1")
#elf2 = Npc("엘프2")
#elf3 = Npc("엘프3")
#elf1.showInfo()
#elf2.die()
#elf1.showInfo()

# 상점 계산대
class Payment:
    # 클래스 변수
    count = 0       # 제품의 총 개수
    discount = 0.2  # 할인율

    # 생성자
    def __init__(self, price, number):
        # 인스턴스 변수
        self.price = price
        self.number = number
        Payment.count += 1
    # 인스턴스 메서드
    def calculater(self):
        # 인스턴스 변수
        self.pay = self.price * self.number # 정가
        self.dc_pay = self.pay - (self.pay * Payment.discount)  # 할인가

    # 인스턴스 메서드
    def display(self):
        print(Payment.count, "번째 제품입니다.")
        print("정가 : ", self.price)
        print("수량 : ", self.number)
        print("가격 : ", self.price)
        print("할인가격 : ", self.dc_pay)

    # 스태틱 메서드
    @staticmethod
    def welcome():
        print("어서오세요~")
        print("할인중입니다.")

    # 클래스메서드
    @classmethod
    def update(cls, value):
        # 할인율 조정 : 1 이상이거나 0이하면,
        # 할인을 입력받도록
        while value >= 1 or value <= 0:
            value = float(input("할인율을 다시 입력하세요 : "))
        cls.discount = value
#-----------------------------------------------------------------------------
p1 = Payment(1000, 5)
p1.calculater()
p1.display()

Payment.update(1)

p2 = Payment(2000, 4)
p2.calculater()
p2.display()

p2.welcome()
        

