# Bismillah
"""
Created on Thu Jul 11 21:16:18 2024

@author: asus
"""

# Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) 
# qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)

class Avto:
    """Avtomobil haqida ma'lumot"""
    def __init__(self, model, rang, korobka, narh):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.probeg = 15_000
        
# Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
# get_info() metodi avti haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
    def get_info(self):
        return f"Avtomobilimizning markasi - {self.model.upper()} va rangi - {self.rang}, korobkasi {self.korobka}, \
oka bo'lish narhi {self.narh}, {self.probeg} probegi bor"

    
# Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
# update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin
    def update_km(self,km):
        self.probeg += km
    

            
car1 = Avto('bmw', "to'q yashil", "avtomat", 44000)

    


# Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring 
# (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
class Avtosalon:
    def __init__(self,nomi,manzili,avtomobillar, raqami):
        self.nomi = nomi 
        self.manzili = manzili
        self.avtomobillar = avtomobillar
        self.raqami = raqami
        self.avtolar = []
        self.avtolar_soni = 0
# Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
    def add_auto(self, auto):
        self.avtolar.append(auto)
        self.avtolar_soni += 1
    
    def get_info(self):
        return f"{self.nomi} salonimiz {self.manzili} da joylashgan bo'lib {self.avtomobillar} avtomobili sotuvda bor, murojat uchun raqam {self.raqami}"
    
    def get_car(self):
        return [auto.get_info() for auto in self.avtolar]
        
auto1 = Avtosalon('KIA', 'Sergeli', "Sorento", 98999755)
auto2 = Avtosalon("Lada", "Rohat", "Largus", 998555745)


# Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring
def see_methods(klass):
    return [method for method in dir(klass) if method.startswith('__') is False]

print(see_methods(Avtosalon))а



































