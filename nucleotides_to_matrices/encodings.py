"""Path, data, and lookup dictionaries for IUPAC code vector encodings"""

import pandas as pd
from os.path import dirname, join, normpath

_encodings_filepath = normpath(join(
    dirname(__file__),
    'encodings.txt'
))

_encodings_df = pd.read_csv(_encodings_filepath, sep='\t')


def encodings_df():
    """Data for encodings
    """
    return _encodings_df


_nucleotide_to_vector = (
    _encodings_df
    .set_index('Code')
    [list(
        'ACGT'
    )]
    .apply(
        tuple,
        axis=1
    )
    .to_dict()
)


def nucleotide_to_vector(nucleotide):
    """Nucleotide code to vector encoding lookup
    """
    return _nucleotide_to_vector


_dna_codes = set(
    _encodings_df[
        _encodings_df['DNA']
    ]
    .drop_duplicates(
        list('ACGT')
    )
    ['Code']
)


def dna_codes():
    """Set of codes for DNA
    """
    return _dna_codes


_rna_codes = set(
    _encodings_df[
        _encodings_df['RNA']
    ]
    .drop_duplicates(
        list('ACGT')
    )
    ['Code']
)


def rna_codes():
    """Set of codes for RNA
    """
    return _dna_codes


_strict_codes = set(
    _encodings_df[
        (~_encodings_df['Degenerate'])
        & (~_encodings_df['Special'])
    ]
    ['Code']
)


def strict_codes():
    """Set of strict codes
    """
    return _strict_codes


_vector_to_dna = {
    vector: nucleotide
    for nucleotide, vector
    in _nucleotide_to_vector.items()
    if nucleotide in _dna_codes
}


def vector_to_dna():
    """Vector encoding to DNA code lookup
    """
    return _vector_to_dna


_vector_to_rna = {
    vector: nucleotide
    for nucleotide, vector
    in _nucleotide_to_vector.items()
    if nucleotide in _rna_codes
}


def vector_to_rna():
    """Vector encoding to RNA code lookup
    """
    return _vector_to_rna
