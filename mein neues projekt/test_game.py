import n_in_a_row
import pytest


def trim_game(ascii_game):
    return '\n'.join([i.strip() for i in ascii_game.splitlines()])
t = trim_game

def test_new_game():
    assert n_in_a_row.Game(3,3).ascii() == t("""
    ...
    ...
    ...
    """)

    assert n_in_a_row.Game(4,3).ascii() == t("""
    ....
    ....
    ....
    """)

    assert n_in_a_row.Game(3,4).ascii() == t("""
    ...
    ...
    ...
    ...
    """)

def test_n_in_a_row():
    game = n_in_a_row.Game(3,3,win=3)
    assert game.count_fields == 0
    assert game.game_status == 'active'
    assert game.turn_color == None
    # drop first field
    field = game.drop('x',0)
    assert game.game_status == 'active'
    assert field.position == (0,0)
    assert field.color == 'x'
    assert game.ascii() == t("""
    ...
    ...
    x..
    """)
    assert game.count_fields == 1
    assert game.turn_color == 'o'
    # drop second field
    field = game.drop('o',0)
    assert game.game_status == 'active'
    assert field.position == (0,1)
    assert field.color == 'o'
    assert game.ascii() == t("""
    ...
    o..
    x..
    """)
    assert game.count_fields == 2
    assert game.turn_color == 'x'

    # dropping the wrong color should raise an error
    with pytest.raises(Exception):
        field = game.drop('o',1)

    # drop third field
    field = game.drop('x',1)
    assert game.game_status == 'active'
    assert field.position == (1,0)
    assert field.color == 'x'
    assert game.ascii() == t("""
    ...
    o..
    xx.
    """)
    assert game.count_fields == 3
    assert game.turn_color == 'o'
    # drop fourth field
    field = game.drop('o',0)
    assert game.game_status == 'active'
    assert field.position == (0,2)
    assert field.color == 'o'
    assert game.ascii() == t("""
    o..
    o..
    xx.
    """)
    assert game.count_fields == 4
    # drop fifth field
    field = game.drop('x',2)
    assert game.game_status == 'over'
    assert game.won_by == 'x'
    assert field.position == (2,0)
    assert field.color == 'x'
    assert game.ascii() == t("""
    o..
    o..
    xxx
    """)
    assert game.count_fields == 5

def test_n_in_a_row_2():
    game = n_in_a_row.Game(5,5,win=3)
    assert game.count_fields == 0
    assert game.game_status == 'active'
    assert game.turn_color == None
    # drop first field
    field = game.drop('x',0)
    assert game.game_status == 'active'
    assert field.position == (0,0)
    assert field.color == 'x'
    assert game.ascii() == t("""
    .....
    .....
    .....
    .....
    x....
    """)
    assert game.count_fields == 1
    assert game.turn_color == 'o'
    # drop second field
    field = game.drop('o',0)
    assert game.game_status == 'active'
    assert field.position == (0,1)
    assert field.color == 'o'
    assert game.ascii() == t("""
    .....
    .....
    .....
    o....
    x....
    """)
    assert game.count_fields == 2
    assert game.turn_color == 'x'

    # dropping the wrong color should raise an error
    with pytest.raises(Exception):
        field = game.drop('o',1)

    # drop third field
    field = game.drop('x',1)
    assert game.game_status == 'active'
    assert field.position == (1,0)
    assert field.color == 'x'
    assert game.ascii() == t("""
    .....
    .....
    .....
    o....
    xx...
    """)
    assert game.count_fields == 3
    assert game.turn_color == 'o'
    # drop fourth field
    field = game.drop('o',0)
    assert game.game_status == 'active'
    assert field.position == (0,2)
    assert field.color == 'o'
    assert game.ascii() == t("""
    .....
    .....
    o....
    o....
    xx...
    """)
    assert game.count_fields == 4
    # drop fifth field
    field = game.drop('x',2)
    assert game.game_status == 'over'
    assert game.won_by == 'x'
    assert field.position == (2,0)
    assert field.color == 'x'
    assert game.ascii() == t("""
    .....
    .....
    o....
    o....
    xxx..
    """)
    assert game.count_fields == 5

def test_load_game():
    """
    The Game class should provide a load method to load a predefined game.
    the load method should be implemented as a static method like this:

    >>> class Test:
    >>>     @staticmethod
    >>>     def a_static_factory():
    >>>        t = Test()
    >>>        # do something with t and return it
    >>>        return t

    the load function accepts a game layout. It retrieves the dimensions of the game
    and loads the provided data into the game.
    """

    game = n_in_a_row.Game.load(t("""
    o..
    o..
    xxx
    """))

def test_axis_strings():
    game = n_in_a_row.Game.load(t("""
    o..
    o..
    xxx
    """))

    # get the axis strings in this order:  | \ / -
    axis_strings = game.axis_strings(0,0)
    assert axis_strings[0] == 'xoo'
    assert axis_strings[1] == 'x'
    assert axis_strings[2] == 'x..'
    assert axis_strings[3] == 'xxx' # the winner :-)

def test_check_win():
    game = n_in_a_row.Game.load(t("""
    .....
    .....
    .....
    xx...
    xooo.
    """))
    assert game.count_fields == 0
    assert game.game_status == 'active'
    assert game.turn_color == None
    # drop first field
    field = game.drop('o', 4)
    assert game.game_status == 'over'
    assert game.won_by == 'o'
    assert field.position == (4,0)
    assert field.color == 'o'
    assert game.ascii() == t("""
    .....
    .....
    .....
    xx...
    xoooo
    """)
    assert game.count_fields == 1

def test_check_win_2():
    game = n_in_a_row.Game.load(t("""
    .....
    .....
    .....
    xx...
    xoo.o
    """))
    assert game.count_fields == 0
    assert game.game_status == 'active'
    assert game.turn_color == None
    # drop first field
    field = game.drop('o', 3)
    assert game.game_status == 'over'
    assert game.won_by == 'o'
    assert field.position == (3,0)
    assert field.color == 'o'
    assert game.ascii() == t("""
    .....
    .....
    .....
    xx...
    xoooo
    """)
    assert game.count_fields == 1