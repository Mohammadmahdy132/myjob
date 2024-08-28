from termcolor import colored
Bank = ['در پردازش متن ،متون مختلف مورد تحلیل قرار می گیرند  و هدف نهایی مدل و فهم زبان انسانی است که با روش های یادگیری ماشین قابل انجام است' ,
       'که ار کاربردهای آن در ماشین های خودران است، در این حالت ویدویوهای دریافتی از محیط بیرون  با استفاده از روش های یادگیری عمیق و پردازش تصویر برای کامپیوتر قابل فهم خواهند بود',
       'سیستم های خبره نوع دیگری از زیر شاخه های هوش مصنوعی می باشند که هدف اصلی این سیستم ها ، مدل سازی پدیده ها در قالب متن و استنتاج های مختلف از آن است .'
]
Bank_code = ['1','2','3']
text1 = colored("کدام:",'cyan')
char = 0
History = []
print('سلام\nبه سامانه ی گوگل من خیلی خوش آمدید\nگزینه ها:\n*****************************************************\n1 = جستوجو\n*****************************************************\n2 = جستوجو های من\n*****************************************************\n3 = افزودن\n*****************************************************\n4 = حذف\n*****************************************************\nX = اتمام\n')
while (True):
    N = input(text1)
    if N == "1":
        print('اتمام = 1\n')
        while (True):
            search = input('جستوجو:')
            if search == '1':
                break

            for text in Bank:
                if search in text:
                    char +=1
                    Index = Bank.index(text)
                    if char != 0 :
                        for text in Bank:
                            if search in text:
                                print(f"---***---\n{text}\nکد:{Bank_code[Index]}\n---***---\n")
            if search in History:
                Bank = Bank
            else:
                History.append(search)
            if char == 0 :
                print ('جیزی پیدا نشد')
            char = 0

            
    elif N == "2":
        print(History)
            
    elif N == '3':
        print('برای بازگشت 1 بنویسید.')
        Add = input("اضافه کنید:")
        if Add == '1':
            M = 0
        else:
            Add_code = input("کد متن:")
            if Add_code in Bank_code:
                print('خطا؟ : این کد قبلا استفاده شده!')
            else:
                Bank_code.append(Add_code)
                Bank.append(Add)
            print("متن با موفقیت ثبت شد")
    elif N == '4':
        print("کد متن را وارد کنید")
        print('برای بازگشت 1 بنویسید.')
        C = input("کد:")

        if C == '1':
            M = 0
        else:
            if C in Bank_code:
                Index1 = Bank_code.index(C)
                Bank.remove(Bank[Index1])
                Bank_code.remove(C)
                print('متن حذف شد')
            else:
                print("کد موجود نیست")
    elif N == "X" or N == "x":
        print ('به امید سلامتی شما\nخدا نگهدار')
        break
    else:
        print("خطا دوباره وارد کنید")