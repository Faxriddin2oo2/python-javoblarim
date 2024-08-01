# Bismillah
"""
Created on Thu Aug  1 11:26:47 2024

@author: Faxriddin
"""

class Person:
    def __init__(self, ism, familiya, yosh, email, t_kun):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        self.email = email
        self.t_kun = t_kun  
    
    def get_info(self):
        return {
            "First Name": self.ism,
            "Last Name": self.familiya,
            "yosh": self.yosh,
            "Email": self.email,
            "Birth Day": self.t_kun
        }
    
    def get_life_path_number(self):
        day, month, year = self.t_kun
        
        def sum_digits(n):
            return sum(int(digit) for digit in str(n))
        
        day_sum = sum_digits(day)
        month_sum = sum_digits(month)
        year_sum = sum_digits(year)
        
        total_sum = day_sum + month_sum + year_sum
        
        while total_sum > 9:
            total_sum = sum_digits(total_sum)
        
        return total_sum
    
    def get_life_path_description(self):
        life_path_number = self.get_life_path_number()
        descriptions = {
            1: "1 - Rahbar \
            Siz rahbarlikni yaxshi ko'rasiz! Siz innovatsiya ruhiga ega mehnatkashsiz. Sizda ham san’atga ishtiyoq bor. Siz o'zingizni osonlikcha namoyon qila olasiz va har qanday ishda doimo birinchi bo'lishni xohlaysiz. Siz va orzularingizga hech narsa yoki hech kim to'sqinlik qilishiga yo'l qo'ymaysiz. Siz qilishingiz kerak bo'lgan narsa - o'zingiz xohlagan narsaga e'tiboringizni qaratishdir va siz bunga erisha olasiz!\
            Sizning halokatingiz: siz o'zingizni va boshqalarni tanqid qilasiz. Siz dangasalik bilan qattiq ro'za tutasiz va siz o'zingizdan va shuning uchun atrofingizdagilardan eng yaxshisini kutasiz. Sizda o'zini o'ylashga va talabchanlikka moyillik bor. Siz eng zo'r bo'lishga ishtiyoqli bo'lganingiz uchun, ba'zida takabbur yoki maqtanchoq bo'lib qolishingiz mumkin. Ammo bu sizning muvaffaqiyatga erishish uchun tug'ma xohishingiz.",
            2: "2 - Uyg'unlikni izlovchi   \
            Hayotdagi ikkalasini ham o'ylab ko'ring. Ular hamkorlikda va boshqalar bilan ishlashda muvaffaqiyat qozonishadi. Siz juda sezgirsiz va atrofingizdagi dunyo bilan uyg'unsiz. Siz boshqalarga yordam berishda va sahna ortida shizz sodir etishda o'zingizning eng yaxshi shaxsingizsiz. Siz tafsilotlarni yaxshi bilasiz. Sizning e'tiboringiz guruhning katta foydasiga xizmat qilishga qaratilgan bo'lsa, siz gullab-yashnayapsiz. Siz tabiatan tinchlikparvarsiz va har qanday vaziyatning barcha qarashlarini ko'ra olasiz. Bu sizning super kuchingiz.",
            3: "3 - Muloqotchi\
            Siz kuchli tebranish va yuqori darajadagi ijodkorlik va o'zingizni ifoda etishda yashaysiz. Siz mustaqilsiz va muloqotda muvaffaqiyat qozonasiz. Og'zaki va yozma muloqot qobiliyatingiz tufayli siz shoir, yozuvchi, aktyor, rassom yoki musiqachi sifatida juda mos kelasiz. Siz optimistik va juda saxiysiz. Siz har doim har qanday vaziyatda ijobiy tomonlarni topishingiz mumkin. Siz atrofingizdagilarni osongina qulay va qulay his qilasiz. Muvaffaqiyatli bo'lish uchun sizda, xususan, san'atda juda yuqori salohiyat bor va agar siz pul ishlash yo'lini o'ylab topsangiz; siz ajoyib martaba uchun tayyorlanasiz.",
            4: "4 - Jamiyatning band arisi\
            Siz barcha qismlarni birlashtirib, uni ishga tushirishga harakat qilyapsiz. Siz mehnatkash, juda asosli, qat'iyatli, amaliy va intizomlisiz. Siz \"jamiyatning qurilish bloklari\"siz, chunki siz boshqalarning rivojlanishi uchun poydevor yaratasiz. Siz cho'qqiga chiqishning oson yo'lini izlamaysiz va sizni odatda juda tubdan deb hisoblaysiz. Siz tartibli va rejali bo'lishni yaxshi ko'rasiz. Agar rejangiz bo'lsa, hech qachon tugamaydigan ishlar ro'yxatini osongina engishingiz mumkin. Uy - bu sizning boshpanangiz va sizning uyingizdagi hamma narsa joyida bo'lishi kerak. Agar sizning uyingiz tartibsiz va tartibsiz bo'lsa, bu sizning yaxshi ishlamayotganligingizning aniq belgisidir.",
            5: "5 - Erkin qush\
            Sizning raqamingiz erkinlik va o'zgarishdir. Siz hamma narsadan ustun erkinlikni qidirasiz. Siz sarguzashtli bo'lishni yaxshi ko'rasiz va juda oson bezovtalanishingiz mumkin. Siz doimo yo'ldasiz, hayotingizda o'zgarish va xilma-xillikni xohlaysiz. Siz yangi odamlar bilan tanishishni, yangi narsalarni sinab ko'rishni va doimo hozirgi paytda yashashni yaxshi ko'rasiz. Siz odatda o'zingizning xo'jayiningiz bo'lishni xohlaysiz va ajoyib sayohatchi sotuvchi bo'lasiz. Siz oddiy yoki takroriy narsalarni yoqtirmaysiz, shuning uchun siz doimo yangi narsaga intishingiz kerak. Sizning hayotingiz his-tuyg'ularga bog'liq va tajribaga bo'lgan xohishingiz ko'p jihatdan o'zini namoyon qilishi mumkin.",
            6: "6 - Tarbiyachi\
            Sizda kuchli tug'ma mas'uliyat va xabardorlik tuyg'usi bor, bu sizni tarbiyalashda ajoyib qiladi. Siz oila, uy va jamiyat haqidasiz. Siz mehribon, iliq, rahm-shafqatlisiz va boshqalarni xursand qilishga qiziqasiz. Siz qo'riqchi va provayder sifatida rivojlanasiz. Siz oilangiz va do'stlaringizga xizmat qilishdan boshqa hech narsani yoqtirmaysiz. Sizning ota-onalik instinktlaringiz ham juda kuchli. Siz ajoyib odamsiz va nima qilish kerakligini aytishni yoqtirmaysiz. Siz o'z uyingizni va uning atrofidagilarni boyitish bilan shug'ullanasiz va bu sizga katta quvonch keltiradi.",
            7: "7 - Qidiruvchi \
            Siz juda ma'naviy jihatdan harakatlanasiz va bizning dunyomizdagi kuchga ega bo'lishingiz mumkin. Sizda yuksaklikka erishish potentsialingiz bor va boshqalardan ko'ra boshqacha ruhiy tekislikda yashashingiz mumkin. Sizning raqamingiz yuqoriroq xabardorlik va kengroq nuqtai nazarni beradi. Sizda sirli havo bor, lekin osongina yolg'iz bo'lib qolishingiz mumkin. Siz dono va bilimdonsiz. Siz har doim hamma narsaning haqiqiy ma'nosini va asosiy javobini qidirasiz. Sizda tabiiy go'zallikni yaxshi ko'rasiz: okean, yashil o'tlar, rejalar, gullar va boshqalar. Siz haqiqat izlovchi bo'lish uchun keldingiz. Buni quchoqlang.",
            8: "8 - O'zini namoyon qiluvchi xo'jayin. "
            "Siz kuchsiz va u bilan faxrlanasiz! Sizda xarakterning ajoyib hakami bor va atrofingizdagi odamlarni o'ziga jalb qiladi. Siz biznes yoki siyosiy dunyoda ajoyib rahbar bo'lar edingiz. Sizda muvaffaqiyatga bo'lgan ehtiyoj va muvaffaqiyatga erishish uchun kuchli istak bor. Sizning raqamingiz hokimiyat, moddiy boylik, shuhratparastlik va ehtiyotkorlikni anglatadi. Maqsadlaringizga erishish uchun astoydil harakat qilasiz.",
            9: "9 - Gumanitar\
            Numerologiyada to'qqiz raqam - bu to'liqlik soni. Siz tug'ma etakchisiz va odamlar sizni mas'ul deb o'ylashadi, hatto siz bo'lmasangiz ham. Siz boshqalarga g'amxo'rlik qilasiz, lekin qo'llab-quvvatlash va o'zingizni sevishingiz kerak bo'lganda gapirishingiz kerak. Sizda juda kuchli rahm-shafqat va saxiylik tuyg'usi bor va boshqalarga yordam berish siz uchun juda muhimdir. Sizning saxiyligingiz chegara bilmaydi va siz atrofingizdagi odamlarni juda qulay his qilasiz. Sizning asosiy maqsadingiz yaxshiroq dunyoga intilishdir."
        }
        return descriptions.get(life_path_number, "Unknown life path number")
odam = Person('faxriddin', 'teshaboyev', 21, 'teshaboydinweq1@gmail.com', (4 , 9, 2002))
