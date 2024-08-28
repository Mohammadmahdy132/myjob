ER=0
while (True):
    Pass = int(input("لطفا یک رمز وارد وارد کنید"))
    if Pass == int():
        print('بفرمایید')
        break
    else:
        print("لطفا دوباره وارد کنید")
        del Pass
while(True):
    ipt = int(input("رمز تان را وارد کنید"))
    if ipt == Pass:
        print("خوش آمدید")
        break
    else :
        print("رمز اشتباه است لطفا دوباره وارد کنید")
        ER +=1
    if ER == 5 :
        print("شما دیگر نمی توانید رمز وارد کنید")
        break