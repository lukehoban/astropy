import astropy.modeling.models as m
import astropy.modeling.separable

# Test 1: Simple compound model
cm = m.Linear1D(10) & m.Linear1D(5)
print("Test 1 - Simple compound model:")
print(separability_matrix(cm))
print()

# Test 2: Complex model
complex_model = m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5)
print("Test 2 - Complex model:")
print(separability_matrix(complex_model))
print()

# Test 3: Nested compound model (shows the bug)
nested_model = m.Pix2Sky_TAN() & cm
print("Test 3 - Nested compound model:")
print(separability_matrix(nested_model))