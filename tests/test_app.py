import sys
from pathlib import Path
import pytest
import math

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, sub, mul, div, log, square, sin, cos, sqrt, percentage

# Tests for add function
def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_mixed_numbers():
    assert add(2, -3) == -1

def test_add_zero():
    assert add(5, 0) == 5

# Tests for sub function
def test_sub_positive_numbers():
    assert sub(5, 2) == 3

def test_sub_negative_numbers():
    assert sub(-5, -2) == -3

def test_sub_mixed_numbers():
    assert sub(5, -2) == 7

def test_sub_zero():
    assert sub(5, 0) == 5
    assert sub(0, 5) == -5

# Tests for mul function
def test_mul_positive_numbers():
    assert mul(2, 3) == 6

def test_mul_negative_numbers():
    assert mul(-2, -3) == 6

def test_mul_mixed_numbers():
    assert mul(2, -3) == -6

def test_mul_by_zero():
    assert mul(5, 0) == 0

def test_mul_by_one():
    assert mul(5, 1) == 5

# Tests for div function
def test_div_positive_numbers():
    assert div(6, 3) == 2

def test_div_negative_numbers():
    assert div(-6, -3) == 2

def test_div_mixed_numbers():
    assert div(6, -3) == -2

def test_div_by_one():
    assert div(5, 1) == 5

def test_div_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        div(5, 0)

# Tests for log function
def test_log_positive_number():
    assert log(10) == pytest.approx(2.30258509299)
    assert log(1) == 0

def test_log_non_positive_number():
    with pytest.raises(ValueError, match="Cannot calculate logarithm of a non-positive number"):
        log(0)
    with pytest.raises(ValueError, match="Cannot calculate logarithm of a non-positive number"):
        log(-1)

# Tests for square function
def test_square_positive_number():
    assert square(5) == 25

def test_square_negative_number():
    assert square(-5) == 25

def test_square_zero():
    assert square(0) == 0

# Tests for sin function
def test_sin():
    assert sin(0) == 0
    assert sin(math.pi / 2) == 1
    assert sin(math.pi) == pytest.approx(0)

# Tests for cos function
def test_cos():
    assert cos(0) == 1
    assert cos(math.pi / 2) == pytest.approx(0)
    assert cos(math.pi) == -1

# Tests for sqrt function
def test_sqrt_positive_number():
    assert sqrt(25) == 5
    assert sqrt(0) == 0

def test_sqrt_negative_number():
    with pytest.raises(ValueError, match="Cannot calculate square root of a negative number"):
        sqrt(-1)

# Tests for percentage function
def test_percentage():
    assert percentage(50, 100) == 50
    assert percentage(25, 50) == 50
    assert percentage(10, 200) == 5
    assert percentage(0, 100) == 0

def test_percentage_with_zero_base():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        percentage(10, 0)