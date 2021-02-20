
# edX Unit2 Notes

## String / List manipulation CS

`s = 'y' + s[1:]` -> `s` is now `y`+ whatever was in `s[1:]` `s` appended to end. Added `y` to the beginning of string.

`L3 = L1 + L2` -> Concatenates.

`del(L1[1])` -> Delete specific index.

`L.remove(2)` -> Removes first `int 2`.

`L.pop()` -> Returns last index then removes last index.

`L.pop(3)` -> Returns 3rd from last and removes 3rd from last.

`list(s)` -> Makes `s` in to a list.

`s.split('<')` -> Split at `<`.

`''.join(L1)` -> Returns string from list no separator.

`'_'.join(L1)` -> Returns string from list `'_'` separator.

`sort(L1)` -> Return sorted list. List does not change.

`L1.sort()` -> Changes `L1` to a sorted list.

`sorted(L1)` -> Return sorted list. List does not change.

`L1 = sorted(L1)` -> Modify `L1` to be sorted.

`L1.reverse()` -> Changes `L1` to reverse order list.

`range(5)` -> Return `[1, 2, 3, 4]` similar to tuple.

`range(2, 6)` -> Return `[2,3,4,5]`.

`range(5,2,-1)` -> Return list in reverse order `[5,4,3]`.

## Example of manipulation that may fail on occasion

Careful to use this method. As the idex items are being processed by `.remove()`, the index inside of the list changes. Since iteration is a linear process, some items may be skipped.

```python

def remove_dups(L1, L2):
    for e in L1:
        if e in L2:
            Li.remove(e)

```

## A better example on manipulating lists

Make a copy of the list

Runs through `L1` and `L2` and applies function.

```python

def remove_dups(L1, L2):
    L1_copy = L1[:]
    for e in L1:
        if e in L2:
        L1.remove(e)

for elm in map(remove_dups, L1, L2)
    print(elm)

```

## Using Dictionaries

Use `{}` to initiate a dictionary `.keys()` to return the key for each index item `.values()` to return the values for each index item.

### Lyrics Example

Create a dict with word and how many times it appears.

```python

def lyrics_to_frequencyies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
    return myDict

```

With the dictionary method return which common words show up the most times.

```python

def most_common_words(freqs):
    values = freqs.values()
    # using 'max()' function instead of iteration to determine the
    # largest number
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)

```

Words that repeat the most.

```python

def words_ofter(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del(freqs[w])
            else:
                done = True
        return result

print(words_often(beatles, 5))

```

## FE U3:6.2,6.3, Exercise: `how many`

```python

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result = 0
    for i in aDict:
        result = len(aDict[i]) + result
    return result

print(how_many(animals))

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

```

## Example of efficently using dictionary to calculate complicated problem

Fibonacci with a Dictionary

```python

def fib_efficient (n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient (n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

d = {1:1, 2:2}
print(fib_efficient(6, d))

```

* do a `lookup first` in case already calculated the value
* `modify dictionary` as progress through function calls

## Global variables

Can be dangerous to use but may be needed in specific cases. Globals can be created with the `global varName` call. Also variables created at the top level are global and a common proctice is to make globals ALL CAPS.

# Problem Set 3

## Requirements

Here are the requirements for your game:

1. The computer must select a word at random from the list of available words that was provided in words.txt. The functions for loading the word list and selecting a random word have already been provided for you in ps3_hangman.py.

2. The game must be interactive; the flow of the game should go as follows:

    * At the start of the game, let the user know how many letters the computer's word contains.
    * Ask the user to supply one guess (i.e. letter) per round.
    * The user should receive feedback immediately after each guess about whether their guess appears in the computer's word.
    * After each round, you should also display to the user the partially guessed word so far, as well as letters that the user has not yet guessed.

3. Some additional rules of the game:

    * A user is allowed 8 guesses. Make sure to remind the user of how many guesses s/he has left after each round. Assume that players will only ever submit one character at a time (A-Z).
    * A user loses a guess only when s/he guesses incorrectly.
    * If the user guesses the same letter twice, do not take away a guess - instead, print a message letting them know they've already guessed that letter and ask them to try again.
    * The game should end when the user constructs the full word or runs out of guesses. If the player runs out of guesses (s/he "loses"), reveal the word to the user when the game ends.

```text
-----OUTPUT OF WINNING GAME-----
Loading word list from file...
55900 words loaded.
Welcome to the game, Hangman!
I am thinking of a word that is 4 letters long.
-------------
You have 8 guesses left.
Available letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Good guess: _ a_ _
------------
You have 8 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Oops! You've already guessed that letter: _ a_ _
------------
You have 8 guesses left.
Available letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: s
Oops! That letter is not in my word: _ a_ _
------------
You have 7 guesses left.
Available letters: bcdefghijklmnopqrtuvwxyz
Please guess a letter: t
Good guess: ta_ t
------------
You have 7 guesses left.
Available letters: bcdefghijklmnopqruvwxyz
Please guess a letter: r
Oops! That letter is not in my word: ta_ t
------------
You have 6 guesses left.
Available letters: bcdefghijklmnopquvwxyz
Please guess a letter: m
Oops! That letter is not in my word: ta_ t
------------
You have 5 guesses left.
Available letters: bcdefghijklnopquvwxyz
Please guess a letter: c
Good guess: tact
------------
Congratulations, you won!


-----OUTPUT OF LOSING GAME-----
Loading word list from file...
55900 words loaded.
Welcome to the game Hangman!
I am thinking of a word that is 4 letters long.
-----------
You have 8 guesses left.
Available Letters: abcdefghijklmnopqrstuvwxyz
Please guess a letter: a
Oops! That letter is not in my word: _ _ _ _
-----------
You have 7 guesses left.
Available Letters: bcdefghijklmnopqrstuvwxyz
Please guess a letter: b
Oops! That letter is not in my word: _ _ _ _
-----------
You have 6 guesses left.
Available Letters: cdefghijklmnopqrstuvwxyz
Please guess a letter: c
Oops! That letter is not in my word: _ _ _ _
-----------
You have 5 guesses left.
Available Letters: defghijklmnopqrstuvwxyz
Please guess a letter: d
Oops! That letter is not in my word: _ _ _ _
-----------
You have 4 guesses left.
Available Letters: efghijklmnopqrstuvwxyz
Please guess a letter: e
Good guess: e_ _ e
-----------
You have 4 guesses left.
Available Letters: fghijklmnopqrstuvwxyz
Please guess a letter: f
Oops! That letter is not in my word: e_ _ e
-----------
You have 3 guesses left.
Available Letters: ghijklmnopqrstuvwxyz
Please guess a letter: g
Oops! That letter is not in my word: e_ _ e
-----------
You have 2 guesses left.
Available Letters: hijklmnopqrstuvwxyz
Please guess a letter: h
Oops! That letter is not in my word: e_ _ e
-----------
You have 1 guesses left.
Available Letters: ijklmnopqrstuvwxyz
Please guess a letter: i
Oops! That letter is not in my word: e_ _ e
-----------
Sorry, you ran out of guesses. The word was else.
```
