import numpy as np
from numpy.linalg import norm
from scipy.linalg import sqrtm

def fidelity(rho, sigma):
    sqrt_rho = sqrtm(rho)
    product = sqrtm(sqrt_rho @ sigma @ sqrt_rho)
    return np.real(np.trace(product)) ** 2

def trace_distance(rho, sigma):
    return 0.5 * norm(rho - sigma, ord='nuc')

