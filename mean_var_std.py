import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    flat = np.array(list) # flattened array
    matrix = np.array(list).reshape(3, 3) # matrix

    results = {}

    results['mean'] = [matrix.mean(axis = 0).tolist(), matrix.mean(axis = 1).tolist(), flat.mean()]

    results['variance'] = [matrix.var(axis = 0).tolist(), matrix.var(axis = 1).tolist(), flat.var()]

    results['standard deviation'] = [matrix.std(axis = 0).tolist(), matrix.std(axis = 1).tolist(), flat.std()]

    results['max'] = [matrix.max(axis = 0).tolist(), matrix.max(axis = 1).tolist(), flat.max()]

    results['min'] = [matrix.min(axis = 0).tolist(), matrix.min(axis = 1).tolist(), flat.min()]

    results['sum'] = [matrix.sum(axis = 0).tolist(), matrix.sum(axis = 1).tolist(), flat.sum()]

    return results