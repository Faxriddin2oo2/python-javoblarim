# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 18:28:53 2024

@author: asus
"""

from googletrans import Translator

tarjimon = Translator()

msg = 'Tarjima uchun so\'z kiriting (chiqib ketish uchun "q" deb yozing): '
while True:
    text = input(msg)
    if text == "q":
        break
    else:
        tarjima = tarjimon.translate(text, src="uz", dest="en")
        print(tarjima.text)