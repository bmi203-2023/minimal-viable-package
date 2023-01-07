import pytest
from example import welcome 

def test_greeting():

    assert welcome.Greeting().the_world == 'Hello, World!'

    guiding_principles = welcome.Greeting().the_zen_of_python('./data/the-zen-of-python.txt')
    assert guiding_principles[2] == 'Simple is better than complex.'
    assert len(guiding_principles) == 19

    assert welcome.Greeting().a_person(named='Andrew') == 'Hello, Andrew!'