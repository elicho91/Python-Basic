# dunder name / main
def print_hello():
    print("hello method!")

print_hello()

print("__name__ : ", __name__)
# 현재 main 스레드로 이 파일을 실행시켰으면
# print_hello()를 실행해라~
# -> 아래 구문으로 코드가 실행되는 것인지, 임포트 된것인지 체크함
if __name__ == '__main__':
    print_hello()
