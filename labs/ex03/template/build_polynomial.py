# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    # ***************************************************
    # INSERT YOUR CODE HERE
    # polynomial basis function: TODO
    # this function should return the matrix formed
    # by applying the polynomial basis to the input data
    # ***************************************************
	Phi = np.ones((len(x), degree+1))
	for j in range(1,degree+1):
		Phi[:,j] = Phi[:,j-1] * x
	return Phi 
