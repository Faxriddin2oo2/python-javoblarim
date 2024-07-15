# Bismillah
"""
Created on Sun Jul 14 16:27:40 2024

@author: Faxriddin
"""

# From lesson
class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
    
    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.rang} {self.make} {self.model}"
    
    # def __eq__(self,boshqa_avto):
    #     """Tenglik"""
    #     return self.narh == boshqa_avto.narh

    # def __lt__(self,boshqa_avto):
    #     """Kichik"""
    #     return self.narh<boshqa_avto.narh
    
    # def __le__(self,boshqa_avto):
    #     """Kichik yoki teng"""
    #     return self.narh<=boshqa_avto.narh
    def __eq__(self, boshqa_avto):
        """Tenglik"""
        return self.narh == boshqa_avto.narh
    
    def __lt__(self,boshqa_avto):
        """Kichik"""
        return self.narh < boshqa_avto.narh
    
    def __le__(self,boshqa_avto):
        """Kichik yoki teng"""
        return self.narh <= boshqa_avto.narh
    
    def __gt__(self, boshqa_avto):
        """Katta"""
        return self.narh> boshqa_avto.narh
    
    def __ge__(self,boshqa_avto):
        """Katta yoki teng"""
        return self.narh >= boshqa_avto.narh
        
    
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Honda","Accord","Oq",2017,40000)

class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __len__(self):
        return len(self.avtolar)
    
    def __getitem__(self, index):
        return self.avtolar[index]
    
    def __setitem__(self,index,value):
        if isinstance(value, Avto):
            self.avtolar[index] = value
            
    def __add__(self,qiymat):
        if isinstance(qiymat,AvtoSalon):
            yangi_salon =  AvtoSalon(f"{self.name} {qiymat.name}")
            yangi_salon.avtolar = self.avtolar + qiymat.avtolar
            return yangi_salon
        
    def __call__(self,*param):
        if param: # agar parametr bo'lsa
            for avto in param:
                self.add_avto(avto)
        else: # agar parametr bo'lmasa
            return [avto for avto in self.avtolar]
    
    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto obyektini kiriting")

# salon1 = AvtoSalon("MaxAvto")
# salon2 = AvtoSalon("Avto Lider")
# avto1 = Avto("GM","Malibu","Qora",2020,40000)
# avto2 = Avto("GM","Lacetti","Oq",2020,20000)
# avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
# avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
# avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
# avto6 = Avto("Honda","Accord","Oq",2017,42000)
# salon1.add_avto(avto1, avto2, avto3)
# salon2.add_avto(avto4, avto5, avto6)



# PRACTICE
# Avvalga darslarda yaratilgan obyektlarga (Shaxs, Talaba) turli dunder metodlarni qo'shishni mashq qiling. 
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
        
    def __repr__(self):
        return f"{self.ism.title()} {self.familiya.title()}"
        
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
    def __init__(self, ism, familiya, passport, tyil,jins,bosqich):
        """Talabaning xususiyatlari"""
        super().__init__(ism, familiya, passport, tyil,jins)
        self.bosqich = 1
        # self.manzil = manzil
        self.bosqich = bosqich
        self.fanlar = []
        Talaba.talabalar_soni += 1 
    
    def __repr__(self):
        return f"Student {self.ism.title()} {self.familiya.title()}"
    
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
    
    def __lt__(self, boshqa_talaba):
        """Kichikligi5"""
        return self.bosqich < boshqa_talaba.bosqich
        
# talaba = Talaba("valijon","aliyev","FA112299",2000,"0000012",3)
# talaba2 = Talaba('ali', 'valiyev', 'AS2223112', 2002, 'erkak', 1)

# Fan degan yangi klass yarating. Fan obyetklari tarkibida shu fanga yozilgan talabalarning ro'yxati saqlansin. 
# Buning uchun Fanga add_student(), __getitem__, __setitem__, __len__ kabi metodlarni qo'shing.
class Fan:
    """Fan klassi"""
    def __init__(self, matematika, kimyo, fizika, biologiya, tarix):
        self.matematika = matematika
        self.kimyo = kimyo
        self.fizika = fizika
        self.biologiya = biologiya
        self.tarix = tarix
        self.studentlar = []
    
    # def __setitem__(self,index,value):
    #     if isinstance(value, Avto):
    #         self.avtolar[index] = value
            
    # def __add__(self,qiymat):
    #     if isinstance(qiymat,AvtoSalon):
    #         yangi_salon =  AvtoSalon(f"{self.name} {qiymat.name}")
    #         yangi_salon.avtolar = self.avtolar + qiymat.avtolar
    #         return yangi_salon
        
    # def __call__(self,*param):
    #     if param: # agar parametr bo'lsa
    #         for avto in param:
    #             self.add_avto(avto)
    #     else: # agar parametr bo'lmasa
    #         return [avto for avto in self.avtolar]
    
    # def add_avto(self, *qiymat):
    #     for avto in qiymat:
    #         if isinstance(avto, Avto):
    #             self.avtolar.append(avto)
    #         else:
    #             print("Avto obyektini kiriting")        
    def __repr__(self):
        return f"Bizda {self.matematika}, {self.kimyo}, {self.fizika}, {self.biologiya} va {self.tarix} fanlar bor"
    
    def __len__(self):
        return len(self.studentlar)
    
    def __getitem__(self, index):
        return self.studentlar[index]
    
    def __setitem__(self,index, value):
        if isinstance(value, Fan):
            self.studentlar[index] = value
    
    

fan1 = Fan('matematika', 'kimyo', 'fizika', 'biologiya', 'tarix')
fan2 = Fan('matematika', 'kimyo', 'fizika', 'biologiya', 'tarix')





















