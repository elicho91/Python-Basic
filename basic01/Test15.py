def packer(name, **kwargs): # dict로 패킹해서 담는다.
    print(name)
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())
    for i,j in kwargs.items():
        print("{} : {}".format(i, j))


packer("pika", age="30", mobile="010-1111-2222", city="seoul")

# dict unpacking 두개 모두 값이 있으면 true 없으면 false
def unpacker(name, score=None):
    if name and score: # 둘중 하나라도 값이 없으면 false
        print("안녕하세요, {}님의 점수는 {}점 입니다.".format(name, score))
    else:
        print("이름이나 점수가 없네요~~")

unpacker(**{"name":"김피카츄"})

