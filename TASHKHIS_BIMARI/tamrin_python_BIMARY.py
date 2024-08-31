while(True):
    Input = input("کجا ی شما درد نیکند؟(سینه یا کلو یا شکم یا هیچکدام)")
    if Input == "سینه" :
        print("احتمال سکته وجود دارد")
    elif Input == "شکم" :
        print("احتمال عود آپاندیس وجود دارد")
    elif Input == "گلو" :
        Input2=input("آیا سرفه هم دارید؟بله یا خیر؟")
        if Input2 == "بله" :
            print('احتمالا شما ویروسی شده اید.')
        elif Input2 == 'خیر' or Input2 == 'نه':
            print("شما حساسیت فصلی دارید")
        else :
            print('لطفا درست وارد کنید')
    elif Input == "هیچکدام" :
        Input3 = input('آیا شما سرفه می کنید؟')
        if Input3 == "بله":
            Input4 = input("آیا شما تب دارید؟")
            if Input4 == "بله":
                print('شما آنفولانزا گرفته اید')
            elif Input4 == "خیر" or Input4 == "نه" :
                print('شما سرما خورده اید')
            else:
                print('لطفا درست وارد کنید')
        elif Input3 == "خیر" or Input3 == 'نه':
            print('شما سالم هستید')
        else :
            print('لطفا درست وارد کنید')
    else :
        print('لطفا درست وارد کنید')
        
    
    
    
    