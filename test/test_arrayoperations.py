import numpy as np
import uebung.Dataanalytics.arrayoperations as arrayops

def test_array_1d_values():
    assert arrayops.array_1d.tolist() == [1, 2, 3, 4, 5, 6]

def test_matrix_1_shape():
    assert arrayops.matrix_1.shape == (2, 3)

def test_elementwise_multiplication():
    result = arrayops.matrix_1 * arrayops.matrix_2
    expected = np.array([[6, 10, 12], [9, 8, 5]])
    assert np.array_equal(result, expected)

def test_dot_product_shape():
    result = np.dot(arrayops.matrix_1, arrayops.matrix_2.T)
    assert result.shape == (2, 2)

def test_dot_product_values():
    result = np.dot(arrayops.matrix_1, arrayops.matrix_2.T)
    expected = np.array([[28, 10], [58, 22]])
    assert np.array_equal(result, expected)