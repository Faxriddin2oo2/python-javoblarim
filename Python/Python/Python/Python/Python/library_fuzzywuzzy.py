# Bismillah
"""
Created on Tue Jul 30 19:29:19 2024

@author: asus
"""

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from uzwords import words

# Ikki so'z o'rtasida o'xshashlik foizini topish
print(fuzz.ratio("salom", 'assalom'))
print(fuzz.ratio("salom", 'salim'))

# Matnlar orasida 3 ta eng o'xshashlarini ajratib olish
text = 'салом'
matches = process.extract(text, words, limit = 3)
print(matches)

# Matnlar orasidan eng o'xshashini topish
text = "талба"
match = process.extractOne(text, words)
print(match)