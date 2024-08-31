data_madrak = {'لیسانس','فوق_لیسانس','دکترا'}
data_city = {"تهران","اصفهان","فم"}
data_zaban = {"django","html","bootstrap","python",'java','javascript','php','cpp'}
print({'python', 'django', 'javascript', 'c', 'bootstrap', 'php', 'java', 'cpp', 'html'},{"سیکل",'دیپلم','فوق_دیپلم','لیسانس','فوق_لیسانس','دکترا'})
email = input("لطفا مدرک و نوع زبان مدنظرتان طبق لیست وارد کنید :")
Word = set()

for i in email.split():
    Word.add(i)
mod = data_zaban.intersection(i)
mod2 = data_madrak.intersection(i)
mod3 = data_city.intersection(i)
mod1 = list(mod)
if len(mod1) >= 4 and mod2 != {} and mod3 != {} :
    print('شما تائیدیه اولیه را اخذ کردید')
else :
    print('شما تائیدیه اولیه را اخذ نکردید')