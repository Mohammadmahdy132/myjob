import random 
LEN = 0

print("سلام من قول چراغ ام تو اینجا 100 تا صندوق وجود دارد اگه با ده تا حدس بتونی صندوق پر از طلا رو ولی اگه نتونی جعبه رو عوض میکنم")
while(True): #braye avaz shodan adad
    i = input("شروع کنیم؟")
    if i == "بله":
        PCN = random.randint(1,100)
        while(True):
            PLR = int(input(" بگو ببینم تو کدومه؟" ))
            if LEN == 10 and PCN != PLR: #shart avaz shodan adad
                print("ایوای عدد عوض شد")
                print("دوباره")
                break
            else:
                if PCN == PLR: #shart barande shodan
                    print("آفرین تو محشری!")
                    break
                elif PCN < PLR :
                    LEN += 1
                    print('بیا پایین')
                elif PCN > PLR :
                    LEN += 1
                    print("برو بالا") # baraye rahnamaiy
                else :
                    print("متوجه نشدم")
    elif i == "نه" or i== "خیر": #shart raftan
        print("پس خدافظ")
        break
    else :
        print("متوجه نشدم")