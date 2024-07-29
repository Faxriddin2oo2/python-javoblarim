# Bismillah
"""
Created on Mon Jul 29 23:10:32 2024

@author: Faxriddin
"""

# На вход функция more_than_five(lst) получает список из целых чисел. Результатом работы функции должен стать новый список, 
# в котором содержатся только те числа, которые больше 5 по модулю.
# def more_than_five(lst):
#     new_lst = []
#     for number in lst:
#         if abs(number) > 5:
#             new_lst.append(number)
            
#         return new_lst

# print(more_than_five([7, -6, 9, 21, -25, 11, -5, 13]))
# print(more_than_five([1, -4, 87, -7, 54, -9, -12]))
# print(more_than_five([-1, -9, -42, 22, 54, 2, 6, 8, 9]))




# letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
# for letter in letters:
#     if letter == letter.upper():
#         letters.replace(letter, '')
# print(letters)

# letters = 'ЫгВЫоЯСремДШНККАыкЩЙФа'
# clean_string = ''
# for letter in letters:
#     if not letter.isupper():
#         clean_string += letter
# letters = clean_string
# print(letters)


# В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения. 
# По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
# x = int(input())
# y = int(input())
# i = 1
# while x < y:
#     x *= 1.1
#     i += 1
# print(i)

def find_day(x, y):
    # Инициализируем переменные
    current_distance = x
    day = 1
    
    # Пока текущий пробег меньше требуемого
    while current_distance < y:
        # Увеличиваем пробег на 10%
        current_distance *= 1.10
        # Переходим к следующему дню
        day += 1
    
    return day

# Пример использования
x = float(input("Введите пробег в первый день (в километрах): "))
y = float(input("Введите целевой пробег (в километрах): "))

day = find_day(x, y)
print(f"На {day}-й день пробег составит не менее {y} километров.")



























