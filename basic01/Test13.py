'''
예상할 수 없는 함수 : 매개변수에 전달되는 인자가 여러개일경우 한곳에 받아 줄 수 있는 기능
def 함수명(*파라미터)
    실행문들...
'''
def sum(*num): #던져줄 변수가 몇개인지 몰라~ *은 단일값이어도 튜플로 인식
    tot = 0
    print(num)
    print(type(num))
    for i in num:
        tot += i
    return tot

print(sum(10,20))

print("hello", "hahahaha")

print("*"*100)
def calc(oper, *num, test="hahahahah"):
    if oper == 'sum':
        tot = 0
        for i in num:
            tot += i
    elif oper == 'mul':
        tot = 1
        for i in num:
            tot *= i
        print(tot)
        return tot

result = calc("sum", 10, 20, 30, 40, test="kakakakakak")
print(result)