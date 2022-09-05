# Armstrong Numbers

"""
An Armstrong number is a number that is the sum of its own digits each raised to the 
power of the number of digits.

For example:
    153 is an Armstrong number, because:
        153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
    
    154 is not an Armstrong number, because:
        154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190

Write some code to determine whether a number is an Armstrong number.
"""

def is_armstrong_number(number):
    solution = 0
    for n in str(number):
        solution += int(n) ** len(str(number))
    if solution == number:
        return True;
    return False;
