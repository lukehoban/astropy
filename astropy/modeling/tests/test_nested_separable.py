"""
Test separability of nested compound models.
"""
import pytest
import numpy as np
from numpy.testing import assert_allclose

from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix

def test_nested_compound_model_separability():
    # Simple compound model
    cm = m.Linear1D(10) & m.Linear1D(5)
    result = separability_matrix(cm)
    assert_allclose(result, np.array([[True, False],
                                    [False, True]]))

    # More complex model
    complex_model = m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5)
    result = separability_matrix(complex_model)
    assert_allclose(result, np.array([[True, True, False, False],
                                    [True, True, False, False],
                                    [False, False, True, False],
                                    [False, False, False, True]]))

    # Nested compound model
    nested_model = m.Pix2Sky_TAN() & cm
    result = separability_matrix(nested_model)
    assert_allclose(result, np.array([[True, True, False, False],
                                    [True, True, False, False],
                                    [False, False, True, False],
                                    [False, False, False, True]]))