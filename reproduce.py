from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

print("Test 1: Simple compound model separability")
cm = m.Linear1D(10) & m.Linear1D(5)
print(separability_matrix(cm))
print("\nExpected: Diagonal matrix [[True, False], [False, True]]")
print("----------------------------------")

print("\nTest 2: Complex compound model separability")
model2 = m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5)
print(separability_matrix(model2))
print("\nExpected: Block diagonal matrix showing independence")
print("----------------------------------")

print("\nTest 3: Nested compound model separability (current bug)")
nested = m.Pix2Sky_TAN() & cm
print(separability_matrix(nested))
print("\nExpected: Same pattern as Test 2, but showing independence")