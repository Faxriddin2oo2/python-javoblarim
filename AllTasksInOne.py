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
#     "string" : "Teks malumotlar turi",
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