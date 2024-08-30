def Check_Language(text):
    n = list()
    EN = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
    FA = {'ی', 'ه', 'و', 'ن', 'م', 'ل', 'گ', 'ک', 'ق', 'ف', 'غ', 'ع', 'ظ', 'ط', 'ض', 'ص', 'ش', 'س', 'ژ', 'ز', 'ر', 'ذ', 'د', 'خ', 'ح', 'چ', 'ج', 'ث', 'ت', 'پ', 'ب' ,'آ', 'ا'}
    NM = {'1','2','3','4','5','6','7','8','9','0'}
    Ch_FA = 0 
    Ch_EN = 0
    Ch_NM = 0
    Ch_DG = 0
    for i in text:
        n.append(i)
        if i in FA:
            Ch_FA += 1
        elif i in EN:
            Ch_EN += 1
        elif i in NM:
            Ch_NM += 1
        else:
            Ch_DG += 1
    LENFA = (Ch_FA/len(n))*100
    LENEN = (Ch_EN/len(n))*100
    LENNM = (Ch_NM/len(n))*100
    LENDG = (Ch_DG/len(n))*100
    if LENFA > LENEN and LENFA > LENDG and LENFA > LENNM :
        print("بیشتر حروف فارسی است")
    elif LENEN > LENFA and LENEN > LENDG and LENEN > LENNM :
        print("بیشتر حروف انگلیسی است")
    elif LENNM > LENEN and LENNM > LENDG and LENNM > LENFA :
        print("بیشتر حروف فارسی است")
    else:
        print("بیشتر حروف نامعلوم است")
    print(f"این نامه {int(LENFA)}% فارسی و\n{int(LENEN)}% انگلیسی و\n{int(LENNM)}% عددی است")
Check_Language(input("نامه ی خود را وارد کنید:"))
        