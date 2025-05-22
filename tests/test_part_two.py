from source.part_two import categorize_strand
from .test_data import DNA_ENCODED, RNA_ENCODED, ENCODED_BOTH_BASES, ENCODED_NEITHER_BASE

def test_encoded_categorize_strand_DNA():
    # Arrange
    expected = 0

    # Act
    result = categorize_strand(DNA_ENCODED)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"

def test_encoded_categorize_strand_RNA():
    # Arrange
    expected = 1

    # Act
    result = categorize_strand(RNA_ENCODED)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"

def test_encoded_categorize_strand_both_bases():
    # Arrange
    expected = -1

    # Act
    result = categorize_strand(ENCODED_BOTH_BASES)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"

def test_encoded_categorize_strand_neither_base():
    # Arrange
    expected = -1

    # Act
    result = categorize_strand(ENCODED_NEITHER_BASE)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"