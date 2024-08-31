print("سلام\nشما وارد سامانه پیشرفته شده اید\nامید واریم حالتان خوب باشد")
while(True):
    avval = input("شما می خواهید از چه سامانه ای استفاده کنید\n(کلمه کلمه کردن جمله یا دریافت شماره موبایل از نامه یا ارسال نامه یا تمام):\n")
    if avval == "کلمه کلمه کردن جمله" or avval =="اولی" or avval =='1':
        Str = input("نامه را وارد کنید:\n")
        Word = set()

        for i in Str.split():
            Word.add(i)
        print(Word)
    elif avval == "دریافت شماره ی موبایل از نلمه" or avval =="دربافت شماره ی موبایل" or avval =="دومی" or avval =='2':
        LEN = []
        def PHNUM(text):
            NUM = text.split()
            AMAL2 = []
            for i in NUM:
                if i.isdigit():
                    if len(i) == 11 and i.startswith("09") and i.isdigit():
                        AMAL2.append(i)
                        LEN.append(AMAL2)
            return AMAL2
        l = PHNUM(input("شما در این فسمت می نوانید نامه ی تان را وارد و شماره های موجود را دریافت کنید:\n"))
        if len(LEN) == 0 :

            print("شماره ای وارد نشد")
            print("شماره ای وجود ندارد")
        print("شماره های موجود:",l)
    elif avval == "ارسال نامه" or avval =="سومی" or avval =='3':
        print("این سامانه هنوز طراحی نشده.")
    elif avval == "تمام":
        break
    else :
        print("شما اشتباه وارد کردید لطفا دوباره وارد کنید")
