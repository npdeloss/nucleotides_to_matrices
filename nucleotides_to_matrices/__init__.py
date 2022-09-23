"""Top-level package for Nucleotides To Matrices."""

__author__ = """Nathaniel Delos Santos"""
__email__ = 'Nathaniel.P.DelosSantos@jacobs.ucsd.edu'
__version__ = '0.1.0'

from .nucleotides_to_matrices import (
    sequence_to_matrix,
    matrix_to_sequence
)

from .encodings import encodings_df

__all__ = [
    'encodings_df',
    'sequence_to_matrix',
    'matrix_to_sequence'
]
