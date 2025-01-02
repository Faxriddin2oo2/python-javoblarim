# Bismillah
"""
Created on Thu Jul  4 12:16:04 2024

@author: Faxriddin
"""

# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. 
#Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
shoir1 = {
    "ism" : "ahad qayum",
    't_yil' : 1984,
    "til" : "uzbek",
    'millati': "o'zbek",
    'asarlar' : ["Xo'rlangan", "do'st", "vatan"]
    }

shoir2 = {
    "ism" : "Pushkin",
    't_yil' : 1765,
    "til" : "rus",
    'millati': "gruzin",
    "asarlar" : ["sevgi", 'hayot', 'tabiat']
    }

shoir3 = {
    "ism" : "Lermontov",
    't_yil' : 1805,
    "til" : "rus",
    'millati': "rus" ,
    'asarlar' : ['borodino', 'cherkeslar', 'kavkaz asirasi']
    }
shoirlar = [shoir1, shoir2, shoir3]
# for shoir in shoirlar:
#     print(f"{shoir['ism'].title()} {shoir['t_yil']}da tug'ilgan, \
# millati - {shoir['millati'].title()} va {shoir['til']} tilida yozgan")


# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. 
# For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
# for shoir in shoirlar:
#     asarlar = shoir['asarlar']
#     ism = shoir['ism']
#     print(f"{ism.title()}ning mashxur asarlari:")
#     for asar in asarlar:
#         print(asar.upper()) 

# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, 
# uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.
# kinolar = {
#     "sardor": ["bo'rilar", "sarviqomat dilbarim", "mendirman jaloliddin" ],
#     "zohirjon" : ["oxirgi samuray", "batman", "forsaj 7"],
#     "faxriddin" : ["interstellar", "yashil kitob", "forest gamp"]
#     }
# for ism,kino in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli filmlari:")
#     for k in kino:
#         print(k.upper(), end= ' ')


# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. 
# Har bir davlat haqida ma'lumotni konsolga chiqaring.

davlatlar = {
    "O'zbekiston" : { "til" : "uzbek",
                     'aholi' : 38_000_000_000,
                     "din" : "islom"
        },
    "Russia" : { "til" : "rus",
                'aholi' : 200_000_000_000,
                "din" : "xristian"
        },
    "Hindiston" : {"til" : "hind",
                  'aholi' : 2_000_000_000_000,
                  "din" : "hinduism"
        }
    }

# for davlat,info in davlatlar.items():
#     print(f"{davlat}da aloqa tili - {info['til'].title()} tili\n"
#           f"Aholisi qariyb - {info['aholi']}\n"
#           f"Va aholisining katta qismi {info['din'].title()} dinida")


# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering.
#  Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
country = input("Davlatni nomini kiriting: ")
if country in davlatlar:
    info = davlatlar[country]
    print(f"{country}da aloqa tili - {info['til'].title()} tili\n"
        f"Aholisi qariyb - {info['aholi']}\n"
          f"Va aholisining katta qismi {info['din'].title()} dinida")
else:
        print("Bizda bu davlat haqida ma'lumot yo'q")











