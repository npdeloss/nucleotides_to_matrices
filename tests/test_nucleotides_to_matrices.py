#!/usr/bin/env python

"""Tests for `nucleotides_to_matrices` package."""

import pytest

from click.testing import CliRunner

from nucleotides_to_matrices import (
    encodings_df,
    sequence_to_matrix,
    matrix_to_sequence
)
from nucleotides_to_matrices import cli

import numpy as np

from .ground_truth_values import ground_truths

_encodings_df = encodings_df()
_ground_truths = ground_truths()


@pytest.fixture
def sequence():
    """Sequence fixture.
    """
    return ''.join(
        _encodings_df['Code']
    )


def test_sequence(sequence):
    """Sequence test
    """
    assert sequence == _ground_truths.sequence


@pytest.fixture
def matrix(sequence):
    """Matrix fixture
    """
    return sequence_to_matrix(sequence)


def test_matrix(matrix):
    """Matrix test
    """
    assert np.array_equiv(
        matrix,
        _ground_truths.matrix
    )


@pytest.fixture
def dna_sequence(matrix):
    """Converted DNA sequence fixture
    """
    return matrix_to_sequence(matrix)


def test_dna_sequence(dna_sequence):
    """Converted DNA sequence test
    """
    assert dna_sequence == _ground_truths.dna_sequence


@pytest.fixture
def rna_sequence(matrix):
    """Converted RNA sequence fixture
    """
    return matrix_to_sequence(matrix, type='rna')


def test_rna_sequence(rna_sequence):
    """Converted RNA sequence test
    """
    assert rna_sequence == _ground_truths.rna_sequence


@pytest.fixture
def rc_matrix(matrix):
    """Reverse complemented matrix fixture
    """
    return matrix[::-1, ::-1]


def test_rc_matrix(rc_matrix):
    """Reverse complemented matrix test
    """
    assert np.array_equiv(
        rc_matrix,
        _ground_truths.rc_matrix
    )


@pytest.fixture
def rc_dna_sequence(rc_matrix):
    """Reverse complemented DNA sequence fixture
    """
    return matrix_to_sequence(rc_matrix)


def test_rc_dna_sequence(rc_dna_sequence):
    """Reverse complemented DNA sequence test
    """
    assert rc_dna_sequence == _ground_truths.rc_dna_sequence


@pytest.fixture
def rc_rna_sequence(rc_matrix):
    """Reverse complemented RNA sequence fixture
    """
    return matrix_to_sequence(rc_matrix, type='rna')


def test_rc_rna_sequence(rc_rna_sequence):
    """Reverse complemented DNA sequence test
    """
    assert rc_rna_sequence == _ground_truths.rc_rna_sequence


def test_command_line_interface(sequence):
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main, [sequence])
    assert result.exit_code == 0
    # assert 'nucleotides_to_matrices.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help' in help_result.output
    assert 'Show this message and exit.' in help_result.output
