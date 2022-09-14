'''
with 키워드 이용해서 cotext manager 만들기
'''
with open("database.txt", 'w') as file:
    # file.write("하하하하하\n")
    # file.write("호호호호호\n")
    # file.close() : 블럭이 끝나면 file이 없어지니 close도 필요없음

with open("database.txt", "r") as file:
    result = file.readlines()
    print(result)
    for r in result:
        print(r, end="")
    print(result)
