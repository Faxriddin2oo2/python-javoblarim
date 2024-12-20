# InshaAllah today 19.12.2024 this is will be start of my path in data science sphere
#03 PRINT(), SINTEKS VA ARIFMETIK AMALLAR

# Quyidagi matnni aynan shunday ko'rinishda konsolda chiqaring:
# "Nexia", "Tico", 'Damas' ko'rganlar qilar havas
# print('"Nexia",', '"Tico",',"'Damas'", "ko'rganlar qilar havas")

# Quyidagi misollarga yechimni Pythonda chiqaring. Har bir misoldan avval misol matnini izoh ko'rinishida yozing:
# 5 ning 4-darajasini toping
# print("5 ning 4-darajasi:", 5**4)

# 22 ni 4 ga bo'lganda qancha qoldiq qoladi?
# print("22 ni 4 ga bo'lganda:", 22%4, "qoldiq qoladi")

# Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
# print("Tomonlari 125 ga teng kvadratning yuzi:", 125**2, ", perimetri esa:", 125*4)

# Diametri 12 ga teng bo'lgan doiraning yuzini toping  (π=3.14 deb oling)
# print("Diametri 12 ga teng bo'lgan doirani yuzi:", 3.14*((12/2)**2))

# Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping (Pifagor teoremasidan foydalaning)
# print("Katetlari 6 va 7 bo'lgam to'g'ri burchakli uchburchakning gipotenuzasi:", (6**2+7**2)**0.5)


# AMALIYOT
# Quyidagi mashqlarni bajaring:
# "Hello World!" matnini yangi o'zgaruvchiga yuklang va print() yordamida konsolga chiqaring
# x = "Hello World!"
# print(x)

# xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring, keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.
# xabar="Assalomu alaykum"
# print(xabar)
# xabar="Vaaleykum assalom"
# print(xabar)

# class den nomlangan o'zgaruvchi yarating, unga biror qiymat bering va konsolga chiqaring (siz kutgan natija chiqdimi?)
# class=123
# print(class) # Bu xato bo'lishi oydin masala edi

# Quyidagi kodni bajaring:
# radius = 5
# pi = 3.14159
# aylana_yuzi = pi * radius**2
# print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)


# AMALIYOT
# Quyidagi mashqlarni bajaring:
# Quyidagi o'zgaruvchilarni yarating: 
# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor" 
# viloyat="Samarqand"
# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
kocha=input("Ko'chani nomini kiriting: ")
mahalla=input("Mahalla nomini kiriting: ")
tuman=input("Tuman nomini kiriting: ")
viloyat=input("Viloyat nomini kiriting: ")
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
# print(f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati")
# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
print(f"{kocha.title()} ko'chasi, {mahalla.title()} mahallasi, {tuman.upper()} tumani, {viloyat.upper()} viloyati")
