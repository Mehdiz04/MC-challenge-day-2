
def romanToInt(s):
    romanSYM = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    s = s.replace('IV','IIII').replace('IX','VIIII').replace('XL','XXXX').replace('XC','LXXXX').replace('CD','CCCC').replace('CM','DCCCC')
    integer = 0
    for i in range(len(s)):
        integer += romanSYM[s[i]]
    return str(integer)

def intToRoman(num):
    SymValues = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',900: 'CM', 1000: 'M'}
    numbers = sorted(SymValues.keys() , reverse = True)
    roman = ''
    for n in numbers:
        while n <= num:
            roman += SymValues.get(n)
            num -= n
    return roman

text = '1100 V/III/MCMLXXXV'

print(intToRoman(int(text.split()[0])), '/'.join(map(romanToInt , text.split()[1].split('/'))))