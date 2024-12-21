# Bismillah
"""
Created on Sun Jul  7 16:05:23 2024

@author: Faxriddin
"""


# import random as r

# def son_top(x):
#     print("Men son o'yladim, topishga harakat qilib ko'ring!")
#     number = r.randint(1, x)
#     guess = 0
#     n = 0
#     while guess != number:
#         n += 1
#         guess = int(input(f"1 dan {x} gacha bo'lgan oraliqda son o'yladim, men o'ylagan sonni toping: "))
#         if guess == number:
#             print(f"To'g'ri! Javobni {n}ta urunishda topdingiz")
#             break
#         if number < guess :
#             print( "Xato, men o'ylgan son bundan kichik. Yana harakat qiling\n>>> ")
#             continue
#         if number > guess :
#             print( "Xato, men o'ylagan son bundan katta. Yana harakat qiling\n>>> " )
#             continue
        



# def son_tanla(y):
#     print("Keling endi siz son o'ylaysiz men topaman")
#     input(f"1 dan {y} oraliqda son o'ylang men uni topaman: ")
#     son = r.randint(1, y)
#     topishga_urunish = r.randint(1,y)
#     s = input(f"Siz tanlagan son: {topishga_urunish}")
#     b = 0
#     while topishga_urunish != son:
#         b += 1
#         a=input("Agar o'ylagan soningizni to'g'ri topgan bo'lsam (T) yozing, agar siz o'ylagan son katta bo'lsa (+) , agar kichik bo'lsa (-) yozing")
#         if a == "T":
#             print(f"Men {b}ta urunishda topdim!,")
#             if b>son_top().n:
#                 print(f"Qoyil siz {son_top.n} urunishda topib yutdingiz!")
#             elif b<son_top.n:
#                 print(f"Men {b}ta urunish bilan topib yutdim!")
#             else:
#                 print("Durrang bo'ldi")
#             break
#         if a == "+":
#             print(r.randint(topishga_urunish,y))
#             continue
#         elif a == "-":
#             print(r.randint(1, topishga_urunish))
#             continue
#         return a
    
# son_top(10)
# son_tanla(10)


# Mentorning varianti
import random

def sontop (x=10):
    tasdifiy_son = random.randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?", end= "")
    taxminlar = 0
    while True:
        taxminlar += 1
        taxmin = int(input(">>>"))
        if taxmin < tasdifiy_son:
            print("Xato. Men o'ylagan son bundan kattaroq. Yana harakat qiling:", end= "")
        elif taxmin > tasdifiy_son:
            print("Xato. Men o'ylagan son bundan kichikroq. Yana harakat qiling:", end= "")
        else:
            break
    
    print(f"Tabriklayman. {taxminlar} ta taxmin bilan topdingiz ")
    return taxminlar


def sontop_pc(x=10):
    input(f"1 dan {x}gacha son o'ylang va istalgan tugmani bosing. Men topaman.")
    quyi = 1
    yuqori = x
    taxminlar = 0
    while True:
        taxminlar += 1
        if quyi != yuqori:
            taxmin = random.randint(quyi, yuqori)
        else:
            taxmin = quyi
        javob = input(f"Siz {taxmin} sonini o'yladingiz: to'g'ri(t),"
                      f"men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)".lower())
        if javob == "-":
            yuqori = taxmin - 1
        elif javob == "+":
            quyi = taxmin + 1
        else:
            break
    print(f"Men {taxminlar} ta taxmin bilan topdim!")
    return taxminlar


def play(x=10):
    yana = True
    while yana:
        taxminlar_user = sontop(x)
        taxminlar_pc = sontop_pc(x)
        
        if taxminlar_user > taxminlar_pc:
            print(f"Men {taxminlar_pc} taxmin bilan topdim va yutdim!")
        elif taxminlar_user < taxminlar_pc:
            print(f"Siz {taxminlar_user} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        yana = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0)"))

play()




























