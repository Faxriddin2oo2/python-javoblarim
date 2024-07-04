# Bismillah
"""
Created on Thu Jul  4 14:22:13 2024

@author: Faxriddin
"""


# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
# print("Assalomu alaykum buyurtamalaringizni qabul qilishga tayyormiz!")
# buyurtmalar = []
# n = 1
# while True:
#     savol = f"{n}chi buyurtmani kiriting:"
#     buyurtma = input(savol)
#     buyurtmalar.append(buyurtma)
#     javob = input("Yana qo'shasizmi? (ha/yo'q)")
#     if javob == 'ha':
#         n+=1
#     else:
#         break




# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
# print("Elektron bozor uchun mahsulotlar ro'yhatini tuzamiz:")
# mahsulotlar = {}
# n = 1
# ishora = True
# while ishora:
#     mahsulot = input(f"{n}chi mahsulotni kiriting:")
#     narh = input(f"{mahsulot.title()}ning narhini kiriting:")
#     mahsulotlar[mahsulot] = int(narh)
#     javob = input("Yana mahsulot kiritasizmi? (ha/yo'q)")
#     if javob == 'ha':
#         n+=1
#     else:
#         ishora = False


# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan 
# solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda 
#                "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")