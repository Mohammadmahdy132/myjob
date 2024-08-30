ER=0
Pass = str()
while (True):
    K = input("لطفا یک رمز وارد کنید:")
    m = K.isdigit()
    if  m == True:
        print('بفرمایید')
        Pass = K
        break
    else:
        print("لطفا دوباره وارد کنید")
    del K
while(True):
    ipt = input("رمز تان را وارد کنید:")
    if ipt == Pass:
        print("خوش آمدید")
        break    
    elif ER == 5 :
        print("شما دیگر نمی توانید رمز وارد کنید")
        break
    else :
        print("رمز اشتباه است لطفا دوباره وارد کنید")
        ER +=1

