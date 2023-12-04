import sys
from os.path import abspath, dirname
sys.path.insert(0, dirname(dirname(abspath(__file__))))

from src.guideline import add

def test_addition():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(10, -5) == 5