"""
Monoalphabetic Substitution Cipher Implementation
Maps each letter to another letter using a substitution key
"""
import string

def encrypt(text, key):
    """
    Encrypt text using monoalphabetic substitution cipher
    Args:
        text: Plain text to encrypt
        key: 26-character substitution alphabet
    Returns:
        Encrypted text
    """
    if len(key) != 26:
        raise ValueError("Key must be exactly 26 characters (one for each letter)")
    
    # Create translation table
    alphabet = string.ascii_uppercase
    key = key.upper()
    
    # Check if key contains all unique letters
    if len(set(key)) != 26 or not all(c in alphabet for c in key):
        raise ValueError("Key must contain all 26 unique letters")
    
    trans_table = str.maketrans(alphabet + alphabet.lower(), 
                                key + key.lower())
    
    return text.translate(trans_table)


def decrypt(text, key):
    """
    Decrypt text using monoalphabetic substitution cipher
    Args:
        text: Cipher text to decrypt
        key: 26-character substitution alphabet
    Returns:
        Decrypted text
    """
    if len(key) != 26:
        raise ValueError("Key must be exactly 26 characters (one for each letter)")
    
    # Create reverse translation table
    alphabet = string.ascii_uppercase
    key = key.upper()
    
    # Check if key contains all unique letters
    if len(set(key)) != 26 or not all(c in alphabet for c in key):
        raise ValueError("Key must contain all 26 unique letters")
    
    # Reverse the mapping for decryption
    trans_table = str.maketrans(key + key.lower(), 
                                alphabet + alphabet.lower())
    
    return text.translate(trans_table)
