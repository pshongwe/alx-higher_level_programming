#!/usr/bin/python3
"""Defines matrix multiplication function."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.
    """
    if not all(isinstance(mat, list) and mat != [] for mat in [m_a, m_b]):
        raise ValueError("m_a and m_b can't be empty")

    for name, mat in [("m_a", m_a), ("m_b", m_b)]:
        if not all(isinstance(row, list) for row in mat):
            raise TypeError(f"{name} must be a list of lists")
        if not all(isinstance(el, (int, float)) for row in mat for el in row):
            raise TypeError(f"{name} should contain only integers or floats")
        if not all(len(row) == len(mat[0]) for row in mat):
            raise TypeError(f"each row of {name} must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    b_t = list(zip(*m_b))
    return [[sum(a * b for a, b in zip(row_a, col_b))
            for col_b in b_t] for row_a in m_a]
