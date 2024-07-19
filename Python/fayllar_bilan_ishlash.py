# Bismillah
"""
Created on Fri Jul 19 18:51:44 2024

@author: Faxriddin
"""


# From lesson
# with open("pi.txt") as fayl:
#     pi = fayl.read()
    # print(pi)
    # fayl.close()

# pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
# pi = pi.replace('\n', '') # qator tashlash belgisini almashtiramiz
# pi = float(pi) # matnni float (o'nlik) songa o'tkazamiz
# print(pi)


# PAPKA ICHIDAGI FAYLLARNI OCHISH
# with open('data/pi.txt') as fayl:
#     pi = fayl.read()
# with open('data/pi.txt') as fayl:
#     pi = fayl.read()
#     print(pi)
# filename = 'data/talabalar.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)

# FAYLNI QATORMA-QATOR OʻQISH
# filename = 'talabalar.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)
# with open(filename) as file:
#     talabalar = file.readlines()

# print(talabalar)



# FAYLGA YOZISH
# faylnomi = 'data/uquvchilar.txt' # ochilayotgan (yaratilayotgan) fayl nomi
# with open(faylnomi, 'w') as fayl:
#     fayl.write('faxriddin teshaboyev') # faylga yozilayotgan ma'lumot


# faylnomi = 'data/new_file.txt'
# ism = 'Olimjon Hasanov '
# tyil = 2005
# with open(faylnomi, 'w') as fayl:
#     fayl.write(ism + '\n')
#     fayl.write(str(tyil) + '\n')
    
# with open(faylnomi, 'a') as fayl:
#     fayl.write('Alijon Valiev\n')
#     fayl.write('2000')




# O'ZGARUVCHILARNI FAYLDA SAQLASH
# import pickle

# talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs':2}
# talaba2 = {'ism':'hasan', 'familiya':'valiyev', 'tyil':2004, 'kurs':1}

# with open('info','wb') as file:
#     pickle.dump(talaba1,file)
#     pickle.dump(talaba2, file)
    
    
# # with open('info','rb') as file:
# #     talaba1 = pickle.load(file)
#     # talaba2 = pickle.load(file)
# with open('info', 'rb') as file:
#     talaba1 = pickle.load(file)
#     talaba2 = pickle.load(file)
# print(talaba1)



# PRACTICE
# Bugun o'rgangan narsalaringizni matnga yozing va matnni Python yordamida oching
# with open('data/dars.txt') as file:
#     darslik = file.read()
#     print(darslik)
#     file.close()


# Quyidagi pi_million_digits.txt faylini yuklab oling (faylda π  soni nuqtadan so'ng million xona aniqlik bilan yozilgan). 
# Tug'ilgan kunim pi da bormi?
import pickle

# with open('data/pi_million_digits.txt') as file:
#     pi = file.read()
# pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
# pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
# pi = pi.replace(' ','')

# bdate = '14159265'
# print(bdate in pi)

# faylnomi = 'data/new_file.txt'
# ism = 'Olimjon Hasanov '
# tyil = 2005
# with open(faylnomi, 'w') as fayl:
#     fayl.write(ism + '\n')
#     fayl.write(str(tyil) + '\n')
    
# with open(faylnomi, 'a') as fayl:
#     fayl.write('Alijon Valiev\n')
#     fayl.write('2000')


faylnomi = "data/malumotnoma.txt"
ism = input("Ismingizni kiriting:")
familiya = input("Familiyangizni kiriting: ")
tyil = int(input("Tugilgan yilingiz? : "))
with open(faylnomi, 'a') as fayl:
    fayl.write(ism + '\n')
    fayl.write(familiya + '\n')
    fayl.write(str(tyil) + '\n')





















