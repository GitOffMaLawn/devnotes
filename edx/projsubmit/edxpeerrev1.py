# -*- coding: utf-8 -*-
"""
Spyder Editor

This is an eDX project. The purpose of this file is to
write a function that will output the SUM of a polygon.
Also to proctice documentation inside of a Python script.
"""

from math import tan, pi

def polysum(number_sides, side_length):
    """
    Function
    --------
    'polysum' function will return the SUM of the area
    + perimiter ^ 2 for a polygon.

    Parameters
    ----------
    n : INT
        Number of sides fol polygon.
    s : INT
        Side size.

    Returns
    -------
    FLOAT
        SUM for area + perimiter ^ 2 for a polygon limited to
        4 decimal.

    """
    area = number_sides * (side_length ** 2) / (4 * tan(pi / number_sides))
    perimiter = number_sides * side_length
    sum_ap = area + perimiter ** 2
    return round(sum_ap,4)

# Sample Output to test 'polysum' function.
print(polysum(4, 20), "\n6800.0 -- correct")
print(polysum(21, 88), "\n3684838.9356 -- correct")
print(polysum(74, 28), "\n4634619.4522 -- correct")
print(polysum(12, 83), "\n1069146.294 -- correct")
print(polysum(12, 5), "\n3879.9038 -- correct")
print(polysum(42, 67), "\n8547562.1918 -- correct")
