#!/usr/bin/env python3

"""
Write a procedure called oddTuples, which takes a tuple as input, and returns a new tuple as output, 
where every other element of the input tuple is copied, starting with the first one. So if test 
is the tuple ('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').

"""


# def applyToEach(L, f):
#     for i in range(len(L)):
#         L[i] = f(L[i])

# def timesFive(a):
#     return a * 5

# def plusOne(a):
#     return a + 1

# def timesTwoAbs(a):
#     return abs(a) * abs(a)

# testList = [1, -4, 8, -9]

# applyToEach(testList, timesTwoAbs)

# print(testList)

def applyEachTo(L, x):
    result = []
    for i in range(len(L)):
        result.append(L[i](x))
    return result

def square(a):
    return a*a

def halve(a):
    return a/2

def inc(a):
    return a+1

test = applyEachTo([inc, square, halve, abs], 3.0)
print(test)