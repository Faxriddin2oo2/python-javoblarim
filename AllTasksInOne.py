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
# davlatlar = ["O'zbekiston", "Saudiya Arabistoni", "Germaniya", "Yaponiya", "Malaysiya", "Indonesiya"]
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
# sonlar = list(range(120,1200,2))

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
# taomlar = ["osh", "manti", "somsa", "beshbarmoq", "lag'mon"]

# nonushta degan yangi ro'yxatga taomlardan nusxa oling
# nonushta = []

# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
# nonushta.append(taomlar.pop(0))
# nonushta.append(taomlar.pop(1))
# nonushta.append("saryog'")
# nonushta.append("qaymoq")
# print(nonushta)
# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
# nonushta = tuple(nonushta)
# nonushta[0] = 'qaymoq va non' # We all knew that will be the error
# print(nonushta)


# FOR LOOP
# AMALIYOT
# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# ismlar = ["Sardor", "Boymurod", "Davlatyor", "Zohirjon", "Husan"]
# for ism in ismlar:
#     print(f"Assalomu aleykum, hush kelibsan {ism}!")
# print(f"Kod {len(ismlar)} marta takrorlandi")
# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# sonlar = range(11,100,2)
# for son in sonlar:
#     print(f"{son} ning kubi {son**3}")

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# kinolar = []
# print("Sevimli 5 ta kinongizni kiriting!")
# for n in range(5):
#     kinolar.append(input(f"Sizga yoqadigan {n+1} chi kinoni kiriting: "))
# print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, 
# va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
# son = int(input("Bugun nechta odam bilan ko'rishdingiz?\n>>>"))
# odamlar = []
# print(f"Shu {son} ta odamni ismlarini ayting")
# for n in range(son):
#     odamlar.append(input(f"Ko'rishganiz {n+1} chi odamiz: "))

# print("Siz ko'rishgan odamlar: ",odamlar)


# if/else 
# AMALIYOT
# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. 
# GM uchun ikkala harfni katta qiling.
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == "gm":
#         print(car.upper())
#     else:
#         print(car.title())

# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
# for car in cars:
#     if car != "gm":
#         print(car.title())
#     else:
#         print(car.upper())

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" 
# xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
# savol = input("Iltimos ismingizni kiriting: ")
# if savol.lower() == 'admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {savol.title()}")

# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# son1 = int(input("Iltimos birinchi sonni kiriting: "))
# son2 = int(input("Iltimos ikkinchi sonni kiriting: "))
# if son1 == son2:
#     print("Bu ikta son teng ekan!")

# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
# son = int(input("Istalgan sonni kiriting: "))
# if son < 0:
#     print("Bu manfiy son")
# else:
#     print("Bu musbat son")

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
# if son >= 0:
#     print(f"Bu {son} ning ildizi: {son**0.5}")
# else:
#     print("Iltimos musbat son kiriting!")


# Bir nechta shartlarni tekshirish
# AMALIYOT
# Quyidagi dasturlarni alohida fayllarga yozing va bajaring:
# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
# son = int(input("Juft son kiriting: "))
# if son%2 == 0:
#     print("Rahmat!")
# else:
#     print("Bu juft son emas")

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
# Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
# Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm
# yosh = int(input("Iltimos yoshingizni kiriting: "))
# if yosh < 4 or yosh>60:
#     narx = 'bepul'
# elif yosh < 18:
#     narx = 10000
# else:
#     narx = 20000
# print(f"Sizga muzeyga kirish {narx} bo'ladi")

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# print("Siz menga ikta son bering va men ularni solishtiraman!")
# son1 = int(input("Birinchi sonni kiriting: "))
# son2 = int(input("Ikkinchi sonni kiriting: "))
# if son1 > son2:
#     print(f"Birinchi son katta!--> {son1} > {son2}")
# elif son1 < son2:
#     print(f"Ikkinchi son katta!--> {son1} < {son2}")
# else:
#     print("Bu sonlar teng!")

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting.
#  Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. 
# Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, 
# "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ['guruch', 'sabzi', 'piyoz', 'yo\'g', 'go\'sht', 'qalampir', 'zira', 'olma', 'chimchi', 'suv']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1} chi mahsulotni soling: "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"{mahsulot.title()} bor bizda")
#     else:
#         print(f"Afsuski {mahsulot} bizda yo'q")

# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
# Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi, bor_mahsulotlar degan ro'yxatga, 
# do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, 
# "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas == []:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# else:
#     print("\nQuyidagi mahsulotlar do'konimizda yo'q: ")
#     for i in mavjud_emas:
#         print(i)

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
# Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. 
# Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
# foydalanuvchilar = ['magneto', 'abu123', 'umar', 'faxriddin', 'ajdar jangchisi']
# savol = input("Yangi login kiriting:\n>>>")
# if savol.lower() in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz, {savol.title()}")

# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 
# son = int(input("Son kiriting: "))
# for n in range(2,11):
#     if son%n==0:
#         print(f"{son} {n} ga qoldiqsiz bo'linadi")


# DICTIONARY
# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). 
# Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan
# otam = {
#     "ism" : "Sharofiddin",
#     "t_yil" : 1970,
#     "t_joy" : "Sariosiyo"
# }
# print(f"Mening dadamning ismlari {otam["ism"]}, ular {otam["t_yil"]} yilda {otam['t_joy']} tumanida da tug'ilganlar")

# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
# Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh
# oilam_taomlari= {
#     "dadam" : "palov",
#     "ayam" : "baliq",
#     "akam" : "manti",
#     "men" : "osh",
#     "singlim" : "pizza"
# }
# print(f" Dadamning sevimli taomlari {oilam_taomlari['dadam']}")
# print(f" Ayamning sevimli taomlari {oilam_taomlari['ayam']}")
# print(f" Akamning sevimli taomlari {oilam_taomlari['akam']}")
# for odam, taom in oilam_taomlari.items():
#     print(f" {odam.title()}ning sevimli taomlari {taom}")

# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) 
# va har birining qisqacha tarjimasini yozing.
# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, 
# "Bunda so'z mavjud emas" degan xabarni chiqaring.
# izohli_lugat = {
#     "int":"Butun sonlar",
#     "float" : "O'nlik sonlar",
#     "string" : "Tekst malumotlar turi",
#     "if" : "Agar sharti",
#     "else": "if ning tugatuvchi sherigi",
#     "dictionary" : "Lug'at",
#     "list" : "Ro'yxat",
#     "for" : "Sikl",
#     "print" : "Konsolga natijani chiqarish",
# }

# savol = input("Biron bir python terminini kiriting, men esa agar bilsam sizga uni nimaligini aytaman.\n>>>")
# javob = izohli_lugat.get(savol.lower(),"Bunday so'z mavjud emas")
# print(f"{savol.lower()} - {javob}, degani")

# if savol.lower() in izohli_lugat.keys():
#     print(izohli_lugat[savol.lower()])
# else:
#     print("Men bu so'zni Pythonda borligini bilmas ekanman!")
# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.


#15 LUG'AT ELEMENTLARI BILAN ISHLASH
# # AMALIYOT
# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, 
# alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
# for keys, values in sorted(izohli_lugat.items()):
#     print(f"{keys} ning ma'nosi - {values.capitalize()}")

# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
# poytaxtlar = {
#     "O'zbekiston" : "Toshkent",
#     "Russia" : "Moskow",
#     "USA" : "Washington D.C.",
#     "Spain" : "Madrid",
#     "Saudia Arabia" : "Ar-Riyadh",
#     "Italy" : "Rome",
#     "France" : "Paris",
#     "Germany" : "Berlin"
# }
# print("Dunyo davlatlari: ")
# for davlat in poytaxtlar.keys():
#     print(davlat.upper())
# print("Davlatlarning poytaxtlari: ")
# for poytaxt in sorted(poytaxtlar.values()):
#     print(poytaxt)
# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. 
# Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
# savol = input("Siz menga davlatning nomini ayting, agar men bilsam uning poytaxtini aytaman. \n>>>")
# if savol.capitalize() in poytaxtlar.keys():
#     print(f"{savol.capitalize()} ning poytaxti {poytaxtlar[savol.capitalize()]}")
# else:
#     print("Bizda bunday ma'lumot yo'q")

# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
# menu = {
#     "osh" : 18000,
#     "lag'mon" : 22000,
#     "manti" : 5000,
#     "gumma" : 4000,
#     "beshbarmoq": 80000,
#     "sho'rva" : 20000,
#     "bifshteks" : 25000,
#     "norin" : 28000,
#     "moshkichiri" : 60000,
#     "somsa" : 7000,
#     "kabob" : 12000
# }
# buyurtma = []
# for n in range(3):
#     buyurtma.append(input(f"Iltimos {n+1} chi taomni tanglang\n>>>"))
# for taom in buyurtma:
#     if taom in menu.keys():
#         print(f"{taom.capitalize()} ning narhi - {menu[taom]} so'm")
#     else:
#         print(f"Afsuski bizda {taom} yo'q")


#16 NESTING
# AMALIYOT
# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang,
#  va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
#            'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona",
#            'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#            }
# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

