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

# STRING
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
# kocha=input("Ko'chani nomini kiriting: ")
# mahalla=input("Mahalla nomini kiriting: ")
# tuman=input("Tuman nomini kiriting: ")
# viloyat=input("Viloyat nomini kiriting: ")
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yozing
# print(f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati")
# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang
# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
# print(f"{kocha.title()} ko'chasi, {mahalla.title()} mahallasi, {tuman.upper()} tumani, {viloyat.upper()} viloyati")


# SONLAR
# AMALIYOT
# Quyidagi dasturlarning har birini alohida fayl ko'rinishida yozing va bajaring:
# Foydalanuvchi kiritgan sonning kvadrati va kubini konsolga chiqaruvchi dastur
# son = int(input("Son kiriting, men esa uning kvadrat va kubini hisoblab beraman: "))
# print(f"{son} ning kvadrati {son**2}\n{son} ning kubi {son**3} ")

# Foydalanuvchining yoshini so'rab, uning tug'ilgan yilini hisoblab, konsolga chiqaruvchi dastur
# yosh = int(input("Siz yoshingizni ayting men esa sizni nechanchi yilda tugilganingizni aytaman: "))
# print("Siz",2024-yosh, "yilda tug'ilgansiz!")

# Foydalanuvchidan ikki son kiritshni so'rab, kiritilgan sonlarning yig'indisi, ayirmasi, ko'paytmasi va bo'linmasini chiqaruvchi dastur
# kirish = input("Siz ikta son kiritasiz, men esa bu sonlar ustida 4 ta asosiy matematik amallarni bajaraman!(Davom ettirish uchun 'Enter' ni bosing)")
# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))
# print(f"{son1} + {son2} = {son1+son2}")
# print(f"{son1} - {son2} = {son1-son2}")
# print(f"{son1} * {son2} = {son1*son2}")
# print(f"{son1} / {son2} = {son1//son2}")


# LISTS
# AMALIYOT
# Quyidagi mashqlarni bajaring:
# ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# ismlar = ['Sardor', 'Boymurod', 'Davlatyor']
# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring: 
# print("Assalomu alaykum do'stim", ismlar[0])
# print("Assalomu alaykum do'stim", ismlar[1])
# print("Assalomu alaykum do'stim", ismlar[2])

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik). 
# sonlar = [5, 3.1415, -2, 22]
# print(sonlar)
# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
# sonlar[0] = 15
# sonlar[1] = sonlar[1]**2
# sonlar[3] = sonlar[3] - sonlar[0]
# del sonlar[2]
# print(sonlar)  

# t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning,
# ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
# t_shaxslar = ["Imom Buxoriy", "Al-Xorazmiy", "Abdulla Qodiriy"]
# z_shaxslar = ["Anvar Narzullayev", "Timur Adhamov", "Abdulloh domla"]
# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (
# .pop()), quyidagi ko'rinishda chiqaring:
# print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan,\n\
# zamonimiz shaxslaridan esa {z_shaxslar.pop(2)} bilan\n\
# suxbat qurishni xoxlar edim")

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
# friends = []
# friends.append("Sardor")
# friends.append("Boymurod")
# friends.append("Davlatyor")
# friends.append("Husan")
# print(friends)

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
# friends.remove("Davlatyor")
# print(friends)

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
# friends.insert(0, 'Xasan')
# friends.insert(3, "Davlatyor")
# friends.insert(-1, 'Zohirjon')
# print(friends)

# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan 
# do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
# mehmonlar = []
# mehmonlar.append(friends.pop(1))
# mehmonlar.append(friends.pop(-1))
# mehmonlar.append(friends.pop(3))
# print("\n Kelgan mehmonlar: ",mehmonlar)


#08 RO'YXATLAR BILAN ISHLASH
# AMALIYOT
# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ["O'zbekiston", "Saudiya Arabistoni", "Germaniya", "Yaponiya", "Malaysiya", "Indonesiya"]
# Ro'yxatning uzunligini konsolga chiqaring
# print(len(davlatlar))

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# print(sorted(davlatlar))
# print(sorted(davlatlar, reverse=True))
# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring

# Asl ro'yxatni qaytadan konsolga chiqaring
# print(davlatlar)

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# davlatlar.reverse()
# print(davlatlar)

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
sonlar = list(range(120,1200,2))

# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# print(sum(sonlar))

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# print(max(sonlar)-min(sonlar))

# Ro'yxatdagi elementlar sonini hisoblang
# print(len(sonlar))

# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# boshi = sonlar[:20]
# urta = sonlar[260:280]
# oxiri = sonlar[-20:]
# print(boshi+urta+oxiri)

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ["osh", "manti", "somsa", "beshbarmoq", "lag'mon"]

# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = []

# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.append(taomlar.pop(0))
nonushta.append(taomlar.pop(1))
nonushta.append("saryog'")
nonushta.append("qaymoq")
print(nonushta)
# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
# nonushta[0] = 'qaymoq va non' # We all knew that will be the error
print(nonushta)