from nltk.stem.snowball import RussianStemmer
from pymystem3 import Mystem
text = {'повернулась': 16886,
'повернулось': 23512,
'повернутый': 19619,
'повернуть': 3060,
'поверх': 12171,
'поверхности': 8734,
'поверхность': 20169,
'поверь': 2895,
'поверье': 31798,
'поверьте': 16164,
'поверью': 16131,
'поверю': 6320,
'повеселиться': 29517,
'повесил': 18273,
'повесилась': 28387,
'повесился': 21063,
'повесить': 11401,
'повеситься': 19918}

words = [key for key in text]
print(words)
stmmr = RussianStemmer()
new_words = [stmmr.stem(word) for word in words]
print(new_words)
m = Mystem()
lem_words = [''.join(m.lemmatize(word)).replace('\n', '') for word in words]
print(lem_words)