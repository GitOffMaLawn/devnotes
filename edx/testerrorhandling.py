#!/bin/env python3

def normalize(numbers):
    max_number = max(numbers)
    for i in range(len(numbers)):
        numbers[i] /= float(max_number)
    return numbers

try:
      normalize([0, 0, 0])
except ZeroDivisionError:
      print('Invalid maximum element')

print(fancy_divide([0, 2, 4], 0))
