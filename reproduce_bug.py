from astropy.modeling import models as m 
from astropy.modeling.separable import separability_matrix

# Test case 1: Simple compound model
cm = m.Linear1D(10) & m.Linear1D(5)
print("Test case 1 - Simple compound model:")
print(separability_matrix(cm))
print()

# Test case 2: Complex model without nesting 
print("Test case 2 - Complex model without nesting:")
print(separability_matrix(m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5)))
print()

# Test case 3: Complex model with nesting - shows bug
print("Test case 3 - Complex model with nesting (bug):")
print(separability_matrix(m.Pix2Sky_TAN() & cm))