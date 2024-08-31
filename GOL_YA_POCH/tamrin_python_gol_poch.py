import random
bpl = 0 #emtibpc = 0
bpc = 0
Spl = 0
Spc = 0
while(True):
    i = input(" سلام توپ دست کی؟من یا تو؟")
    if i == "تو":
        while(True):
            pc = random.randint(0,1)
            pl=input("تو کدومه ؟ چپ یا راست؟")
            if pc == 0 and pl == "چپ" or pc == 1 and pl == "راست":
                print('آفرین از کجا فهمیدی')
                print('اه تو بردی')
                bpl += 1
            elif pc == 1 and pl == "چپ" or pc == 0 and pl == "راست":
                print('اشتباه گفتی')
                print('ایول من بردم')
                bpc += 1
            elif pl == "از اول" :
                bpc , bpl = 0 , 0
                print('باشه پس بیا آمار رو باضهم ببینیم')
                print(bpl,"بار بردی")
                print(bpc, "بار بردم")
                if bpl > bpc :
                    print('شما بردی')
                    Spl += 1
                elif bpl < bpc :
                    print('من بردم')
                    Spc += 1
                else :
                    print('برابر')
                break
            else :
                print('اشتباه زدی دوباره بزن')
    elif i == "من":
        while(True):
            pc = random.randint(0,1)
            pl=input("تو کدوم میذاری ؟ چپ یا راست؟")
            if pc == 1 and pl == "چپ":
                print('تو راسته')
                print('آفرین')
                print('اه تو بردی')
                bpl += 1
            elif pc == 0 and pl == "راست":
                print('تو چپه')
                print('آفرین')
                print('اه تو بردی')
                bpl += 1
            elif pc == 0 and pl == "چپ":
                print('تو چپه')
                print('درست هدس زدم')
                print('ایول من بردم')
                bpc += 1
            elif pc == 1 and pl == "راست":
                print('تو راسته')
                print('درست هدس زدم')
                print('ایول من بردم')
                bpc += 1
            elif pl == "از اول" :
                
                print('باشه پس بیا آمار رو باضهم ببینیم')
                print(bpl,"بار بردی")
                print(bpc, "بار بردم")
                bpc , bpl = 0 , 0
                if bpl > bpc :
                    print('شما بردی')
                    Spl += 1
                elif bpl < bpc :
                    print('من بردم')
                    Spc += 1
                else :
                    print('برابر')
                break
            else :
                print('اشتباه زدی دوباره بزن')
    elif i == "پایان":
        print('شما' , Spl , 'بار بردید')
        print('من' , Spc ,'بار بردم')
        if Spl > Spc :
            print('شما بردی')
        elif Spl < Spc :
            print('من بردم')
        else :
            print('برابر')
        print('خدافظ')
        break
    else :
        print('اشتباه زدی دوباره بزن')