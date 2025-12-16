"""
One-Time Pad (OTP) Cipher Implementation
Dual-mode encryption supporting letters (A-Z) and XOR (bytes) modes.
"""

import base64


def _normalize_text_letters(text):
    """
    Normalize text to uppercase letters A-Z only.
    
    Args:
        text: Input text
        
    Returns:
        Normalized text containing only A-Z letters
    """
    return ''.join(filter(str.isalpha, text)).upper()


def encrypt(text, key, mode='letters', fmt='hex'):
    """
    Encrypt text using One-Time Pad in either letters or XOR mode.
    
    Args:
        text: Plain text to encrypt
        key: Encryption key (string for letters mode, string or bytes for XOR mode)
        mode: 'letters' for A-Z modulo-26 addition, 'xor' for byte XOR
        fmt: Output format for XOR mode ('hex' or 'base64')
        
    Returns:
        Encrypted text (letters for letters mode, hex/base64 for XOR mode)
        
    Raises:
        ValueError: For invalid inputs or key length mismatches
    """
    if mode == 'letters':
        # Letters mode: modulo-26 addition
        normalized_text = _normalize_text_letters(text)
        
        # Ensure key is uppercase letters only and matches text length
        normalized_key = _normalize_text_letters(key)
        
        if len(normalized_key) != len(normalized_text):
            raise ValueError(f"Key length ({len(normalized_key)}) must equal plaintext length ({len(normalized_text)}) for letters mode")
        
        # Perform modulo-26 addition
        result = []
        for i in range(len(normalized_text)):
            text_char = ord(normalized_text[i]) - ord('A')
            key_char = ord(normalized_key[i]) - ord('A')
            encrypted_char = (text_char + key_char) % 26
            result.append(chr(encrypted_char + ord('A')))
        
        return ''.join(result)
    
    elif mode == 'xor':
        # XOR mode: byte-wise XOR
        text_bytes = text.encode('utf-8')
        
        # Convert key to bytes if it's a string
        if isinstance(key, str):
            key_bytes = key.encode('utf-8')
        else:
            key_bytes = key
            
        if len(key_bytes) != len(text_bytes):
            raise ValueError(f"Key length ({len(key_bytes)} bytes) must equal plaintext length ({len(text_bytes)} bytes) for XOR mode")
        
        # Perform XOR operation
        result_bytes = bytes([text_bytes[i] ^ key_bytes[i] for i in range(len(text_bytes))])
        
        # Return in specified format
        if fmt == 'hex':
            return result_bytes.hex()
        elif fmt == 'base64':
            return base64.b64encode(result_bytes).decode('ascii')
        else:
            raise ValueError("Format must be 'hex' or 'base64'")
    
    else:
        raise ValueError("Mode must be 'letters' or 'xor'")


def decrypt(text, key, mode='letters', fmt='hex'):
    """
    Decrypt text using One-Time Pad in either letters or XOR mode.
    
    Args:
        text: Cipher text to decrypt
        key: Decryption key (string for letters mode, string or bytes for XOR mode)
        mode: 'letters' for A-Z modulo-26 subtraction, 'xor' for byte XOR
        fmt: Input format for XOR mode ('hex' or 'base64')
        
    Returns:
        Decrypted text
        
    Raises:
        ValueError: For invalid inputs or key length mismatches
    """
    if mode == 'letters':
        # Letters mode: modulo-26 subtraction
        # Ensure key is uppercase letters only and matches text length
        normalized_key = _normalize_text_letters(key)
        
        if len(normalized_key) != len(text):
            raise ValueError(f"Key length ({len(normalized_key)}) must equal ciphertext length ({len(text)}) for letters mode")
        
        # Perform modulo-26 subtraction
        result = []
        for i in range(len(text)):
            if not text[i].isalpha():
                raise ValueError("Ciphertext must contain only letters A-Z for letters mode")
                
            text_char = ord(text[i].upper()) - ord('A')
            key_char = ord(normalized_key[i]) - ord('A')
            decrypted_char = (text_char - key_char) % 26
            result.append(chr(decrypted_char + ord('A')))
        
        return ''.join(result)
    
    elif mode == 'xor':
        # XOR mode: byte-wise XOR (same as encryption)
        # Convert text from specified format to bytes
        if fmt == 'hex':
            try:
                text_bytes = bytes.fromhex(text)
            except ValueError:
                raise ValueError("Invalid hex format for ciphertext")
        elif fmt == 'base64':
            try:
                text_bytes = base64.b64decode(text)
            except Exception:
                raise ValueError("Invalid base64 format for ciphertext")
        else:
            raise ValueError("Format must be 'hex' or 'base64'")
        
        # Convert key to bytes if it's a string
        if isinstance(key, str):
            key_bytes = key.encode('utf-8')
        else:
            key_bytes = key
            
        if len(key_bytes) != len(text_bytes):
            raise ValueError(f"Key length ({len(key_bytes)} bytes) must equal ciphertext length ({len(text_bytes)} bytes) for XOR mode")
        
        # Perform XOR operation (same as encryption)
        result_bytes = bytes([text_bytes[i] ^ key_bytes[i] for i in range(len(text_bytes))])
        
        # Convert back to string
        return result_bytes.decode('utf-8')
    
    else:
        raise ValueError("Mode must be 'letters' or 'xor'")