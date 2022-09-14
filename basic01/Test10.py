'''
* 딕셔너리 dict *
    key, value 쌍으로 구성되는 데이터를 저장하는 자료구조
    key값은 고유한값, 중복X
    수정 가능 mutable
    구분기호 : { : }

    변수 = { key:value, key:value, ..... }
'''
dic = {"a":[1,2,3,4,5], "b":20, "c":30}
print(dic)
print(type(dic))
print(dic["a"])
print(dic["b"])
print(dic["c"])

# 빈 딕셔너리
tup = ()
lst = []
dic = {}
print(type(dic))

info = {"name":"피카츄", "age":30, "mobile":"010-111-2222"}
print(info)

# key들만 꺼내기
key_list = info.keys()
print(key_list)

# value 들만 꺼내기
val_list = info.values()
print(val_list)

# key, value 세트로 꺼내기
items = info.items()
print(items)

# value 한개 꺼내기 : [키] .get(키)
print(info["name"])
print(info.get("name"))
# print(info["hello"]) 없는키 꺼내면 에러
print(info.get("hello", "hahahaha")) # 없는 key 꺼낼때 None으로 리턴(에러x) default값 설정가능

# in 연산자
print("name" in info)

# 요소 추가 #1.
info.update({"city" : "Seoul"})
print(info)
# 요소 추가 #2. 없는 key값으로 대입시 세트 추가
info["nickname"] = "pikapika"
print(info)

# 수정
info["nickname"] = "krong"
info.update({"nickname" : "python"})
print(info)
info["nickname"] = "krong"
print(info)

# 요소 제거 : __delitem__(키값)
info.__delitem__("nickname")
print(info)

'''
* 집합 set*
    중복 허용안되는 자료구조
    set 키워드 사용, 순서X, 2.3버전
    교집합 intersection, 합집합 union, 차집합 difference
    구분기호 : {}
    변수 = set(리스트, 문자열, 튜플, 딕셔너리)
'''
# 빈 set
s = set()
print(s)
print(type(s))

s1 = set([1,2,3,4,5,6,7])
s2 = set([3,6,8,9])

print(s1)
print(s2)

# 교집합 : &
print(s1 & s2)
print(s1.intersection(s2))

# 합집합 : |
print(s1|s2)
print(s1.union(s2))

# 차집합 : -
print(s1-s2)
print(s1.difference(s2))
print(s2-s1)
print(s2.difference(s1))

# 추가 : add()
s3 = set([1,2,3])
s3.add(10)
print(s3)

# 삭제 : remove()
s3.remove(10)
print(s3)







