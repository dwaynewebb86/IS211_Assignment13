# Assignment 13

def fibonnaci(n):
    # Base case
    if n == 1 or n == 2:
        return 1
    
    # Recursive case
    return fibonnaci(n - 1) + fibonnaci(n - 2)