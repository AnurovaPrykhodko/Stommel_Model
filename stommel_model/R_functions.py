import numpy as np

def R_linear(t, R_const, A):
    return R_const + A*t

def R_sudden(t, R_const, A, start, finish):
    """Give sudden value of freshwater supply, A, during a certain interval, otherwise R_const."""
    condition = np.logical_and(start <= t, t <= finish)
    result = np.where(condition, A, R_const)
    return result

def R_oscillating(t, R_const, a, w):
    return a * np.sin(w*t) + R_const