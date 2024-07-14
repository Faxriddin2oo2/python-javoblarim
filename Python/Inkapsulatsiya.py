# Bismillah
"""
Created on Sun Jul 14 15:14:10 2024

@author: Faxriddin
"""

# From lesson
from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    def __init__(self,make,model,rang, yil, narh, km=0):
        """Avtomobilning  xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1 #Klassning nechi marta ishlatilganini bilish uchun sonning o'zi 12 qatorda
        
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    def add_km(self,km):
        """Mashinaning km ga yana km qo'shish"""
        if km>=0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi")
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# print(Avto.get_num_avto())



# PRACTICE
# Avvalgi darslarimizda yaratgan Shaxs va Talaba klasslariga yopiq xususiyatlar qo'shing va ularning qiymatini ko'rsatuvchi 
# va o'zgartiruvchi metodlar yozing.
class Shaxs:
    """Shaxslar haqida ma'lumot"""
    __odamlar_soni = 0
    def __init__(self,ism, familiya, passport, tyil, jins):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        self.__jins = jins
        Shaxs.__odamlar_soni += 1
        
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f"Passport: {self.passport}, {self.tyil} - yilda tug'ilgan"
        return info
    
    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
    
    def get_jins(self):
        return f"{self.__jins.title()}"
    
    @classmethod
    def get_num_people(cls):
        return cls.__odamlar_soni
    
inson = Shaxs("Hasan","Alimov","FB001122",1995,'erkak')

class Talaba(Shaxs):
    """Talaba klassi"""
    talabalar_soni = 0
    def __init__(self, ism, familiya, passport, tyil,jins,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil,jins)
        self.idraqam = idraqam
        self.bosqich = 1
        # self.manzil = manzil
        self.fanlar = []
        Talaba.talabalar_soni += 1 
        
    def get_id(self):
        """Talabaning ID raqami"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f"{self.get_bosqich()} - bosqich. ID raqami: {self.idraqam}"
        return info  
    
    def fanga_yozil(self,fan):
        self.fanlar.append({fan})
    
    def get_num_students(self):
        return self.talabalar_soni
        
talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",2232223)






























