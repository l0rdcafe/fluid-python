from unicodedata import normalize, name

for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'El Niño'.encode(codec), sep='\t')

city = 'São Paulo'
print(city.encode('utf_8'))
print(city.encode('utf_16'))
print(city.encode('iso8859_1'))

ohm = '\u2126'
print(name(ohm)) # OHM SIGN

ohm_c = normalize('NFC', ohm)
print(name(ohm_c)) # GREEK CAPITAL LETTER OMEGA
print(ohm == ohm_c) # False
print(normalize('NFC', ohm) == normalize('NFC', ohm_c)) # False

micro = 'μ'
print(name(micro)) # MICRO SIGN

micro_cf = micro.casefold()
print(name(micro_cf)) # GREEK SMALL LETTER MU

print(micro, micro_cf)

eszett = 'ß'
print(name(eszett)) # LATIN SMALL LETTER SHARP S

eszett_cf = eszett.casefold()
print(eszett, eszett_cf)
