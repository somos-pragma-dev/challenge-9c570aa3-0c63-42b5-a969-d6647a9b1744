import subprocess
import pytest

@pytest.mark.parametrize('num1, num2, expected', [(1, 2, 'La suma es: 3.0'), (4, 5, 'La suma es: 9.0')])
def test_sum(num1, num2, expected):
    result = subprocess.run(['python', 'src/main.py', str(num1), str(num2)], capture_output=True, text=True)
    assert result.stdout.strip() == expected

def test_invalid_input():
    result = subprocess.run(['python', 'src/main.py', 'a', 'b'], capture_output=True, text=True)
    assert result.stdout.strip() == 'Error: Por favor ingrese números válidos.'