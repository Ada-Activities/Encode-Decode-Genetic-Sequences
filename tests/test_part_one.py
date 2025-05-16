from source.part_one import categorize_strand, decode_strand, encode_strand
from .test_data import DNA, DNA_ENCODED, RNA, RNA_ENCODED, STRAND_BOTH_BASES, STRAND_NEITHER_BASE

# DNA tests

def test_encode_DNA_strand():
    # Arrange
    expected = DNA_ENCODED

    # Act
    result = encode_strand(DNA)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"

def test_decode_DNA_strand():
    # Arrange
    expected = DNA

    # Act
    result = decode_strand(DNA_ENCODED)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"

def test_categorize_DNA_strand():
    # Arrange
    expected = 0

    # Act
    result = categorize_strand(DNA)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"

# RNA tests

def test_encode_RNA_strand():
    # Arrange
    expected = RNA_ENCODED

    # Act
    result = encode_strand(RNA)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"

def test_decode_RNA_strand():
    # Arrange
    expected = RNA

    # Act
    result = decode_strand(RNA_ENCODED)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"

def test_categorize_RNA_strand():
    # Arrange
    expected = 1

    # Act
    result = categorize_strand(RNA)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"

# uncategorized strand tests

def test_categorize_strand_both_bases_present():
    # Arrange
    expected = -1

    # Act
    result = categorize_strand(STRAND_BOTH_BASES)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"

def test_categorize_strand_neither_base_present():
    # Arrange
    expected = -1

    # Act
    result = categorize_strand(STRAND_NEITHER_BASE)

    # Assert
    assert result == expected, f"Expected {expected}, but got {result}"