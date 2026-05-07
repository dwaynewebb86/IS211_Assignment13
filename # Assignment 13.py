# Assignment 13

# Part 1

def fibonnaci(n):
    # base
    if n == 1 or n == 2:
        return 1
    
    # recursive
    return fibonnaci(n - 1) + fibonnaci(n - 2)

# Part 2

def gcd(a, b):
    # base
    if b == 0:
        return a
    
    # recursive
    return gcd(b, a % b)

# Part 3
def compareTo(s1, s2):
    # Base case: both strings empty
    if s1 == "" and s2 == "":
        return 0
    
    # If one string is empty
    if s1 == "":
        return -1
    if s2 == "":
        return 1
    
    # Compare first characters
    if s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    
    # Recursive case: move to next characters
    return compareTo(s1[1:], s2[1:])