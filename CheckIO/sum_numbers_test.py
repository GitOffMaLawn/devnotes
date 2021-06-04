#!/bin/env python

import string
import csv
import sys

def sum_numbers(text: str) -> int:
    # your code here
    # no_spacetxt = csv.reader(text, delimiter=' ')
    no_spacetxt = text.split()
    try:
        for i in no_spacetxt:
            print(i+' not matched')
            if type(int(i)) == type(int()):
                print(i + ' ++ matched ++')
    except Exception:
        pass
        
    
            
            


if __name__ == '__main__':
    sum_numbers('hi')
    sum_numbers('who is 1st here')
    sum_numbers('my numbers is 2')
    sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year')
    sum_numbers('5 plus 6 is')
    sum_numbers('')

