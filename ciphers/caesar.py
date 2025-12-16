"""
Caesar Cipher Implementation
Shifts each letter by a fixed number of positions in the alphabet
"""

def encrypt(text, key):
    """
    Encrypt text using Caesar cipher
    Args:
        text: Plain text to encrypt
        key: Shift value (should be a number)
    Returns:
        Encrypted text
    """
    try:
        shift = int(key)
    except ValueError:
        raise ValueError("Key must be a number for Caesar cipher")
    
    result = []
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            # Shift character
            shifted = (ord(char) - ascii_offset + shift) % 26
            result.append(chr(shifted + ascii_offset))
        else:
            result.append(char)
    
    return ''.join(result)


def decrypt(text, key):
    """
    Decrypt text using Caesar cipher
    Args:
        text: Cipher text to decrypt
        key: Shift value (should be a number)
    Returns:
        Decrypted text
    """
    try:
        shift = int(key)
    except ValueError:
        raise ValueError("Key must be a number for Caesar cipher")
    
    # Decryption is just encryption with negative shift
    return encrypt(text, -shift)
