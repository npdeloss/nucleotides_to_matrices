"""Main module."""

import numpy as np
from numpy import ndarray

from .encodings import (
    nucleotide_to_vector,
    vector_to_dna,
    vector_to_rna
)


_nucleotide_to_vector = nucleotide_to_vector()
_vector_to_dna = vector_to_dna()
_vector_to_rna = vector_to_rna()


def sequence_to_matrix(
    sequence: str
) -> ndarray:
    """
    Convert a string of nucleotide codes into a matrix.

    Parameters
    ----------
    sequence : str
        String representing the nucleotides to convert.

    Returns
    -------
    matrix : numpy.ndarray
        The converted string of nucleotide codes as a matrix of integers.


    See Also
    --------
    matrix_to_sequence : Converts a matrix into a string of nucleotide codes.

    Examples
    --------
    >>> import nucleotides_to_matrices as n2m
    >>> example_dna_sequence = 'GATTACAN'
    >>> n2m.sequence_to_matrix(example_dna_sequence)
    array([[0, 0, 1, 0],
           [1, 0, 0, 0],
           [0, 0, 0, 1],
           [0, 0, 0, 1],
           [1, 0, 0, 0],
           [0, 1, 0, 0],
           [1, 0, 0, 0],
           [1, 1, 1, 1]])
    >>> example_rna_sequence = 'GAUUACIN'
    >>> n2m.sequence_to_matrix(example_rna_sequence)
    array([[0, 0, 1, 0],
           [1, 0, 0, 0],
           [0, 0, 0, 1],
           [0, 0, 0, 1],
           [1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 1, 0],
           [1, 1, 1, 1]])
    """
    return np.stack([
        np.array(_nucleotide_to_vector[nuc])
        if nuc
        in _nucleotide_to_vector.keys()
        else _nucleotide_to_vector['N']
        for nuc
        in sequence
    ])


def matrix_to_sequence(
    matrix: ndarray,
    type: str = 'dna'
) -> str:
    """
    Convert a matrix of encoded nucleotides into a string.

    Parameters
    ----------
    matrix : numpy.ndarray
        Matrix of encoded nucleotides to convert.
    type: {'dna', 'rna'}, default 'dna'
        The type of nucleotides to convert to. May be either 'dna' or 'rna'.

    Returns
    -------
    sequence : string
        The converted matrix as a string of nucleotide codes.


    See Also
    --------
    sequence_to_matrix : Convert a string of nucleotide codes into a matrix.

    Examples
    --------
    >>> example_dna_sequence = 'GATTACAN'
        >>> dna_matrix = n2m.sequence_to_matrix(example_dna_sequence)
    >>> dna_matrix
    >>> array([[0, 0, 1, 0],
               [1, 0, 0, 0],
               [0, 0, 0, 1],
               [0, 0, 0, 1],
               [1, 0, 0, 0],
               [0, 1, 0, 0],
               [1, 0, 0, 0],
               [1, 1, 1, 1]])
        >>> dna_sequence = n2m.matrix_to_sequence(dna_matrix)
    >>> dna_sequence
    'GATTACAN'
    >>> example_rna_sequence = 'GAUUACIN'
    >>> rna_matrix = n2m.sequence_to_matrix(example_rna_sequence)
    >>> rna_matrix
    >>> array([[0, 0, 1, 0],
               [1, 0, 0, 0],
               [0, 0, 0, 1],
               [0, 0, 0, 1],
               [1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [1, 1, 1, 1]])
    >>> rna_sequence = n2m.matrix_to_sequence(rna_matrix, type = 'rna')
    >>> rna_sequence
    'GAUUACGN'
    """
    if type.lower() == 'rna':
        lu = _vector_to_rna
    else:
        lu = _vector_to_dna
    return ''.join([
        lu[tuple(vector)]
        for vector
        in matrix.tolist()
    ])
