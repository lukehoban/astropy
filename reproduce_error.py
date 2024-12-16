from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

# Simple compound model case
cm = m.Linear1D(10) & m.Linear1D(5)
print("Simple compound model (should be diagonal):")
print(separability_matrix(cm))
print()

# Complex model case
print("Complex model with Pix2Sky_TAN() & Linear1D & Linear1D:")
print(separability_matrix(m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5)))
print()

# Nested compound model case
print("Nested compound model case (currently incorrect):")
print(separability_matrix(m.Pix2Sky_TAN() & cm))