# for shaxs in shaxslar:
#     print(f"{shaxs['ism']}, {shaxs['tyil']} yil {shaxs['tjoy']}da tug'ilgan va " 
#         f"{shaxs['vyil']-shaxs['tyil']} yil umr ko'rib {shaxs['vyil']} yilda vafot topgan")

# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     asarlar = shaxs['asarlar']
#     print(f"\n{ism} ning mashxur asarlari: ")
#     for asar in asarlar:
#         print(asar)

# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. 
# Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang. Natijani konsolga chiqaring.
# yaqinlar = {
#     'Sardor' : [],
#     'Fazliddin' : [],
#     'Boymurod' : [],
# }
# for ism, film in yaqinlar.items():
#     for n in range(3):
#         savol = input(f"{ism} yaxshi korgan {n+1} chi filmingizni yoki serialingizni ayting\n>>>")
#         yaqinlar[ism].append(savol)

#     print(f"{ism} ning yaxshi ko'rgan film va seriallar: ")
#     for kino in film:
#         print(kino.capitalize())

# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. 
# Har bir davlat haqida ma'lumotni konsolga chiqaring.
# davlatlar = {
#     "o'zbekiston":{'poytaxt':"toshkent",
#                    'maydon':448978,
#                    'aholi':33_000_000,
#                    'pul birligi':"so'm"
#                    },
#     "rossiya":{'poytaxt':"moskva",
#                    'maydon':17_098_246,
#                    'aholi':144_000_000,
#                    'pul birligi':"rubl"
#                    },
#     "aqsh":{'poytaxt':"vashington",
#                    'maydon':9_631_418,
#                    'aholi':327_000_000,
#                    'pul birligi':"dollar"},
#     "malayziya":{'poytaxt':"kuala-lumpur",
#                    'maydon':329750,
#                    'aholi':25_000_000,
#                    'pul birligi':"rinngit"}
#     }

# for davlat, info in davlatlar.items():
#     print(f"\n{davlat.capitalize()} ning poytaxt {info['poytaxt'].title()}\nHududi: {info['maydon']}\nAholisi: {info['aholi']}\nPul birligi: {info['pul birligi']}")

# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. 
# Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
# savol = input("Davlatni kiriting, men sizga u haqida ma'lumot beraman\n>>>")
# if savol.lower() in davlatlar.keys():
#     info = davlatlar[savol.lower()]
#     print(f"\n{savol.capitalize()} ning poytaxt {info['poytaxt'].title()}\nHududi: {info['maydon']}\nAholisi: {info['aholi']}\nPul birligi: {info['pul birligi']}")
# else:
#     print(f"Afsuski, bizda {savol.title()} haqida ma'lumot yo'q")


#17 WHILE TSIKLI
# AMALIYOT
# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
# while True:
#     savol = input("O'ziz yaxshi korgan kitobni kiriting(Agar to'xtatishni istasangiz 'stop' deb yozing):\n>>>")
#     if savol == 'stop':
#         break
# print("Dastur to'xtatildi!")

# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
# Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin 
# (ikkita shartni ham tekshiring).
# ishora = True
# while ishora:
#     yosh = int(input("Yoshingiz nechida: "))
#     if yosh <= 7 and yosh > 0:
#         narh = 2000
#     elif yosh < 18:
#         narh = 3000
#     elif yosh < 65:
#         narh = 10000
#     else:
#         narh = 'bepul'
#     print(f"Siz uchun muzeyga kirish - {narh}")
#     savol = input("Yana davom etishni hohlaysizmi? (yes/no)\n>>>")
#     if savol == 'yes':
#         continue
#     else:
#         ishora = False
# Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)


#18 WHILE, RO'YXATLAR VA LUG'ATLAR
# AMALIYOT
# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
# buyurtma = []

# while True:
#     savol = input("Taomni nomini kiriting(agar to'xtatmoqchi bo'lsangiz 'exit' deb yozing): ")
#     if savol != 'exit':
#         buyurtma.append(savol)
#     else:
#         break
# print(buyurtma)

# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
# e_bozor = {}
# print("Keling bozorlik qilamiz!")
# while True:
#     mahsulot = input(f"Mahsulotni kiriting: ")
#     kg = float(input(f"{mahsulot.title()} dan nechi kg olmoqchisiz: "))
#     narh = int(input(f"{mahsulot.title()}ning narhini kiriting: "))
#     e_bozor[mahsulot] = narh * kg
#     savol = input("Yana mahsulot kiritasizmi?(yes/no)\n>>>")
#     if savol == 'yes':
#         continue
#     else:
#         break

