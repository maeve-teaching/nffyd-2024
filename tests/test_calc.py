import pythag.calc
import pytest

def test_example():
    '''Test for the example function'''

    # Arrange
    test_opp = 3
    test_adj = 5
    expected_output = 5.83095

    # Act
    output = pythag.calc.pythag(test_opp, test_adj)

    # Assert
    assert output == pytest.approx(expected_output, 0.1)

    # No cleanup needed