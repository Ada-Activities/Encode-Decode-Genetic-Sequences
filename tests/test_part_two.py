from source.part_two import categorize_strand as categorize_encoded_strand
from .test_data import DNA_ENCODED, RNA_ENCODED, ENCODED_BOTH_BASES, ENCODED_NEITHER_BASE

def test_categorize_encoded_strand_DNA():
    # Arrange
    expected = 0

    # Act
    result = categorize_encoded_strand(DNA_ENCODED)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"

def test_categorize_encoded_strand_RNA():
    # Arrange
    expected = 1

    # Act
    result = categorize_encoded_strand(RNA_ENCODED)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"

def test_categorize_encoded_strand_both_bases():
    # Arrange
    expected = -1

    # Act
    result = categorize_encoded_strand(ENCODED_BOTH_BASES)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"

def test_categorize_encoded_strand_neither_base():
    # Arrange
    expected = -1

    # Act
    result = categorize_encoded_strand(ENCODED_NEITHER_BASE)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"