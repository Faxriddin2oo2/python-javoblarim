# Bismillah
"""
Created on Thu Aug  1 11:26:47 2024

@author: Faxriddin
"""

class Person:
    def __init__(self, ism, familiya, yosh, email, t_kun):
        self.ism = ism
        self.familiya = familiya
        self.yosh = yosh
        self.email = email
        self.t_kun = t_kun  
    
    def get_info(self):
        return {
            "First Name": self.ism,
            "Last Name": self.familiya,
            "yosh": self.yosh,
            "Email": self.email,
            "Birth Day": self.t_kun
        }
    
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
        # descriptions = 
        filename = 'hayot_yoli.txt' 
        with open(filename) as file:
            for line in file:
                if line.startswith(f'#{life_path_number} -'):
                    return line
        return filename.get(life_path_number, "Unknown life path number")
    
odam = Person('faxriddin', 'teshaboyev', 21, 'teshaboydinweq1@gmail.com', (4 , 9, 2002))
