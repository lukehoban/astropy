"""
Test the separability matrix for nested CompoundModels.
"""
import numpy as np
from astropy.modeling import models as m
from astropy.modeling.separable import separability_matrix
from numpy.testing import assert_allclose


def test_nested_compound_separability():
    """Test that separability matrix is correctly computed for nested compound models."""
    # Simple compound model with two Linear1D models
    cm = m.Linear1D(10) & m.Linear1D(5)
    assert_allclose(
        separability_matrix(cm),
        np.array([[True, False], [False, True]])
    )

    # More complex compound model with Pix2Sky_TAN and two Linear1D models
    complex_model = m.Pix2Sky_TAN() & m.Linear1D(10) & m.Linear1D(5)
    assert_allclose(
        separability_matrix(complex_model),
        np.array([[True, True, False, False],
                  [True, True, False, False],
                  [False, False, True, False],
                  [False, False, False, True]])
    )

    # Nested compound model
    nested_model = m.Pix2Sky_TAN() & cm
    assert_allclose(
        separability_matrix(nested_model),
        np.array([[True, True, False, False],
                  [True, True, False, False],
                  [False, False, True, False],
                  [False, False, False, True]])
    )

    # Testing another nesting level
    double_nested = m.Pix2Sky_TAN() & (m.Linear1D(10) & m.Linear1D(5) & m.Linear1D(2))
    result = separability_matrix(double_nested)
    assert result.shape == (5, 5)  # 2 outputs from Pix2Sky_TAN + 3 outputs from Linear1Ds
    # Check that outputs from Pix2Sky_TAN depend on its inputs only
    assert_allclose(result[0:2, 0:2], True)
    assert_allclose(result[0:2, 2:], False)
    # Check that each Linear1D output depends only on its input
    for i in range(3):
        assert result[2+i, 2+i]  # Diagonal should be True
        for j in range(5):
            if j != 2+i:  # Off-diagonal should be False
                assert not result[2+i, j]