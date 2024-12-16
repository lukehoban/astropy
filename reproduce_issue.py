from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

# Test case 1: Simple compound model
cm = m.Linear1D(10) & m.Linear1D(5)
print("\nTest case 1 - Simple compound model:")
print(separability_matrix(cm))

# Test case 2: More complex compound model
print("\nTest case 2 - Complex compound model:")
print(separability_matrix(m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5)))

# Test case 3: Nested compound model
print("\nTest case 3 - Nested compound model:")
print(separability_matrix(m.Pix2Sky_TAN() & cm))