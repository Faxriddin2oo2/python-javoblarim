# def minimal_districts(votes):
#   """
#   Вычисляет минимальное количество районов, которые должен посетить Борис.

#   Args:
#     votes: Список кортежей (a, b), где a - голоса за Андрея, b - голоса за Бориса.

#   Returns:
#     Минимальное количество районов.
#   """

#   # Сортируем районы по разнице голосов в пользу Бориса
#   votes.sort(key=lambda x: x[1] - x[0], reverse=True)

#   total_a, total_b = 0, 0
#   for i, (a, b) in enumerate(votes):
#     total_a += a
#     total_b += b
#     if total_b > total_a:
#       return i + 1

#   return -1  # Если Борис не может победить

# # Считываем входные данные
# n = int(input())
# votes = []
# for _ in range(n):
#   a, b = map(int, input().split())
#   votes.append((a, b))

# # Вычисляем и выводим результат
# result = minimal_districts(votes)
# print(result)

# def minimal_gorods(city_data):
#     city_data.sort(key=lambda x: x[1] - x[0], reverse=True)

#     candidate_one_total, candidate_two_total = 0, 0
#     for index, (city_one_votes, city_two_votes) in enumerate(city_data):
#         candidate_one_total += city_one_votes
#         candidate_two_total += city_two_votes
#         if candidate_two_total > candidate_one_total:
#             return index + 1

#     return -1

# num_cities = int(input())
# city_votes = []
# for _ in range(num_cities):
#     votes_city_one, votes_city_two = map(int, input().split())
#     city_votes.append((votes_city_one, votes_city_two))

# result = minimal_gorods(city_votes)
# print(result)

def min_subsidies(debts):
    total_subsidies = 0
    visited = set()

    def dfs(person, visited, debts, depth=0, max_depth=1000):
        if depth > max_depth:
            raise RecursionError("Слишком глубокая рекурсия")
        if person in visited:
            return
        visited.add(person)
        debt = debts[person]
        if debt < 0:
            raise ValueError("Отрицательный долг")
        debts[person] = 0
        if debt > 0:
            total_subsidies += debt
            dfs(debts[person], visited, debts, depth+1)

    for person in debts:
        if person not in visited:
            dfs(person, visited, debts)
    return total_subsidies

# Считываем входные данные
n = int(input())
debts = {}
for _ in range(n):
    a, b = map(int, input().split())
    if b < 0:
        print("Отрицательный долг")
        exit()  # Выходим из программы при обнаружении отрицательного долга
    debts[a] = b

# Вычисляем и выводим результат
try:
    result = min_subsidies(debts)
    print(result)
except RecursionError:
    print("Слишком глубокая рекурсия")
except ValueError:
    print("Обнаружен отрицательный долг")



# def minimal_gorods(votes):
#     votes.sort(key=lambda x: x[1] - x[0], reverse=True)  # Сортировка по потенциальному приросту голосов
#     boris_votes, andrew_votes = 0, 0
#     cities_to_visit = 0
    
#     for city_votes in votes:
#         boris_votes += city_votes[1]
#         andrew_votes += city_votes[0]
#         cities_to_visit += 1
#         if boris_votes > andrew_votes:
#             return cities_to_visit

#     return -1  

# n = int(input())
# votes = []
# for _ in range(n):
#     a, b = map(int, input().split())
#     votes.append((a, b))

# result = minimal_gorods(votes)
# print(result)