# print("\nSiz tanlagan mahsulotlar: ")
# for mahsulot, narh in e_bozor.items():
#     print(f"{mahsulot.title()} {narh} so'mlik")

# print(f"Umumiy {sum(e_bozor.values())} so'm bo'ldi")

# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring 
# (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahsulot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
# buyurtmalar = ['olma','anjir','uzum','qovun']
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         print(f"{buyurtma.title()}ning narhi {mahsulotlar[buyurtma]}")
#     else:
#         print(f"Afsuski bizda {buyurtma} yo'q")


#19 FUNKSIYA
# AMALIYOT
# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# def info(ism, yosh):
#     return f"Assalomu alaykum {ism.capitalize()}, sizning tug'ilgan yilingiz: {2024-yosh}"

# print(info('faxriddin',22))

# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# def kvadrat_kub(son):
#     return f"{son} ning kvadrati - {son**2}, kubi esa - {son**3}"

# print(kvadrat_kub(5))

# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# def juft_toq(son):
#     if son % 2 == 0:
#         return f"{son} juft son!"
#     else:
#         return f"{son} toq son!"

# print(juft_toq(8))

# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# def bigger(son1, son2):
#     if son1 > son2:
#         max = son1
#     elif son1 < son2:
#         max = son2
#     else:
#         return "Sonlar teng!"
#     return f"{max} kattaroq son!"

# print(bigger(5,7))

# Foydalanuvchidan x va y sonlarini olib, x darajasida y ni qaytaradigan function yarating
# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# def daraja(x,y=2):
#     """x darajasida y ni qaytaradigan function"""
#     return f"{x} ning {y} chi darajasi - {x**y}"

# print(daraja(9))

# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
# def bolinish_alomatlari(son):

#     for n in range(2, 11):
#         if son % n == 0:
#              print(f"{son} {n} ga qoldiqsiz bo'linadi")

# bolinish_alomatlari(70)


#20 QIYMAT QAYTARUVCHI FUNKSIYA
# AMALIYOT
# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. 
# Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
# def info(ism, familiya, t_yil, t_joy, email, telefon):
#     full_info = {}
#     full_info['ism'] = ism
#     full_info['familiya'] = familiya
#     full_info['t_yil'] = t_yil
#     full_info['t_joy'] = t_joy
#     full_info['email'] = email
#     full_info['telefon'] = telefon
#     full_info['yosh'] = 2024-t_yil
#     return full_info

# print(info('Faxriddin', 'Teshaboyev', 2000, 'Paris', 'fax123@gmail.com',"+009334221"))

# Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring. 
# Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
# def info():
#     mijozlar = []
#     full_info = {}
#     while True:
#         ism = input("Ismingizni kiriting: ")
#         full_info['ism'] = ism

#         familiya = input("Familiyangizni kiriting: ")
#         full_info['familiya'] = familiya

#         t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
#         full_info['t_yil'] = t_yil

#         t_joy = input("Tug'ilgan joyingizni kiriting: ")
#         full_info['t_joy'] = t_joy

#         email = input("Emailingizni kiriting: ")
#         full_info['email'] = email

#         telefon = input("Telefon raqamingizni kiriting: ")
#         full_info['telefon'] = telefon
#         full_info['yosh'] = 2024-t_yil

#         mijozlar.append(full_info)
#         savol = input("Yana odam qo'shasizmi(yes/no)?: ")
#         if savol == 'no':
#             break
#     return mijozlar

# print(info())

# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing
# def eng_katta(son1, son2, son3):
#     if son1 > son2 and son1 > son3:
#         max = son1
#     elif son2 > son3 and son2 > son1:
#         max = son2
#     else:
#         max = son3
#     return max

# print(eng_katta(4,9,7))    

# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing
# def data(radius):
#     aylana_info = {}
#     pi = 3.14
#     aylana_info['radius'] = radius
#     aylana_info['diametr'] = radius * 2
#     aylana_info['perimetr'] = 2*pi*radius
#     aylana_info['yuzi'] = pi*(radius**2)
#     return aylana_info

# print(data(3))

# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n == 1:
#             tub = False
#         elif n == 2:
#             tub = True
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)

#     return tub_sonlar

# print(tub_sonlar_top(4,15))

# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.  
# Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. 
# Bunda boshlang’ish had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
def fibonacci(n):
    my_list = []
    for x in range(n):
        if x == 0 or x == 1:
            my_list.append(1)
        else:
            my_list.append(my_list[x - 1] + my_list[x - 2])
    return my_list
print(fibonacci(5))