"""
Approach 1: Leetcode's approach.
Hint! Loop through the string from the back as so s[::-1]

Time complexity: O(N), beats 100%
Space Complexity: O(1)

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

'''
Approach 2: Using the current index to calculate, My approach.
Let's take the roman value CLXIV who's value is 164

        CLXIV
        i
Steps:
1. Let's initialize i at index 0 of the string, total = 0 and n = len(s).
2. Let's check if the value at i is greater or lesser than the value on it's right. In this case it is greater than the right value, so add the value to total as so:
    total = 0 + 100
3. After adding the value, move i one step to the right and check if the value at that index is greater than the one on the right, which it is so we add it to total:
    total = 0 + 100 + 50
4. move i another index to the right. Check if the nxt value is greater, which it is so we add the value to 
total:
    total = 0 + 100 + 50 + 10
5. Move i to the to the next index. check if the next value is greater, which unfornatunately, it is not. So according to the Roman Numerals rules, we need to subtract both values so i + 1 - i to get the value of the two
as so:
    total = 0 + 100 + 50 + 10 + (5 - 1)
    total = 164
6. There we go, we have our answer! But we need some use case to ensure that no errors arise from our algorithm.
Use cases:
    i. i cannot be greater than n which is len(s)
    ii. when calculate the difference between two Roman numerals, we move the index by two positions as so
        Initially: CLXIV
                      i
                Diff: V - I = 4
                * But moving this index by two steps, it would lie out of bounds which will nullify the first use case!
    iii. if the value at i is greater than the next value, add the value of i to total and move i one step to the right
        Initially: CLXIV
                   i
                C is greater than L so move i one step to the right and add value of C to total.
        After: CLXIV
                i

Time complexity: O(N), beats 43%
Space Complexity: O(1)

'''

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