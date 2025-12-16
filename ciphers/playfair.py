"""
Playfair Cipher Implementation
Uses a 5x5 matrix of letters for digraph substitution
"""
import string

def _create_playfair_matrix(key):
    """Create 5x5 Playfair matrix from key"""
    key = key.upper().replace('J', 'I')
    key = ''.join(dict.fromkeys(key))  # Remove duplicates
    
    # Remove non-alphabetic characters
    key = ''.join([c for c in key if c in string.ascii_uppercase])
    
    # Add remaining letters
    alphabet = string.ascii_uppercase.replace('J', '')
    for char in alphabet:
        if char not in key:
            key += char
    
    # Create 5x5 matrix
    matrix = []
    for i in range(5):
        matrix.append(list(key[i*5:(i+1)*5]))
    
    return matrix


def _find_position(matrix, char):
    """Find row and column of character in matrix"""
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None, None


def _prepare_text(text):
    """Prepare text for Playfair encryption"""
    text = text.upper().replace('J', 'I')
    text = ''.join([c for c in text if c in string.ascii_uppercase])
    
    # Insert X between duplicate letters
    prepared = []
    i = 0
    while i < len(text):
        prepared.append(text[i])
        if i + 1 < len(text):
            if text[i] == text[i + 1]:
                prepared.append('X')
            else:
                prepared.append(text[i + 1])
                i += 1
        i += 1
    
    # Add X if odd length
    if len(prepared) % 2 != 0:
        prepared.append('X')
    
    return ''.join(prepared)


def encrypt(text, key):
    """
    Encrypt text using Playfair cipher
    Args:
        text: Plain text to encrypt
        key: Keyword for generating the matrix
    Returns:
        Encrypted text
    """
    if not key:
        raise ValueError("Key cannot be empty for Playfair cipher")
    
    matrix = _create_playfair_matrix(key)
    prepared_text = _prepare_text(text)
    
    result = []
    for i in range(0, len(prepared_text), 2):
        char1, char2 = prepared_text[i], prepared_text[i + 1]
        row1, col1 = _find_position(matrix, char1)
        row2, col2 = _find_position(matrix, char2)
        
        if row1 == row2:  # Same row
            result.append(matrix[row1][(col1 + 1) % 5])
            result.append(matrix[row2][(col2 + 1) % 5])
        elif col1 == col2:  # Same column
            result.append(matrix[(row1 + 1) % 5][col1])
            result.append(matrix[(row2 + 1) % 5][col2])
        else:  # Rectangle
            result.append(matrix[row1][col2])
            result.append(matrix[row2][col1])
    
    return ''.join(result)


def decrypt(text, key):
    """
    Decrypt text using Playfair cipher
    Args:
        text: Cipher text to decrypt
        key: Keyword for generating the matrix
    Returns:
        Decrypted text
    """
    if not key:
        raise ValueError("Key cannot be empty for Playfair cipher")
    
    matrix = _create_playfair_matrix(key)
    text = text.upper().replace('J', 'I')
    text = ''.join([c for c in text if c in string.ascii_uppercase])
    
    result = []
    for i in range(0, len(text), 2):
        if i + 1 >= len(text):
            break
        char1, char2 = text[i], text[i + 1]
        row1, col1 = _find_position(matrix, char1)
        row2, col2 = _find_position(matrix, char2)
        
        if row1 == row2:  # Same row
            result.append(matrix[row1][(col1 - 1) % 5])
            result.append(matrix[row2][(col2 - 1) % 5])
        elif col1 == col2:  # Same column
            result.append(matrix[(row1 - 1) % 5][col1])
            result.append(matrix[(row2 - 1) % 5][col2])
        else:  # Rectangle
            result.append(matrix[row1][col2])
            result.append(matrix[row2][col1])
    
    return ''.join(result)
