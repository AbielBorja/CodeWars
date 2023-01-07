def consonant_count(s):
    count = 0
    notConstant = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    for constant in s:
        if constant in notConstant:
            continue
        elif constant.isnumeric():
            continue
        elif constant.isspace():
            continue
        elif constant.isalpha() == False:
            continue
        else:
            count += 1
    return count

print(consonant_count('aaaaa'))
print("-------------")
print(consonant_count('XaeiouX'))
print("-------------")
print(consonant_count('Bbbbb'))
print("-------------")
print(consonant_count('helLo world'))
print("-------------")
print(consonant_count('h^$&^#$&^elLo world'))
print("-------------")
print(consonant_count('0123456789'))
print("-------------")
print(consonant_count('012345_Cb'))

