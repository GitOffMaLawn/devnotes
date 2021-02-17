#!/bin/env python3


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

# def how_many(aDict):
#     '''
#     aDict: A animals, where all the values are lists.

#     returns: int, how many values are in the animals.
#     '''
#     # Your Code Here
#     result = 0
#     for i in aDict:
#         result = len(aDict[i]) + result
#     return result

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    tmp_dictionary = aDict
    best = len(max(aDict.values()))
    for i in tmp_dictionary:
        if len(aDict[i]) == best:
            return i

print(biggest(animals))
