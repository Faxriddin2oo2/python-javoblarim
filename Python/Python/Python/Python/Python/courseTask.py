# Bismillah
"""
Created on Wed Oct 16 18:53:57 2024

@author: Faxriddin
"""

class Person:
    def __init__(self, t_kun):
        self.ism = input('Ism: ')
        self.familiya = input("Familiya: ")
        self.yosh = int(input("Yoshingiz: "))
        self.email = input("Emailing: ")
        self.t_kun = t_kun
        
    def get_info(self):
        info = f'{self.familiya.title()} {self.ism.title()}, {self.t_kun} da tugilgan va hozir yoshi {self.yosh}da va uning emaili: {self.email}.'
        return info
    def get_life_path_number(self):
        day, month, year = self.t_kun
    
        def sum_digits(n):
            return sum(int(digit) for digit in str(n))
        
        day_sum = sum_digits(day)
        
        month_sum = sum_digits(month)
        
        year_sum = sum_digits(year)
        
        total_sum = day_sum + month_sum + year_sum
        
        while total_sum > 9:
            total_sum = sum_digits(total_sum)
        return total_sum
        
    def get_life_path_description(self):
        life_path_number = self.get_life_path_number()
        with open('hayot_yoli.txt', 'r') as file:
            for line in file:
                line = line.strip()  
                if line.startswith("#"):  
                    try:
                        number, info = line[1:].split(" - ", 1)
                        if int(number) == life_path_number:
                            return info.strip()  
                    except ValueError:
                        continue  
        return "Life path description not found."




example1 = Person((4, 9, 2002))
print(example1.get_info())
print(example1.get_life_path_description())
# example2 = Person(, familiya, yosh, email, t_kun)