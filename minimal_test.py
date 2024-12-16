import numpy as np
from astropy.modeling.core import Model, CompoundModel
from astropy.modeling.separable import _cstack, _coord_matrix, _compute_n_outputs

# Mock classes
class MockModel(Model):
    def __init__(self, name, separable=True, n_inputs=1, n_outputs=1):
        self.name = name
        self.separable = separable
        self._n_inputs = n_inputs
        self._n_outputs = n_outputs
        super().__init__()
    
    @property
    def n_inputs(self):
        return self._n_inputs

    @property
    def n_outputs(self):
        return self._n_outputs

# Test cases
m1 = MockModel("m1", separable=True, n_inputs=1, n_outputs=1)
m2 = MockModel("m2", separable=True, n_inputs=1, n_outputs=1)
cm = m1 & m2  # Simple compound model

print("\nTest case 1 - Simple compound model:")
result = _cstack(m1, m2)
print(result)

m3 = MockModel("m3", separable=False, n_inputs=2, n_outputs=2)
print("\nTest case 2 - Complex model without nesting:")
result = _cstack(m3, m1 & m2)
print(result)

print("\nTest case 3 - Nested compound model:")
result2 = _cstack(m3, cm)
print(result2)