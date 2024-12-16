import numpy as np
from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

def assert_equal(a, b, msg=""):
    if not np.array_equal(a, b):
        print(f"FAIL: {msg}")
        print("Expected:")
        print(b)
        print("Got:")
        print(a)
    else:
        print(f"PASS: {msg}")

# Test case 1: Basic compound model
cm = m.Linear1D(10) & m.Linear1D(5)
expected1 = np.array([[True, False],
                     [False, True]])
result1 = separability_matrix(cm)
assert_equal(result1, expected1, "Basic compound model")

# Test case 2: Complex model without nesting
complex_model = m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5)
expected2 = np.array([[True, True, False, False],
                     [True, True, False, False],
                     [False, False, True, False],
                     [False, False, False, True]])
result2 = separability_matrix(complex_model)
assert_equal(result2, expected2, "Complex model without nesting")

# Test case 3: Nested compound model (showing the bug)
nested_model = m.Pix2Sky_TAN() & cm
expected3 = np.array([[True, True, False, False],
                     [True, True, False, False],
                     [False, False, True, False],
                     [False, False, False, True]])
result3 = separability_matrix(nested_model)
assert_equal(result3, expected3, "Nested compound model")