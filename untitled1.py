import datetime

D1 = datetime.datetime.now()


print(D1)

karmandan = ["محمدی","بازرگان","مجدی","علوی"]
karmandan_codes = ["0","120804","121899","120989","120100"]



person1 = set()
Time1 = []

person2 = set()
Time2 = []

while (True):
    t1 = datetime.datetime.now()
    t2 = t1.hour
    t3 = t1.minute
    t4 = t1.second
    name = (input("ورود یا خروج کاربر *** نام کاربری : "))
    if name in karmandan_codes:
        if name in person1:
            person2.add(name)
            Time2.append(f"{t2}:{t3}:{t4}")
        elif name == "0":
            break
        else :
            person1.add(name)
            Time1.append(f"{t2}:{t3}:{t4}")
    else:
        print('کارمندی با این نام کاربری طوجود ندارد')

    


    
#------------------------------------------------------------------------------------------------------------------------
N = str()



List1 = list(person1)
List2 = list(person2)

for i in range(len(List1)):
    print(f"{karmandan[i]}, ورود: {Time1[i]}")
print("------------------------------------------------")
for i in range(len(List2)):
    print(f"{karmandan[i]}, خروج: {Time2[i]}")

S1 = set(person1)
S2 = set(person2)
   
if person1 != person2:
    S3 = S1.difference(S2)
    D3 = list(S3)
    for i in range(len(S3)):
        N1 = N.join(D3[i])
        M1 = karmandan_codes.index(N1)
        M1 -= 1
        print(f"کارمند {karmandan[M1]} ورود یا خروجشان را ثبت نکردند")
        N1 = ""
        N = ""
