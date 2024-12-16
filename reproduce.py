from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

# Test 1: Basic compound model
cm = m.Linear1D(10) & m.Linear1D(5)
print("Test 1 - Basic compound model:")
print(separability_matrix(cm))
print()

# Test 2: More complex model
print("Test 2 - Complex model:")
print(separability_matrix(m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5)))
print()

# Test 3: Nested compound model - the problematic case
print("Test 3 - Nested compound model:")
print(separability_matrix(m.Pix2Sky_TAN() & cm))