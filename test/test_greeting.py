"""
UCSF BMI203: Biocomputing Algorithms Winter 2023
Author: Andrew Blair
Date: 1.06.23
Program: test_greeting.py
Description: Test the welcome package's Greeting class.
"""

import pytest
from example import welcome 

def test_greeting():
    """
    Unit test for the example package's welcome class.
    """

    assert welcome.Greeting().the_world == 'Hello, World!' # Check if the Greeting class attribute is set properly

    # Check if Greeting.the_zen_of_python reads the zen of python and returns it as a list, where each aphorism line is an element.
    guiding_principles = welcome.Greeting().the_zen_of_python('./data/the-zen-of-python.txt')
    assert guiding_principles[2] == 'Simple is better than complex.'
    assert len(guiding_principles) == 19

    # Check if Greeting.a_person returns a welcome message with the name of the person that was passed as a parameter.
    assert welcome.Greeting().a_person(named='Andrew') == 'Hello, Andrew!'
