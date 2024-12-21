# Bismillah
"""
Created on Thu Jul  4 17:13:34 2024

@author: Faxriddin
"""
# Напишите программу, в которой в бексонечном цикле пользователь вводит два числа, а программа выводит их сумму
# print("Kiritgan sonlaringizni yig'indsini hisoblab beradigan dastur!")
# while True:
#     son1 = float(input("Birinchi sonni kiriting: "))
#     son2 = float(input("Ikkinchi sonni kiriting: "))
#     print(f"Bu sonlarni yig'indisi = {son1+son2}")
#     savol = input("Yana amal bajarishni xoxlaysizmi? (ha/yo'q)")
#     if savol != 'ha':
#         break
# print('Dastur tugadi!')

import random

secret_number = random.randint(1, 100)
guess = 0
guesses = []
while guess != secret_number:
    guess = int(input("Угадайте число от 1 до 100: "))
    if guess < secret_number:
        print("Загаданное число больше.")
    elif guess > secret_number:
        print("Загаданное число меньше.")
    guesses.append(guess)
print(f"Вы угадали за {len(guesses)} попыток")


# Дано целое число, не меньшее 2. Выведите его наименьший натуральный делитель, отличный от 1.
# n = int(input())
# i = 2
# while n % i != 0:
#     i += 1
# print(i)

# По данному натуральному числу N найдите наибольшую целую степень двойки, не превосходящую N. 
# Выведите показатель степени и саму степень.
n = int(input())
two_in_power = 2
power = 1
while two_in_power <= n:
    two_in_power *= 2
    power += 1
print(power - 1, two_in_power // 2)