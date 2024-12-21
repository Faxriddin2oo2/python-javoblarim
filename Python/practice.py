# bismillah
"""
Created on Sun Jun 30 22:18:12 2024

@author: Faxriddin
"""


# Даны два целых числа A и B (при этом A ≤ B). Выведите все числа от A до B включительно.
# a = int(input("Введите маленькое число: "))
# b = int(input("Введите большое число: "))
# print(list(range(a,(b+1))))

# a = int(input())
# b = int(input())
# for i in range(a,b+1):
#      print(i)


# По данному натуральном n вычислите сумму КВАДРАТОВ
# n = int(input())
# a = 0
# for i in range(n + 1):
#      a += i ** 2
# print(a)

# По данному натуральном n вычислите сумму КВАДРАТОВ
# n = int(input("Sonni kiriting: "))
# a = 0
# for i in range(n+1):
#     a += i**3
# print(f"{n} gacha bo'lgan sonlarning kublari yig'indisi: {a} ga teng") 

# По данному целому неотрицательному n вычислите значение n!
# son = int(input("Musbat son kiriting: "))
# a=1
# for i in range(1,son+1):
#     a *= i
# print(a)
    
# Дано несколько чисел. Вычислите их сумму. Сначала вводите количество чисел N, затем вводится ровно N целых чисел. 
# Какое наименьшее число переменных нужно для решения этой задачи?
# son = int(input("nechta sonning yig`indisini hisoblash kerak>>> "))
# a=0
# for i in range(son):
#     a+= int(input(f"{i + 1} sonning qiymatini kiriting:"))
# print(a)

# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")


mahsulotlar = ['un', "yog", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
savat = []

for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else: 
    print("Savatingiz bo'sh")        








