Persons = set() #ذخیره کردن کد ملی ها
Masoud, Saeed, Bagher =0, 0, 0 #نامزدها
Void_Votes = 0   #باطله
len_Persons = 0
while (True):
    vote = int(input("کد ملی: "))
    if vote==56561388: #شرط خروج
        print("آقای پزشکیان: ", Masoud)
        print("آقای جلیلی :", Saeed)
        print("آقای قالیباف: ", Bagher)
        print("رای های باطله: ", Void_Votes)
        print("کد های ملی: ", Persons)
        if Masoud > Saeed and Masoud > Bagher and Masoud >= len_Persons / 2:
            print('جناب آقای پزشکیان پیروز شدند')
        elif Saeed > Masoud and Saeed > Bagher and Saeed >= len_Persons / 2:
            print('جناب آقای جلیلی پیروز شدند')
        elif Bagher > Saeed and Bagher > Masoud and Bagher >= len_Persons / 2:
            print('جناب آقای قالیباف پیروز شدند')
        else :
            print('هیچکدام در این انتخابات پیروز نشدند')
        break
    candidate = input(" (پزشکیان / جلیلی / قالیباف)به چه نامزدی رای می دهید: ")
    Persons.add(vote)
    if len(Persons) > len_Persons:  #شرط عدم تکرار رای دهنده
        if candidate == "پزشکیان":
            print("رای شما : پزشکیان")
            Masoud += 1
        elif candidate == "جلیلی":
            print('رای شما : جلیلی')
            Saeed += 1
        elif candidate == "قالیباف":
            print('رای شما : قالیباف')
            Bagher += 1
        else:
            print(" نام کاندید در حافظه وجود نداره رای شما باطل شد")
            Void_Votes+=1
    else :
        print("شما قبلا رای داده اید لطفا دوباره تلاش نکنید")
       
    len_Persons = len(Persons)