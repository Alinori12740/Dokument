import exercise as ex

"""
Testing

Every exercise has to be tested to be sure everything is ok.

------------------------------------------------------------------------
Please provide tests for every exercise to show the expected behaviour.
------------------------------------------------------------------------

"""
# test_exercise 1
def test_exercise_1():
    assert len(ex.exercise_1()) == 5

def test_exercise_1_variant():
    assert len(ex.exercise_1_variant(100)) == 100
    assert len(ex.exercise_1_variant(12)) == 12

# test_exercise 2
def test_exercise_2():
    
    assert ex.exercise_2(['a', 'b', 'c']) == 3
    assert ex.exercise_2([]) == 0
    assert ex.exercise_2('abcdefg') == 7 # BONUS: why is this ? It is a string not a list...
                                            # The output of len is an int. In this case the number of the letters.

# test_exercise 3
def test_exercise_3_intro():
    assert ex.exercise_3_intro([1, 2, 3]) == [2, 3, 4]
    assert ex.exercise_3_intro([-1, -2, -3]) == [0, -1, -2]

def test_exercise_3_intro_variant():
    assert ex.exercise_3_intro_variant([1, 2, 3]) == [2, 3, 4]
    assert ex.exercise_3_intro_variant([-1, -2, -3]) == [0, -1, -2]

def test_exercise_3():
    assert ex.exercise_3(((8,9), (100,20), (27,44))) == 208

# test_exercise 4
def test_exercise_4_intro():
    assert ex.exercise_4_intro([4, -2, -2, 0]) == ['positive', 'negative', 'negative', 'zero']

def test_exercise_4():
    assert ex.exercise_4((999, 54, 212, 83)) == 999

# test_exercise 5
def test_exercise_5():
    assert ex.exercise_5((212, 89, 4, 12, 10000)) == 4

# test_exercise 6
def test_exercise_6():
    assert len(ex.exercise_6(5, 500, 10))  == 10
    assert ([i<=500 for i in ex.exercise_6(5, 500, 10)])
    assert ([i>=500 for i in ex.exercise_6(5, 500, 10)])

# test_exercise 7
def test_exercise_7():
    assert ex.exercise_7('google.com') == {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

# test_exercise 8
def test_exercise_8():
    assert ex.exercise_8(['abc', 'xyz', 'aba', '1221', '2956892', '7']) == 3
    
# test_exercise 9
def test_exercise_9_intro():
    assert ex.exercise_9_intro((3, 42, 9,  1, 99)) == [1, 3, 9, 42, 99]

def test_exercise_9():
    assert ex.exercise_9(((2, 5), (1, 2), (4, 4), (2, 3), (2, 1))) == [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# test_exercise 10
def test_exercise_10_intro():
    assert ex.exercise_10_intro('hal','lo') == 'hallo'

def test_exercise_10_intro2():
    assert ex.exercise_10_intro2('Boom ', 10) == 'Boom Boom Boom Boom Boom Boom Boom Boom Boom Boom '

def test_exercise_10():
    assert ex.exercise_10('Hallo Welt') == 'Halt'
    assert ex.exercise_10('Ha') == ''
    assert ex.exercise_10('x') == ''
    assert ex.exercise_10('') == ''

# test_exercise 11
def test_exersice_11():
    assert ex.exercise_11('einstein') == 'einst$in'

# test_exercise 12
def test_exercise_12():
    assert ex.exercise_12('hello', 'world') == 'wollo herld'
    assert ex.exercise_12('abc', 'xyz') == 'xyc abz'
    assert ex.exercise_12('Christian', 'Meyer') == 'Meristian Chyer'

# test_exercise 13
def test_exercise_13():
    assert ex.exercise_13('abc') == 'abcing'
    assert ex.exercise_13('String') == 'Stringly'
    assert ex.exercise_13('Ok') == 'Ok'

# test_exercise 14
def test_exercise_14():
    assert ex.exercise_14('The lyrics is not that poor!') == 'The lyrics is good!'
    assert ex.exercise_14('To be poor is not the same as to be good') == 'To be poor is not the same as to be good'
    
# test_exercise 15
def test_exercise_15():
    assert ex.exercise_15(['Hallo',  'Welt', 'ich', 'bin', 'Christian']) == 'Christian'
    assert ex.exercise_15(['Hallo',  'Christian', 'ich', 'bin', 'dein', 'PC']) == 'Christian'

# test_exercise 16
def test_exercise_16():
    assert ex.exercise_16('Hallo') == False
    assert ex.exercise_16(5) == True

# test_exercise 17
def test_exercise_17():
    assert ex.my_list.total_sum() == 4.4

# test_exercise 18
def test_exercise_19():
    assert len(ex.exercise_18(['Andreas', 'Barbara', 'Christian', 'Daniel', 'Ernst', 'Fred', 'Günther', 'Hans', 'Ina', 'Julia', 'Katja'], 3)) == 3