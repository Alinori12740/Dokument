"""
Please complete the functions and classes. Start `pytest` to test your solutions.

------------------------------------------------------------------------
Tests are available for each exercise. Feel free to add to them.
See test_exercise.py.
You can run the tests right now by executing `pytest` on the console.
------------------------------------------------------------------------

If you feel stuck, reach out and ask.


We start with an example:

"""

import random
def exercise_1():
    """
    Exercise 1 : Write a function which returns a list with 5 dice rolls.
    To roll a 6 faced dice:
    >>> random.seed(1) # this is only for this test to predict the dice. Don't use seed.
    >>> random.randint(1,6)
    2
    >>> random.randint(1,6)
    5
    >>> random.randint(1,6)
    1
    """

    return [1, 2, 3, 4, 5]

def exercise_1_variant(anumber: int) -> list:
    """
    Exercise 1 variant: Write a function which returns a list with variable number
    of dice rolls.
    """

def exercise_2(alist): # since list is a keyword in python, you sould not use it as argument name
    """
    Exercise 2 : Write a function that returns the length of a given list
    """

def exercise_3_intro(alist):
    """
    Exercise 3 intro : To solve the the next exercise I'd like to introduce loops. Loops are
    good for inspecting and or modifying items in a list or a dict. In this example we loop
    over a list of numbers and incremente every item by 1.
    """
    new_list = []
    for item in alist: # item is a variable that contains the current item if alist.
        new_list.append(item+1)
    return new_list

def exercise_3_intro_variant(alist):
    """
    The last example is nice, but since such scenarios are so common, python has the concept
    of comprehensions. Same functionality, but much much more compact. We create the new_list
    'on the fly'.
    """
    return [item+1 for item in alist]

def exercise_3(list_of_number_pairs):
    """
    Write a python program that sums pairs.
    ((1, 2), (100, 20)) -> (3,120)
    """

def exercise_4_intro(alist_of_numbers):
    """
    For exercise_4 we need to make decisions. Let's introduce if/elif/else
    Scan list list of numbers an return a new list. Every number < 0 should become
    the string "negative", number == 0 should be "zero" and number > 0 should become "positive".
    """
    new_list = []
    for number in alist_of_numbers:
        if number < 0:
            new_list.append('negative')
        elif number > 0:
            new_list.append('positive')
        else:
            new_list.append('zero')
    return new_list

def exercise_4(alist_of_numbers):
    """
    Write a function to get the largest number from a list.
    """

def exercise_5(alist_of_numbers):
    """
    Write a function to get the smallest number from a list.
    """

def exercise_6(rand_start=1, rand_end=10, rand_count=10):
    """
    Write a function that generates rand_count random numbers. The numbers should be between
    rand_start and rand_end including both.
    """

def exercise_7(astring):
    """
    Write a function to count the number of characters (character frequency) in a string.
    Sample String : google.com'

    Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

    You want to use a dict to store they characters as key and the frequency as value.

    >>> a = {}
    >>> a['x'] = 1
    >>> a['x'] += 5
    >>> a
    {'x': 6}

    Remember lists and strings are sequences. You can use a for loop to loop over every
    character in a string.
    """

def exercise_8(alist_of_strings):
    """
    Write a function to count the number of strings in a list where the string length is 2 or more
    and the first and last character are same.

    Sample List : ['abc', 'xyz', 'aba', '1221']
    Expected Result : 2
    """

def exercise_9_intro(a_list_of_numbers):
    """
    Write a function that sorts a list of numbers. See https://docs.python.org/3/howto/sorting.html
    Sample List: [100, 30, 7, 4, 9]
    Expected Result: [4, 7, 9, 30, 100]
    """

def exercise_9(a_list_of_tuples):
    """
    HIGH DIFICULTY FOR BEGINNER. See: https://docs.python.org/3/howto/sorting.html.
    The solution is in fact simple, but:
    The sorted function sorts by default items in a list. In this example our items are tuples (like lists but not
    changable (immutable). And it is ask to sort the list by the second element of each tuple. Sorted has has the
    key argument. It takes a function that is supposed to return the item to be sorted...

    Write a function to get a list, sorted in increasing order by the last element in each tuple from a given list of
    non-empty tuples.
    Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
    """

def exercise_10_intro(stringa, stringb):
    """
    In the next exercise you will need string concatenation. It is easy:
    """
    return stringa + stringb

def exercise_10_intro2(astring, times):
    """
    It is even possible to use * to multiply (repeat) a string.
    """
    return astring * times

def exercise_10(astring):
    """
    10. Write a function to get a string made of the first 2 and the last 2 chars from a given a string. If the string
    length is less than 3, return instead the empty string.
    Sample String : 'w3resource'
    Expected Result : 'w3ce'
    Sample String : 'w3'
    Expected Result : 'w3w3'
    Sample String : ' w'
    Expected Result : Empty String
    """

def exercise_11(astring):
    """
    Write a function to get a string from a given string where all occurrences of its first char have been changed to
    '$', except the first char itself. Take a look at the documentation of string methods:
    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
    replace is probably what you need.

    Sample String : 'restart'
    Expected Result : 'resta$t'
    """

def exercise_12(stringa,stringb):
    """
    Write a function to get a single string from two given strings, separated by a space and swap the first two
    characters of each string.
    Sample String : 'abc', 'xyz'
    Expected Result : 'xyc abz'
    """

def exercise_13(astring):
    """
    Write a function to add 'ing' at the end of a given string (length should be at least 3). If the given string is
    already ends with 'ing' then add 'ly' instead.
    If the string length of the given string is less than 3, leave it unchanged.
    Sample String : 'abc'
    Expected Result : 'abcing'
    Sample String : 'string'
    Expected Result : 'stringly'
    """

def exercise_14(astring):
    """
    Write a function to find the first appearance of the substring 'not' and 'poor' from a given string, if 'poor'
    follows the 'not', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
    Hint: Strings have a find method.
    Sample String : 'The lyrics is not that poor!'
    Expected Result : 'The lyrics is good!'
    """

def exercise_15(list_of_strings):
    """
    Write a function that takes a list of words and returns the longest one.
    """

def exercise_16():
    """
    Write a function to test whether an input is an integer. Integers are instances of the class 'int'.
    Hint: https://docs.python.org/3/library/functions.html#isinstance
    """

"""
Exercise 17
In this example we are using a class to model a simple shopping list.

To use the shopping list we do:
>>> my_list = Excercise17ShoppingList()
>>> my_list.add_item('Banana', 0.80) # add one banana (amount defaults to 1)
>>> my_list.add_item('Milk 1l', 1.20, 3) # add three 1 liter bottles of milk

At the end we can ask my_list.total_sum() and it should tell us 4.40.

Implement the needed code for add_item and total_sum.

"""
class Exercise17ShoppingList:

    def __init__(self):
        self.list = []

    def add_item(self, item_name, item_price, item_amount=1):
        pass

    def total_sum(self):
        pass



"""
Exercise 18
Create a class that will do a lottery of a list of people.
Randomly choose n names from them group of people.
"""
class Exercise18Lottery:

    def __init__(self):
        pass

    def enter(self, name):
        pass

    def choose(self, number_of_people_to_choose):
        pass
