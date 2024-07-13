# Bismillah
"""
Created on Fri Jul 12 21:02:51 2024

@author: Faxriddin
"""

# From lesson

class Shaxs:
    """Shaxslar haqida ma'lumot"""
    def __init__(self,ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism} {self.familiya}."
        info += f"Passport: {self.passport}, {self.tyil} - yilda tug'ilgan"
        return info
    
    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil - self.tyil
        
inson = Shaxs("Hasan","Alimov","FB001122",1995)
# print(f"{inson.get_info()}. {inson.get_age(2021)} yoshda.")

# VORIS KLASS YARATISH
# class Talaba(Shaxs):
#     """Talaba klassi"""
#     def __init__(self, ism, familiya, passport, tyil,idraqam,manzil):
#         """Talabaning xususiyatlari"""
#         super().__init__(ism, familiya, passport, tyil)
#         self.idraqam = idraqam
#         self.bosqich = 1
#         self.manzil = manzil
        
#     def get_id(self):
#         """Talabaning ID raqami"""
#         return self.idraqam
    
#     def get_bosqich(self):
#         """Talabaning o'qish bosqichi"""
#         return self.bosqich
    
#     def get_info(self):
#         """Talaba haqida ma'lumot"""
#         info = f"{self.ism} {self.familiya}."
#         info += f"{self.get_bosqich()} - bosqich. ID raqami: {self.idraqam}"
#         return info

# talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012")
# print(f"{talaba.get_info()}. ID raqami:{talaba.get_id()}")
# print(f"{talaba.get_bosqich()}-bosqich talabasi")
# print(talaba.get_info())

    
# OBYEKT ICHIDA OBYEKT
# class Manzil:
#     """Manzil saqlash uchun klass"""
#     def __init__(self,uy,kocha,tuman,viloyat):
#         """Manzil xususiyatlari"""
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat
    
#     def get_manzil(self):
#         """Manzilni ko'rish"""
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy}-uy"
#         return manzil
# class Manzil:
#     """Manzil saqlash uchun klass"""
#     def __init__(self,uy,kocha,tuman,viloyat):
#         """Manzil xususiyatlari"""
#         self.uy = uy
#         self.kocha = kocha
#         self.tuman = tuman
#         self.viloyat = viloyat
        
#     def get_manzil(self):
#         """Manzil ko'rish"""
#         manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
#         manzil += f"{self.kocha} ko'chasi, {self.uy} - uy"
#         return manzil
    
# talaba_manzil = Manzil(12,'Olmazor',"Bog'bon","Samarqand")
# talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012",talaba_manzil)    
# print(talaba.manzil.get_manzil())
# print(talaba.manzil.tuman)


# PRACTICE
# Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida 
# bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])
class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil,idraqam):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        # self.manzil = manzil
        self.fanlar = []
        
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


# Fan degan yangi klass yarating va bu klassdan turli fanlar uchun alohida obyektlar yarating.
class Fan:
    def __init__(self,matematika,kimyo,fizika,biologiya,tarix):
        self.matematika = matematika
        self.kimyo = kimyo
        self.fizika = fizika
        self.biologiya = biologiya
        self.tarix = tarix
        
    def get_fan():
        return 'matematika'
# Talaba klassiga fanga_yozil() degan yangi metod yozing. Bu metod parametr sifatida 
# Fan klassiga tegishli obyektlarni qabul qilib olsin va talabaning fanlar ro'yxatiga qo'shib qo'ysin.

fan = "matematika" 
talaba = Talaba("Valijon","Aliyev","FA112299",2000,"0000012")    

    
# Yuqoridagi Shaxs klassidan boshqa turli voris klasslar yaratib ko'ring (masalan Professor, Foydalanuvchi, Sotuvchi, 
# Mijoz va hokazo)
class Professor(Shaxs):
    def __init__(self, ism, familiya, passport, tyil,tajriba):
        super().__init__(ism, familiya, passport, tyil)
        self.tajriba = tajriba
        
    def get_tajriba(self, yil):
        """Ish tajribasini aniqlovchi dastur"""
        return f"Professor {self.familiya.title()}ning tajribasi: {yil - 1995} yil"
    
    def get_info(self):
        """Professor haqida ma'lumot"""
        info = f"{self.ism.title()} {self.familiya.title()}."
        info += f"Passport: {self.passport}, {self.tyil} - yilda tug'ilgan va {self.tajriba} yil tajribaga ega professor"
        return info

professor1 = Professor('faxriddin', 'teshaboyev', 'AA223344', 1970, 30)
        
class Sotuvchi(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, hajmi):
        super().__init__(ism, familiya, passport, tyil)
        self.hajmi = hajmi
        self.soni = 0
        
    def get_hajm(self):
        """Sotuvchining sotgan molini hajmini qaytaruvchi metod"""
        return f"Sotuvchi {self.ism.title()} bu oy {self.hajmi} ta sotuv qildi"
    
    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info = f"{self.ism.title()} {self.familiya.title()}."
        info += f"Passport: {self.passport}, {self.tyil} - yilda tug'ilgan sotuvchi hodimimiz har oy eng kamida {self.hajmi} ta savdo qiladi"
        return info

sotuvchi = Sotuvchi("ali", "valiyev", 'ad2232232', 2002, 102)
    
    
    
    
    
    
    
    
    
    
    