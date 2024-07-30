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
    return [random.randint(1, 6) for _ in range(5)]
   

def exercise_1_variant(anumber: int) -> list:
    """
    Exercise 1 variant: Write a function which returns a list with variable number
    of dice rolls.
    """
    return [random.randint(1, 6) for _ in range(anumber)]

def exercise_2(alist): # since list is a keyword in python, you sould not use it as argument name
    """
    Exercise 2 : Write a function that returns the length of a given list
    """
    return len(alist)

def exercise_3_intro(alist):
    """
    Exercise 3 intro : To solve the the next exercise I'd like to introduce loops. Loops are
    good for inspecting and or modifying items in a list or a dict. In this example we loop
    over a list of numbers and incremente every item by 1.
    """
    new_list = []
    for item in alist: # item is a variable that contains the current item if alist.
        new_list.append(item + 1)
    return new_list

def exercise_3_intro_variant(alist):
    """
    The last example is nice, but since such scenarios are so common, python has the concept
    of comprehensions. Same functionality, but much much more compact. We create the new_list
    'on the fly'.
    """
    return [item + 1 for item in alist]

def exercise_3(list_of_number_pairs):
    """
    Write a python program that sums pairs.
    ((1, 2), (100, 20)) -> (3,120)
    """
    return sum(sum(pair) for pair in list_of_number_pairs)

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
    if not alist_of_numbers:
        return None
    return max(alist_of_numbers)

def exercise_5(alist_of_numbers):
    """
    Write a function to get the smallest number from a list.
    """
    if not alist_of_numbers:
        return None
    return min(alist_of_numbers)

def exercise_6(rand_start=1, rand_end=10, rand_count=10):
    """
    Write a function that generates rand_count random numbers. The numbers should be between
    rand_start and rand_end including both.
    """
    return [random.randint(rand_start, rand_end) for _ in range(rand_count)]

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
    char_frequency = {}
    for char in astring:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency

def exercise_8(alist_of_strings):
    """
    Write a function to count the number of strings in a list where the string length is 2 or more
    and the first and last character are same.

    Sample List : ['abc', 'xyz', 'aba', '1221']
    Expected Result : 2
    """
    count = 0
    for s in alist_of_strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count

def exercise_9_intro(a_list_of_numbers):
    """
    Write a function that sorts a list of numbers. See https://docs.python.org/3/howto/sorting.html
    Sample List: [100, 30, 7, 4, 9]
    Expected Result: [4, 7, 9, 30, 100]
    """
    return sorted(a_list_of_numbers)

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
    return sorted(a_list_of_tuples, key=lambda x: x[1])

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
    if len(astring) < 3:
        return ""
    return astring[:2] + astring[-2:]

def exercise_11(astring):
    """
    Write a function to get a string from a given string where all occurrences of its first char have been changed to
    '$', except the first char itself. Take a look at the documentation of string methods:
    https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
    replace is probably what you need.

    Sample String : 'restart'
    Expected Result : 'resta$t'
    """
    if not astring:
        return ""
    first_char = astring[0]
    return first_char + astring[1:].replace(first_char, "$")

def exercise_12(stringa,stringb):
    """
    Write a function to get a single string from two given strings, separated by a space and swap the first two
    characters of each string.
    Sample String : 'abc', 'xyz'
    Expected Result : 'xyc abz'
    """
    if len(stringa) < 2 or len(stringb) < 2:
        return "Both strings must have at least two characters."
    new_stringa = stringb[:2] + stringa[2:]
    new_stringb = stringa[:2] + stringb[2:]
    return f"{new_stringa} {new_stringb}"

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
    if len(astring) < 3:
        return astring
    if astring.endswith("ing"):
        return astring + "ly"
    else:
        return astring + "ing"
    
def exercise_14(astring):
    """
    Write a function to find the first appearance of the substring 'not' and 'poor' from a given string, if 'poor'
    follows the 'not', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.
    Hint: Strings have a find method.
    Sample String : 'The lyrics is not that poor!'
    Expected Result : 'The lyrics is good!'
    """
    not_index = astring.find("not")
    poor_index = astring.find("poor")
    if not_index != -1 and poor_index != -1 and poor_index > not_index:
        return astring[:not_index] + "good" + astring[poor_index + 4 :]
    return astring

def exercise_15(list_of_strings):
    """
    Write a function that takes a list of words and returns the longest one.
    """
    if not list_of_strings:
        return ""
    return max(list_of_strings, key=len)

def exercise_16(input_value):
    """
    Write a function to test whether an input is an integer. Integers are instances of the class 'int'.
    Hint: https://docs.python.org/3/library/functions.html#isinstance
    """
    return isinstance(input_value, int)
 
class Exercise17ShoppingList:
    """
    Exercise 17: Implement a simple shopping list class.
    """

    def __init__(self):
        """Initialize an empty shopping list."""
        self.list = []

    def add_item(self, item_name, item_price, item_amount=1):
        """
     Add an item to the shopping list.

        Args:
        item_name (str): The name of the item.
        item_price (float): The price of the item.
        item_amount (int, optional): The amount of the item. Defaults to 1.
        """
        self.list.append((item_name, item_price, item_amount))

    def total_sum(self):
        """
        Calculate the total sum of all items in the shopping list.

        Returns:
        float: The total sum of all items, rounded to 2 decimal places.
        """
        total = sum(
            item_price * item_amount for _, item_price, item_amount in self.list
        )
        return round(total, 2)


# Create and populate the shopping list for the test
my_list = Exercise17ShoppingList()
my_list.add_item("Banana", 0.80)
my_list.add_item("Milk 1l", 1.20, 3)


class Exercise18Lottery:
    """
    Exercise 18: Implement a simple lottery class.
    """

    def __init__(self):
        """Initialize an empty list of participants."""
        self.participants = []

    def enter(self, name):
        """
        Enter a participant into the lottery.

        Args:
        name (str): The name of the participant.
        """
        self.participants.append(name)

    def choose(self, number_of_people_to_choose):
        """
        Choose winners from the lottery participants.

        Args:
        number_of_people_to_choose (int): The number of winners to choose.

        Returns:
        list: A list of randomly chosen winners.

        Raises:
        ValueError: If there are not enough participants to choose from.
        """
        if number_of_people_to_choose > len(self.participants):
            raise ValueError("Not enough participants to choose from")
        return random.sample(self.participants, number_of_people_to_choose)


def exercise_18(participants, num_winners):
    """
    Exercise 18: Create a lottery from a list of participants and choose winners.

    Args:
    participants (list): A list of participant names.
    num_winners (int): The number of winners to choose.

    Returns:
    list: A list of randomly chosen winners.
    """
    lottery = Exercise18Lottery()
    for participant in participants:
        lottery.enter(participant)
    return lottery.choose(num_winners)