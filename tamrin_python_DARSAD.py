# تمرین انتخاب رشته
def ENTEKHAB_RESHTEH(reshteh = "ریاضی",alageh = 0,talash = 0,hadaf = "خیر",hoosh = 0,tamarkoz = 0,hoseleh = "بله",madreseh = "خیر"):
    if madreseh == "بله":
        madreseh = 100
    elif madreseh == "خیر":
        madreseh = 0 
    else:
        print("یه اشتباهی شده دوباره وارد کنید")
    if hadaf == "بله":
        hadaf = 100
    elif hadaf == "خیر":
        hadaf = 0 
    else:
        print("یه اشتباهی شده دوباره وارد کنید")
    if hoseleh == "بله":
        hoseleh = 0
    elif hoseleh == "خیر":
        hoseleh = 100 
    else:
        print("یه اشتباهی شده دوباره وارد کنید")
    if reshteh == "ریاضی":
        mot = int((alageh*3+talash*2+hadaf*2+hoosh*3+tamarkoz+hoseleh+madreseh*2)/14)
        return mot
    elif reshteh == "تجربی":
        mot = int((alageh*4+talash*3+hadaf*4+hoosh*2+tamarkoz+hoseleh+madreseh*2)/17)
        return mot
    elif reshteh == "انسانی":
        mot = int((alageh*3+talash*2+hadaf*2+hoosh*2+tamarkoz*2+hoseleh*2+madreseh*2)/15)
        return mot
print("سلام\nاین سامانه ی انتخاب رشته است")
R=input("نام رشته که که می خواهید بروید را \nبنویسید:")
A=int(input("چقدر به این رشته علاقه دارید؟"))
TL=int(input("تلاش شما چقدر است؟"))
HA=input("آیا هدفی دارید که به این رشته رفته اید؟ (بله , خیر):")
HO=int(input("هوش شما چفدر است؟"))
TM=int(input("تمرکز شما چفدر است؟"))
HS=input("آیا بی حوصله هستید؟(بله , خیر):")
MA=input("آیا قصد دارید به مدارس خوب بروید؟(بله , خیر):")
X = ENTEKHAB_RESHTEH(R,A,TL,HA,HO,TM,HS,MA)
print(f"میزان موفقیت شما در این رشته:{X}%")