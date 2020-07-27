# If you get any issues while importing the following modules,
# try to deactivate and activate the venv

# To execute the test scripts:
# Change directory to the project folder
# cd <project_folder>
# source venv/bin/activate
# pytest src/tests

# NOTE: you can use the following options while
# executing the pytest:
# -v for verbose
# -s if you want to execute the print statements in the test cases


from src.examples.calculator import Calculator
from src.exceptions import exceptions
import pytest


# Example code to test add function
def test_add():
    c = Calculator()
    assert c.add(1, 3) == 4


# Example code to test exceptions
def test_add_exception():
    c = Calculator()
    with pytest.raises(exceptions.CalculatorException) as context:
        c.add('a', 1)
    assert str(context.value) == 'The supplied argument a is not numeric'


# Run a series of tests on a bunch of inputs
# We need to use a decorator
@pytest.mark.parametrize(
    'a, b, expected', [
        (1, 2, 3),
        (2, 1, 3),
        (30, 40, 70),
        (-10, 10, 0)
    ]
)
def test_with_parms(a, b, expected):
    c = Calculator()
    assert c.add(a, b) == expected

# It is always advisable to group the test cases into different classes,
# based on the functions that you test. For instance, group all the add()
# test cases under the class TestAdd. This way get 2 advantages:
# 1. The code looks organized
# 2. You can confine your pytest execution to a specific class.
# For ex, to execute the test cases in TestAdd class:
# pytest test_calculator.py::TestAdd


class TestAdd:
    @pytest.mark.parametrize(
        'a,b,expected', [(1, 2, 3),
                         (10, 20, 30),
                         (0, 1, 1),
                         (0, -1, -1),
                         (-1, 1, 0),
                         (0, 0, 0),
                         (-2, 1, -1)]
    )
    def test_add(self, a, b, expected):
        c = Calculator()
        assert c.add(a, b) == expected

    # Test exceptions
    @pytest.mark.parametrize('a,b,expected', [
        ('a', 'b', 'The supplied argument a is not numeric'),
        ('a', 1, 'The supplied argument a is not numeric'),
        (1, 'b', 'The supplied argument b is not numeric')
    ])
    def test_add_exceptions(self, a, b, expected):
        c = Calculator()
        with pytest.raises(exceptions.CalculatorException) as context:
            c.add(a, b)

        assert str(context.value) == expected

    # monkeypatch
    # monkeypatch can replace any function in your source code with a different
    # function. For instance, if your code connects to a hive database, then
    # for your test cases, you can just replace that source function in your
    # test program, and generate some fake data.

    # In the following code we will replace the Calculator's add() function to
    # always return 42 value

    def test_add_fixture_demo(self, monkeypatch):
        c = Calculator()

        def fake_add(self, a, b):
            return 42
        monkeypatch.setattr(Calculator, "add", fake_add)
        assert c.add('a', 'b') == 42
        assert c.add(2, 1) == 42
