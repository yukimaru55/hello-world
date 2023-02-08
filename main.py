n = [1,2,3]
# print (n[0])
i = int(input("三桁の数字を入力"))
def validate(ii):
    if ii < 1000 and ii > 99:
        return True
    else :
        return False

if validate (i):
    lst = []
    while i > 0:
        lst.append(i%10)
        i //= 10 # 必須
        lst.reverse()
    print(lst)
    if n[0] == lst[0]:
        if n[1] == lst[1]:
            if n[2] == lst[2]:
                print("3イート")
            elif 


















else:
    print("ERROR")

