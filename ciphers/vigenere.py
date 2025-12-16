"""
Vigenère Cipher Implementation
Polyalphabetic substitution using a keyword
"""

def encrypt(text, key):
    """
    Encrypt text using Vigenère cipher
    Args:
        text: Plain text to encrypt
        key: Keyword for encryption
    Returns:
        Encrypted text
    """
    if not key:
        raise ValueError("Key cannot be empty for Vigenère cipher")
    
    key = key.upper()
    if not all(c.isalpha() for c in key):
        raise ValueError("Key must contain only letters")
    
    result = []
    key_index = 0
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            # Get shift from key
            shift = ord(key[key_index % len(key)]) - 65
            # Encrypt character
            encrypted = (ord(char) - ascii_offset + shift) % 26
            result.append(chr(encrypted + ascii_offset))
            key_index += 1
        else:
            result.append(char)
    
    return ''.join(result)


def decrypt(text, key):
    """
    Decrypt text using Vigenère cipher
    Args:
        text: Cipher text to decrypt
        key: Keyword for decryption
    Returns:
        Decrypted text
    """
    if not key:
        raise ValueError("Key cannot be empty for Vigenère cipher")
    
    key = key.upper()
    if not all(c.isalpha() for c in key):
        raise ValueError("Key must contain only letters")
    
    result = []
    key_index = 0
    
    for char in text:
        if char.isalpha():
            # Determine if uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            # Get shift from key
            shift = ord(key[key_index % len(key)]) - 65
            # Decrypt character
            decrypted = (ord(char) - ascii_offset - shift) % 26
            result.append(chr(decrypted + ascii_offset))
            key_index += 1
        else:
            result.append(char)
    
    return ''.join(result)
