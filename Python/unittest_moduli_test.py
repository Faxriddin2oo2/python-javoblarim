# Bismillah
"""
Created on Tue Jul 23 15:24:47 2024

@author: Faxriddin
"""

# From lesson
# FUNKSIYANI TEKSHIRISH
import unittest
from unittest_moduli import *

# class NameTest(unittest.TestCase):
#     def test_toliq_ism(self):
#         formatted_name = get_full_name('faxriddin', 'teshaboyev')
#         self.assertEqual(formatted_name, 'Faxriddin Teshaboyev')

# unittest.main()



# SONLARNI TEKSHIRISH
# class CircleTest(unittest.TestCase):
#     def test_area(self):
#         self.assertAlmostEqual(getArea(10),314.159)
#         self.assertAlmostEqual(getArea(3),28.27431)
#     def test_perimeter(self):
#         self.assertAlmostEqual(getPerimetr(10), 62.8318)
#         self.assertAlmostEqual(getPerimetr(4), 25.13272)
        
# unittest.main()



# MANTIQIY QIYMATLARNI TEKSHIRISH
# class tubSonTest(unittest.TestCase):
#     def test_true(self):
#         self.assertTrue(tubSonmi(7))
#         self.assertTrue(tubSonmi(193))
#         self.assertTrue(tubSonmi(547))
#     def test_false(self):
#         self.assertFalse(tubSonmi(6))
#         self.assertFalse(tubSonmi(265))
#         self.assertFalse(tubSonmi(489))
        
# unittest.main()



# PRACTICE
# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya
# class maxSonTest(unittest.TestCase):
#     def test_max(self):
#         self.assertEqual(maxSon(14, 11, 9),14)
#         self.assertEqual(maxSon(14, 19, 7),19)  
#         self.assertEqual(maxSon(4, 1, 9),9)
        
# unittest.main()



# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya
# class kattaXarfTest(unittest.TestCase):
#     def test_kattaXarf(self):
#         self.assertEqual(kattaXarf(), ['Olma', 'Nok', 'Taxta', 'Kocha', 'Noutbook', 'Issiq'])

# unittest.main()



# Berilgan sonlar ro'yxatidan juft sonlarni ajratib oluvchi funksiya
class juftSonTest(unittest.TestCase):
    def test_juftSon_true(self):
        self.assertTrue(juftSon(6))
    def test_juftSon_false(self):
        self.assertFalse(juftSon(5))

unittest.main()










