while(True):
    Input = input("کجا ی شکا درد نیکند؟(سینه یا کلو یا شکم یا هیچکدام)")
    if Input == "سینه" :
        print("احتمال سکته وجود دارد")
    elif Input == "شکم" :
        print("احتمال عود آپاندیس وجود دارد")
    elif Input == "گلو" :
        Input2=input("آیا سرفه هم دارید؟بله یا خیر؟")
        if Input2 == "بله" :
            print('احتمالا شما ویروسی شده اید.')
        else :
            print("شما حساسیت فصلی دارید")
    elif Input == "هیچکدام" :
        Input3 = input('آیا شما سرفه می کنید؟')
        if Input3 == "بله":
            Input4 = input("آیا شما تب دارید؟")
            if Input4 == "بله":
                print('شما آنفولانزا گرفته اید')
            else :
                print('شما سرما خورده اید')
        else:
            print('شما سالم هستید')
        
    
    
    
    