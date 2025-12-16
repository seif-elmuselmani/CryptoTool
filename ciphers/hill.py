"""
Hill Cipher Implementation
Matrix-based encryption using linear algebra
"""
import numpy as np
import string

def _text_to_numbers(text):
    """Convert text to numbers (A=0, B=1, ...)"""
    text = text.upper()
    return [ord(c) - 65 for c in text if c in string.ascii_uppercase]


def _numbers_to_text(numbers):
    """Convert numbers to text"""
    return ''.join([chr(n % 26 + 65) for n in numbers])


def _mod_inverse(a, m):
    """Find modular inverse of a under modulo m"""
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def _matrix_mod_inverse(matrix, modulus):
    """Find modular inverse of matrix"""
    det = int(round(np.linalg.det(matrix)))
    det = det % modulus
    
    det_inv = _mod_inverse(det, modulus)
    if det_inv is None:
        raise ValueError("Matrix is not invertible under mod 26")
    
    matrix_inv = np.round(det * np.linalg.inv(matrix)).astype(int)
    matrix_inv = (matrix_inv * det_inv) % modulus
    
    return matrix_inv


def _parse_key_matrix(key, size):
    """Parse key string into matrix"""
    try:
        # Try to parse as comma/space separated numbers
        numbers = []
        for part in key.replace(',', ' ').split():
            numbers.append(int(part))
        
        if len(numbers) != size * size:
            raise ValueError(f"Key must contain exactly {size*size} numbers for {size}x{size} matrix")
        
        matrix = np.array(numbers).reshape(size, size)
        return matrix
    except ValueError as e:
        raise ValueError(f"Invalid key format: {str(e)}")


def encrypt(text, key):
    """
    Encrypt text using Hill cipher
    Args:
        text: Plain text to encrypt
        key: Matrix key as string "a,b,c,d" for 2x2 or "a,b,c,d,e,f,g,h,i" for 3x3
    Returns:
        Encrypted text
    """
    # Determine matrix size (default to 2x2)
    key_parts = len(key.replace(',', ' ').split())
    if key_parts == 4:
        size = 2
    elif key_parts == 9:
        size = 3
    else:
        raise ValueError("Key must be for 2x2 (4 numbers) or 3x3 (9 numbers) matrix")
    
    key_matrix = _parse_key_matrix(key, size)
    
    # Convert text to numbers
    numbers = _text_to_numbers(text)
    
    # Pad if necessary
    while len(numbers) % size != 0:
        numbers.append(23)  # Pad with 'X'
    
    # Encrypt in blocks
    result = []
    for i in range(0, len(numbers), size):
        block = np.array(numbers[i:i+size])
        encrypted_block = np.dot(key_matrix, block) % 26
        result.extend(encrypted_block)
    
    return _numbers_to_text(result)


def decrypt(text, key):
    """
    Decrypt text using Hill cipher
    Args:
        text: Cipher text to decrypt
        key: Matrix key as string "a,b,c,d" for 2x2 or "a,b,c,d,e,f,g,h,i" for 3x3
    Returns:
        Decrypted text
    """
    # Determine matrix size
    key_parts = len(key.replace(',', ' ').split())
    if key_parts == 4:
        size = 2
    elif key_parts == 9:
        size = 3
    else:
        raise ValueError("Key must be for 2x2 (4 numbers) or 3x3 (9 numbers) matrix")
    
    key_matrix = _parse_key_matrix(key, size)
    
    # Calculate inverse matrix
    try:
        key_matrix_inv = _matrix_mod_inverse(key_matrix, 26)
    except ValueError as e:
        raise ValueError(f"Cannot decrypt: {str(e)}")
    
    # Convert text to numbers
    numbers = _text_to_numbers(text)
    
    # Decrypt in blocks
    result = []
    for i in range(0, len(numbers), size):
        block = np.array(numbers[i:i+size])
        decrypted_block = np.dot(key_matrix_inv, block) % 26
        result.extend(decrypted_block)
    
    return _numbers_to_text(result)
