ali_age = 14
ali_chashm = "آبی"
ali_ghad = 160
mahdi_age = 15
mahdi_chashm = "سبز"
mahdi_ghad = 165
hasan_age = 17
hasan_chashm = "سیاه"
hasan_ghad = 180 # ویژگی ها
age = int(input("لطفا سن را وارد کنید:"))
chashm = input("لطفا رنگ چشم را وارد کنید:")
ghad = int(input("لطفا قدتان را وارد کنید:")) # اطلاعات کاربر
if age == ali_age and chashm == ali_chashm and ghad == ali_ghad:
    print("شما علی هستید")
elif age == mahdi_age and chashm == mahdi_chashm and ghad == mahdi_ghad:
    print("شما مهدی هستید")
elif age == hasan_age and chashm == hasan_chashm and ghad == hasan_ghad:
    print("شما حسن هستید")#شرط ها
else:
    print("کاربر ناشناس است")