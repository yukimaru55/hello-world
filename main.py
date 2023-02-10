import random
n = [0, 1, 2, 3, 4,5,6,7,8,9]
n = random.sample(n, 3)

EATE =0
while EATE != 3:
    EATE = 0
    BITE = 0

    i = int(input("三桁の数字を入力"))
    def validate(ii):
        if ii < 1000 and ii > 0:
            return True
        else :
            return False

    
    if validate (i):
        lst = []
        while i > 0:
            lst.append(i%10)
            i //= 10 
        
      
        
        while len(lst) != 3:
            lst.append(0)
        lst.reverse()
        print(lst)

        
        for i in range(3):
            if n[i] == lst[i]:
                EATE += 1
            elif lst[i] in n:
                BITE += 1
            else:
                pass
        print(str(EATE) + ":EATE   " + str(BITE) + ":BITE" )    
        
    else:
        print("ERROR")

print('正解です')