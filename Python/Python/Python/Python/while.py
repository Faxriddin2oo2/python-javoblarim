# Bismillah
"""
Created on Thu Jul  4 13:39:30 2024

@author: Faxriddin
"""

# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
# kitoblar = "Yaxshi ko'rgan kitobingizni kiriting:"
# kitoblar += "(dasturni to'xtatish uchun 'stop' yozing)"
# savol = ''
# while savol != 'stop':
#     savol = input(kitoblar)
# print("Dastur tugadi")


# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 
# 65 dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. 
# Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
savol = "Yoshingiz nechida: "
savol += " (Agar dasturni to'xtatmoqchi bo'lsangiz 'exit' yoki 'quit' deb yozing)"
yosh = ''
# while yosh != 'exit' or yosh !='quit':
#     yosh = input(savol)
#     if yosh == 'exit' or yosh == 'quit': 
#         break
#     yil = int(yosh)
#     if yil <= 7:
#             narh = 2000
#     elif yil <= 18:
#             narh = 3000
#     elif yil <= 65:
#             narh = 10000
#     else:
#             narh = 0
#     print(f"Muzeyga kirish siz uchun {narh} so'm")
# print("Dastur tugadi!")

# True bilan
# while True:
#     yosh = input(savol)
#     if yosh == 'exit' or yosh == 'quit': 
#         break
#     yil = int(yosh)
#     if yil <= 7:
#             narh = 2000
#     elif yil <= 18:
#             narh = 3000
#     elif yil <= 65:
#             narh = 10000
#     else:
#             narh = 0
#     print(f"Muzeyga kirish siz uchun {narh} so'm")
# print("Dastur tugadi!")


# Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. 
# Xatolarni to'g'rilay olasizmi?
savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = input(savol)
    if qiymat == "Exit":
        break
    if int(qiymat)<0:
        continue
    else:
        ildiz = float(qiymat)**(0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")





























