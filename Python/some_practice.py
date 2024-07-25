# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 22:58:26 2024

@author: asus
"""

# calculator
print("Sodda kalkulyatorga xush kelibsiz")

while True:	
	birinchi_son = int(input("Birinchi sonni kiriting \n>>>"))
	amal = input("Amalni tanlang : (+, -, *, /) ")
	ikkinchi_son = int(input("Ikkinchi sonni kiriting \n>>>"))
	if amal == "+":
		print(f"Bu sonlarning yig'indisi = {birinchi_son + ikkinchi_son}")
	elif amal == "-" :
		print(f"Bu sonlarning ayirmasi = {birinchi_son - ikkinchi_son}")
	elif amal == "*" :
		print(f"Bu sonlarning ko'paytmasi = {birinchi_son*ikkinchi_son}")
	elif amal == "/" :
		print(f"Birinchi sonni ikkinchisiga bo'linmasi = {birinchi_son/ikkinchi_son}")
	else:
		print("Iltimos berilgan amallardan birini tanlang!")

	
	savol = input("Yana amal bajarishni xoxlaysizmi? ha(1)/ yo'q(0)")
	if savol == '0':
		break
    
    
    
# class Talaba:
# 	def __init__(self, ism, familiya, yosh, kurs, universitet, tjoy):
# 		self.ism = ism
# 		self.familiya = familiya
# 		self.yosh = yosh
# 		self.kurs = kurs
# 		self.universitet = universitet
# 		self.tjoy = tjoy
# 		self.__jins = jins
# 	
# 	def get_yosh(self):
# 		return f"Sizning ayni damdagi yoshinhgiz {self.yosh}"

# 	def get_kurs(self):
# 		return f"Siz {self.kurs} da o'qiysiz"

# 	def get_university(self):
# 		return f"Siz {self.universitet} ning {self.kurs}da o'qiysiz" 

# 	def get_info(self):
# 		return f"{self.ism.title()} {self.familiya.title()} {self.tjoy.title()} da tug'ilgan."
# 			f"Yoshi {self.yosh} da va {self.universitet}da {self.kurs}da o'qiydi"
		

        
	