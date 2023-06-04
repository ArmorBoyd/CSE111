from guessing_game import generate_number, compare_numbers, compute_difference, \
     validate_input
import pytest


def test_generate_number():

    start = 1
    end = 100
    number = generate_number(start, end)
    assert start <= number <= end, "Generated number is outside the specified range"

def test_compare_numbers():
    assert compare_numbers(5, 10) == "Higher!"
    assert compare_numbers(15, 10) == "Lower!"
    assert compare_numbers(10, 10) == "equal"

def test_compute_difference():
    #Test function for compute_difference()
    assert compute_difference(5, 10) == 5, "Difference calculation test failed"
    assert compute_difference(15, 10) == 5, "Difference calculation test failed"
    assert compute_difference(10, 10) == 0, "Difference calculation test failed"

def test_validate_input():
    #Test function for validate_input()
    assert validate_input("10") == True, "Input validation test failed"
    assert validate_input("abc") == False, "Input validation test failed"





# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
