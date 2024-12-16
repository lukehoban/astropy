import numpy as np
from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

def print_separability(model, title):
    print(f"\n{title}:")
    print(model)
    print("Separability matrix:")
    print(separability_matrix(model))
    print("-" * 50)

# Test 1: Simple compound model
cm = m.Linear1D(10) & m.Linear1D(5)
print_separability(cm, "Test 1: Simple compound model (Linear1D & Linear1D)")

# Test 2: Complex compound model
model2 = m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5)
print_separability(model2, "Test 2: Complex compound model (Pix2Sky_TAN & Linear1D & Linear1D)")

# Test 3: Nested compound model - the bug case
nested = m.Pix2Sky_TAN() & cm
print_separability(nested, "Test 3: Nested compound model (Pix2Sky_TAN & (Linear1D & Linear1D))")

# Test 4: More complex nesting
nested2 = (m.Linear1D(1) & m.Linear1D(2)) & (m.Linear1D(3) & m.Linear1D(4))
print_separability(nested2, "Test 4: Double nested models ((Linear1D & Linear1D) & (Linear1D & Linear1D))")