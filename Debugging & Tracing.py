"""
Part A:
Replace this comment with your answer to Part A
This program after run show number 10 because not written return at the end of def
"""

"""
Part B: 
Edit this code so that it works correctly
"""

def divide_and_round(n):
    """
    Divides an integer n by 2 and rounds 
    up to the nearest whole number
    """
    if n % 2 == 0:
        n = n / 2
    else:
        n = (n + 1) / 2
    return n #return is the main part of calling this function
def main():
    n = 10
    divide_and_round(n)
    print(n) 
