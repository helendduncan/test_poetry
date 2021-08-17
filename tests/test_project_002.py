from project_002 import __version__
from sup_002.hello import hello
from project_002.maths import add_one, add_two, times_three
from process.allin import reader

def test_reader():
    assert reader('../demo_data/example_input_001.csv') == 'Using file ../demo_data/example_input_001.csv'
    
def test_version():
    assert __version__ == '0.1.2'

def test_hello():
    assert hello() == "Howdy Stranger"

def test_add_one():
    assert add_one() == 1
    assert add_one(3) == 4

def test_add_two():
    assert add_two() == 2
    assert add_two(4) == 6

def test_times_three():
    assert times_three() == 0
    assert times_three(7) == 21

