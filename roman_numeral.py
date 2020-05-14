# Write a function that takes in a Roman numeral as an argument and returns the value as a numeric integer. 

# Roman numerals are written by using letters in place of integers.
# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

# For example:
# "MCMXC" = 1990
# "MDCLXVI" = 1666

roman_dic = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)

def decode_roman_numeral(roman):
    value = 0
    for i,letter in enumerate(roman):
        if i+1 < len(roman) and roman_dic[letter] < roman_dic[roman[i+1]]:
            value-=roman_dic[letter]
        else:
            value+=roman_dic[letter]
    return value
    
# TEST CASES
print(decode_roman_numeral("MMMCMXCIX")) # 1990
print(decode_roman_numeral("MDCLXVI")) # 1666

