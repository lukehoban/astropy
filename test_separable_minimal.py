import numpy as np

class Model:
    def __init__(self, n_inputs, n_outputs, separable=True):
        self.n_inputs = n_inputs
        self.n_outputs = n_outputs
        self.separable = separable

class CompoundModel(Model):
    def __init__(self, left, right, operator='&'):
        self.left = left 
        self.right = right
        self.op = operator
        if operator == '&':
            n_inputs = left.n_inputs + right.n_inputs
            n_outputs = left.n_outputs + right.n_outputs
        else:
            n_inputs = right.n_inputs
            n_outputs = right.n_outputs
        super().__init__(n_inputs, n_outputs)

class Linear1D(Model):
    def __init__(self, slope):
        super().__init__(1, 1, separable=True)

class TanModel(Model):
    def __init__(self):
        super().__init__(2, 2, separable=False)

def __and__(left, right):
    return CompoundModel(left, right, '&')

Model.__and__ = __and__

def _coord_matrix(model, pos, noutp):
    if not model.separable:
        mat = np.zeros((noutp, model.n_inputs))
        if pos == 'left':
            mat[:model.n_outputs, :model.n_inputs] = 1
        else:
            mat[-model.n_outputs:, -model.n_inputs:] = 1
    else:
        mat = np.zeros((noutp, model.n_inputs))
        for i in range(model.n_inputs):
            mat[i, i] = 1
        if pos == 'right':
            mat = np.roll(mat, (noutp - model.n_outputs))
    return mat

def _compute_n_outputs(left, right):
    if isinstance(left, Model):
        lnout = left.n_outputs
    else:
        lnout = left.shape[0]
    if isinstance(right, Model):
        rnout = right.n_outputs
    else:
        rnout = right.shape[0]
    return lnout + rnout

def _cstack(left, right):
    """
    Function corresponding to '&' operation.
    """
    noutp = _compute_n_outputs(left, right)

    if isinstance(left, Model):
        if isinstance(left, CompoundModel) and left.op == '&':
            cleft = _cstack(left.left, left.right)
        else:
            cleft = _coord_matrix(left, 'left', noutp)
    else:
        cleft = np.zeros((noutp, left.shape[1]))
        cleft[:left.shape[0], :left.shape[1]] = left

    if isinstance(right, Model):
        if isinstance(right, CompoundModel) and right.op == '&':
            cright = _cstack(right.left, right.right)
            # We need to adjust the right matrix to handle the proper output positions
            cright_adjusted = np.zeros((noutp, cright.shape[1]))
            cright_adjusted[-right.n_outputs:, :] = cright[-right.n_outputs:, :]
            cright = cright_adjusted
        else:
            cright = _coord_matrix(right, 'right', noutp)
    else:
        cright = np.zeros((noutp, right.shape[1]))
        cright[-right.shape[0]:, -right.shape[1]:] = 1

    return np.hstack([cleft, cright])

def _separable(transform):
    if isinstance(transform, CompoundModel):
        if transform.op == '&':
            return _cstack(transform.left, transform.right)
    return _coord_matrix(transform, 'left', transform.n_outputs)

def separability_matrix(transform):
    if transform.n_inputs == 1 and transform.n_outputs > 1:
        return np.ones((transform.n_outputs, transform.n_inputs), dtype=np.bool_)
    separable_matrix = _separable(transform)
    separable_matrix = np.where(separable_matrix != 0, True, False)
    return separable_matrix

# Test 1 - Simple compound model
cm = Linear1D(10) & Linear1D(5)
print("Test 1 - Simple compound model:")
print(separability_matrix(cm))
print()

# Test 3 - Nested compound model
print("Test 3 - Nested compound model:")
nested_model = TanModel() & cm
print(separability_matrix(nested_model))