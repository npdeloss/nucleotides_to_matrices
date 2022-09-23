"""Console script for nucleotides_to_matrices."""
import sys
import click

from .nucleotides_to_matrices import (
    sequence_to_matrix
)


@click.command()
@click.argument(
    'sequence'
)
@click.option(
    '--transpose',
    'transpose',
    flag_value=False,
    default=True,
    help=(
        'Whether or not to transpose the output'
    )
)
def main(
    sequence,
    transpose=False
):
    """This script converts SEQUENCE into a matrix."""

    _matrix = sequence_to_matrix(sequence)
    matrix = _matrix.T if transpose else _matrix
    del _matrix

    for row in matrix:
        print('\t'.join([str(col) for col in row]))

    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
