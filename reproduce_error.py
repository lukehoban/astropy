from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

# Simple case - should show diagonal matrix
cm = m.Linear1D(10) & m.Linear1D(5)
print("\nSimple case:")
print(separability_matrix(cm))

# Complex case - should show block diagonal
print("\nComplex case:")
print(separability_matrix(m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5)))

# Nested case - currently wrong
print("\nNested case:")
print(separability_matrix(m.Pix2Sky_TAN() & cm))