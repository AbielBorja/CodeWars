def solution(number):
    romanSybols = {"M": 1000, "CM": 900,
                   "D": 500, "CD": 400, "C": 100,
                   "XC": 90, "L": 50, "XL": 40, "X": 10,
                   "IX": 9, "V": 5, "IV": 4, "I": 1}

    romanDecode = ""
    for key in romanSybols:
        value = romanSybols[key]
        
        while(number // value >= 1):
            number -= value
            romanDecode += key
    return romanDecode


# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000