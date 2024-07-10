# Bismillah
"""
Created on Wed Jul 10 21:58:12 2024

@author: Faxriddin
"""

class User:
    def __init__ (self,ism,login, email,password):
        self.ism = ism
        self.login = login
        self.email = email
        self.password = password
        
    def get_ism(self):
        return self.ism
    
    def get_login(self):
        return self.login
    
    def get_email(self):
        return self.email

    def get_password(self):
        return self.password
        
    def get_info(self):
        return f"{self.ism} ning saytga kirish logini - {self.login} va paroli - {self.login}, bu foydalanuvchining emaili - {self.email}"

user1 = User("Faxriddin", "Faxriddin1", "teshaboyev@gmail", 23342420)