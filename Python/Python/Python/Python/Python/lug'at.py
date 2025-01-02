# Bismillah
"""
Created on Mon Jul  1 18:17:04 2024

@author: Faxriddin
"""
# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting 
# (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring
# otam = {"ism":'Sharofiddin', 't_yil': 1970, 'manzil': "Sarasio"}
# print(f"{otam['ism']}, {otam['t_yil']}da {otam['manzil']}da tug'ilgan")


# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
# Kamida uch kishining sevimli taomini konsolga chiqaring
# sevimli_taomlar = {
#     'dadam': 'osh',
#     'ayam' : 'baliq',
#     'akam' : 'manti',
#     'singlim': 'shirinlik',
#     'men' : 'palov'
#     }
# print(f"Dadamning sevimli taomlari {sevimli_taomlar['dadam']}")


# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting 
# (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
python_izohli_lugati = {
    'int' : 'butun son',
    'float' : 'xar qanday son',
    'string' : 'matn',
    'if' : 'agar',
    'else' : 'shuningdek',
    'list' : "ro'yxat",
    'length' : 'uzunlig',
    'max' : 'katta qiymat',
    'min' : 'kichik qiymat',
    'sum' : "yig'indi"
    }

# kalit = input("Kalit so'zni kiriting: ").lower()
# print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")