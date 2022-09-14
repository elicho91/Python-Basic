'''
* 특수 메서드 *
__init__() : 생성자
__del__() : 소멸자 레퍼런스 카운트가 0이 되면 자동으로 호출
__coll__() : 객체 호출 시 실행되는 메서드
__getTime__() : 딕셔너리 처럼 객체.['키값']을 이요해 속성을 찾게 해주는 메서드
            메서드 내에서 입력한 키에대한 값을 리턴해주어야한다.
__name__ / __main__ : Dunder name

'''


class Char:
    def __init__(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print("player가 생성되었습니다.")
    def __call__(self, *args, **kwargs):
        print("hp : {}, attack : {}, defence : {}".format(self.hp, self.attack, self.defence))
        print(kwargs)
        for i, j in kwargs.items():
            self.__setattr__(i, j) # 속성추가, 변수 생성 __settattr__(변수명, 값)

    def __getitem__(self, item):
        print(item)
        if item == "hp":
            return self.hp
        elif item == "attack":
            return self.attack
        elif item == "defence":
            return self.defence
        else:
            return "존재하지 않는 값입니다."

a = Char(10, 200, 150)
b = Char(90, 70, 30)

a(abc="123", de="456") # __call__() 호출
b()

print(a["hp"]) #__gettitem__() 호출

print(a.abc)
print(b.de)