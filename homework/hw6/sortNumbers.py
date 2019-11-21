'''
Implement the function sort_numbers which takes in 3 numbers and returns them in ascending order

Parameter:
    a - first number (either int or float)
    b - second number (either int or float)
    c - third number (either int or float)

Return:
    small, middle, large - numbers sorted from smallest to largest

Example output:
    sort_numbers(10,5,2)
    > 2, 5, 10

    sort_numbers(1.5, 0.2, 4)
    > 0.2, 1.5, 4

    sort_numbers(-1, -4, -10)
    > -10, -4, -1

Hint:
    Use nested conditionals or logical operators.
    Think through all possible scenarios

    When is a largest? middle? small?
    - e.g.
        if (a > b and a > c):
            large = a
        elif (a > b and a < c):
            middle = a
      OR
        if (a > b):
            if (a > c):
                large = a
            else:
                middle = a
        
'''
def sort_numbers(a, b, c):
    small, middle, large = None, None, None
    # ---- your code goes here ---- 
    if (a > b):
        if (b > c): # a > b > c
            large = a
            middle = b
            small = c
        else:
            small = b
            if (a > c): # a > c > b
                large = a
                middle = c
            else: # c > a > b
                large = c
                middle = a
    else:
        if (a > c): # b > a > c
            large = b
            middle = a
            small = c
        else:
            small = a
            if (b > c): # b > c > a
                large = b
                middle = c
            else: # c > b > a
                large = c
                middle = b
    # -----------------------------
    return small, middle, large

print(sort_numbers(1,2,3))