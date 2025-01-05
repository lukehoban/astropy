import pytest
import numpy as np
from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

def test_nested_compound_model_separability():
    # Simple compound model
    cm = m.Linear1D(10) & m.Linear1D(5)
    mat1 = separability_matrix(cm)
    assert np.array_equal(mat1, np.array([[True, False],
                                        [False, True]]))

    # More complex model
    mat2 = separability_matrix(m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5))
    assert np.array_equal(mat2, np.array([[True, True, False, False],
                                        [True, True, False, False],
                                        [False, False, True, False],
                                        [False, False, False, True]]))

    # Nested compound model
    mat3 = separability_matrix(m.Pix2Sky_TAN() & cm)
    assert np.array_equal(mat3, np.array([[True, True, False, False],
                                        [True, True, False, False],
                                        [False, False, True, False],
                                        [False, False, False, True]]))