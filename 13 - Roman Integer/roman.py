"""
def roman(s):
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,    
    }
    total = 0
    prev = 0
    for i in s[::-1]:
        if romans[i] >= prev:
            total += romans[i]
        else:
            total -= romans[i]
        prev = romans[i]
    return total
print(roman("XIV"))
"""
def is_roman(s):
    romans = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,    
    }
        
    total = 0
    n = len(s)
    i = 0        
    
    while i < n:
        if i < n - 1 and romans[s[i]] < romans[s[i + 1]]:
            total += romans[s[i + 1]] - romans[s[i]]
            i += 2

        else:
            total += romans[s[i]]
            i += 1

    return total

print(is_roman("CLXIV"))