from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

# Test case 1: Simple compound model
cm = m.Linear1D(10) & m.Linear1D(5)
print("Simple compound model:")
print(separability_matrix(cm))
print()

# Test case 2: Complex but non-nested model
complex_model = m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5)
print("Complex non-nested model:")
print(separability_matrix(complex_model))
print()

# Test case 3: Nested compound model
nested_model = m.Pix2Sky_TAN() & cm
print("Nested compound model:")
print(separability_matrix(nested_model))
print()