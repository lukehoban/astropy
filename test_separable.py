import numpy as np
from astropy.modeling.core import Model, CompoundModel
from astropy.modeling.separable import separability_matrix, _coord_matrix, _cstack, _compute_n_outputs

class DummyModel(Model):
    def __init__(self, n_inputs=1, n_outputs=1, separable=True):
        self._n_inputs = n_inputs
        self._n_outputs = n_outputs
        self._separable = separable
        super().__init__()

    @property
    def n_inputs(self):
        return self._n_inputs

    @property
    def n_outputs(self):
        return self._n_outputs

    @property
    def separable(self):
        return self._separable

# Create models to simulate the issue
linear1 = DummyModel(n_inputs=1, n_outputs=1, separable=True)
linear2 = DummyModel(n_inputs=1, n_outputs=1, separable=True)
tan = DummyModel(n_inputs=2, n_outputs=2, separable=False)

# Create compound models
cm = linear1 & linear2  # Basic compound model
complex_model = tan & linear1 & linear2  # Complex model
nested_model = tan & cm  # Nested compound model - problematic case

print("Test 1 - Basic compound model:")
print(separability_matrix(cm))
print()

print("Test 2 - Complex model:")
print(separability_matrix(complex_model))
print()

print("Test 3 - Nested compound model:")
print(separability_matrix(nested_model))