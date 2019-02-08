from difflib import SequenceMatcher as SM

s1 = 'PHILIPS'
s2 = '"%/&&/PHILIPS2$'
print(SM(None, s1, s2).ratio())

s1 = 'PHILIPS'
s2 = '"%/&&/PHILSZ<$'
print(SM(None, s1, s2).ratio())


