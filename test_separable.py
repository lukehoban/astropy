import sys
sys.path.insert(0, '/tmp/repo-lukehoban-astropy-1-c6cbe2')

from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

# Test 1 - Simple compound model
cm = m.Linear1D(10) & m.Linear1D(5)
print("Test 1 - Simple compound model:")
print(separability_matrix(cm))
print()

# Test 2 - Complex model
print("Test 2 - Complex model:")
complex_model = m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5)
print(separability_matrix(complex_model))
print()

# Test 3 - Nested compound model
print("Test 3 - Nested compound model:")
nested_model = m.Pix2Sky_TAN() & cm  # Using the compound model from Test 1
print(separability_matrix(nested_model))