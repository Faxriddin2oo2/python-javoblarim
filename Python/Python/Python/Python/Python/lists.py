# Bismillah
"""
Created on Sat Jun 29 17:24:40 2024

@author: Faxriddin
"""

# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring
# ismlar = ["Sardor", "Zohirjon", "Davlatyor"]
# print("Salom", ismlar[0], "bugun choyxonaga boramizmi?")
# print(ismlar[1],"va", ismlar[2], "lar ham boradimi?")

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
# sonlar = [2, 3, -4, 3.2, 33, 88, 58, 67]

t_shaxslar = ["Abu Bakr Siddiq", "Umar ibn Xattob"]
z_shaxslar = ["Tim Kuk", "Kristofer Nolan"]
# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
# print("Men tarixiy shaxslardan", t_shaxslar.pop(0),"bilan", "\nZamonaviy shaxslardan esa", z_shaxslar.pop(1), "bilan suhbat qurmoqchiman")

# friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
friends = []
friends.append("Jalol")
friends.append("Toxir")
friends.append("Oybek")
friends.append("Hamlet")
friends.append("Sunnat")

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.insert(0, "Amir")
friends.insert(2, "Temur")
friends.insert(-1, "Otabek")

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
# friends.remove('Sunnat')

# Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(5))
mehmonlar.append(friends.pop(3)) 
print("\nKelgan mehmonlar:", mehmonlar)