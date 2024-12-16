from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

# Test case 1: Basic compound model
cm = m.Linear1D(10) & m.Linear1D(5)
print("Basic compound model:")
print(separability_matrix(cm))
print()

# Test case 2: Complex model without nesting
complex_model = m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5)
print("Complex model without nesting:")
print(separability_matrix(complex_model))
print()

# Test case 3: Nested compound model (showing the bug)
nested_model = m.Pix2Sky_TAN() & cm
print("Nested compound model:")
print(separability_matrix(nested_model))