'''
파라미터와 인자 : 개수, 순서가 일치 해야 된다.
파라미터의 초기값 지정.
초기값이 파라미터에 저장되어있으면, 인자를 생략 가능.

'''

def func(username, password, name, gender, email, nation="S.Korea"):
    print(username)
    print(password)
    print(name)
    print(gender)
    print(email)
    print(nation)

func("pika", "1234", "김피카츄", "M", "abc@gmail.com")
print("="*10)

'''
파라미터와 인자 : 개수, 순서*가 일치 해야 한다.
파라미터 순서 바꿔도 사용가능한 방법
함수 호출할때 인자 기입시, 파라미터명=값
'''

func(name="피카피카", password="1212", email="hello@.com", gender="F", username="haha", nation="USA")
print("="*10)

# 리턴
def calc(num1, num2):
    return num1 + num2, num1 - num2
print(calc(10,20))
print("="*10)

res1, res2 = calc(100,400) #(500,-300) 튜플로 리턴, unpacking되서 변수에 저장
print(res1)
print(res2)

