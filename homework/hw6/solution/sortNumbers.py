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
    if (a > b and a > c):
        large = a
        if (b > c):
            middle = b
            small = c
        else:
            middle = c
            small = b
    elif (a > b and a < c):
        middle = a
        small = b
        large = c
    elif (a < b and a < c):
        small = a
        if (b > c):
            large = b
            middle = c
        else:
            large = c
            middle = b
    # -----------------------------
    return small, middle, large