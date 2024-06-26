# -*- coding: utf-8 -*-
"""Ejercicio5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OZ7IAWYaaih8Saak3CtBGHkSemCx0poN
"""

import numpy as np
import scipy.sparse as sp
import multiprocessing as mp

def multiply_row(args):
    A_row, B = args
    return A_row.dot(B)

def mul(A, B):
    A = A.tocsr()
    B = B.tocsc()
    pool = mp.Pool(mp.cpu_count())
    result = pool.map(multiply_row, [(A.getrow(i), B) for i in range(A.shape[0])])
    pool.close()
    pool.join()
    C = sp.vstack(result)
    return C
if __name__ == "__main__":
    np.random.seed(42)
    A = sp.random(1000, 1000, density=0.01, format='csr')
    B = sp.random(1000, 1000, density=0.01, format='csc')
    C = mul(A, B)
    print(C)