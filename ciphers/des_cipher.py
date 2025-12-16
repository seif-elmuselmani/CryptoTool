"""
DES Cipher Implementation
Uses PyCryptodome for DES encryption
"""
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

def encrypt(text, key):
    """
    Encrypt text using DES
    Args:
        text: Plain text to encrypt
        key: 16-character hexadecimal string (e.g., '0123456789ABCDEF')
    Returns:
        Encrypted text in hexadecimal
    """
    try:
        # Prepare key (DES requires 8 bytes = 16 hex characters)
        # Remove any spaces from the key
        key = key.replace(' ', '').upper()
        
        # Check if key is valid hex
        try:
            key_bytes = binascii.unhexlify(key)
        except (binascii.Error, ValueError):
            raise ValueError("Key must be a valid hexadecimal string (e.g., '0123456789ABCDEF')")
        
        # Ensure key is exactly 8 bytes
        if len(key_bytes) < 8:
            # Pad with zeros
            key_bytes = key_bytes + b'\x00' * (8 - len(key_bytes))
        elif len(key_bytes) > 8:
            # Truncate to 8 bytes
            key_bytes = key_bytes[:8]
        
        # Create cipher
        cipher = DES.new(key_bytes, DES.MODE_ECB)
        
        # Pad and encrypt
        text_bytes = text.encode('utf-8')
        padded_text = pad(text_bytes, DES.block_size)
        encrypted = cipher.encrypt(padded_text)
        
        # Return as hex string
        return binascii.hexlify(encrypted).decode('utf-8')
    
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise ValueError(f"DES encryption error: {str(e)}")


def decrypt(text, key):
    """
    Decrypt text using DES
    Args:
        text: Cipher text in hexadecimal
        key: 16-character hexadecimal string used for encryption
    Returns:
        Decrypted text
    """
    try:
        # Prepare key
        key = key.replace(' ', '').upper()
        
        # Check if key is valid hex
        try:
            key_bytes = binascii.unhexlify(key)
        except (binascii.Error, ValueError):
            raise ValueError("Key must be a valid hexadecimal string (e.g., '0123456789ABCDEF')")
        
        # Ensure key is exactly 8 bytes
        if len(key_bytes) < 8:
            key_bytes = key_bytes + b'\x00' * (8 - len(key_bytes))
        elif len(key_bytes) > 8:
            key_bytes = key_bytes[:8]
        
        # Create cipher
        cipher = DES.new(key_bytes, DES.MODE_ECB)
        
        # Decrypt
        encrypted_bytes = binascii.unhexlify(text)
        decrypted = cipher.decrypt(encrypted_bytes)
        unpadded = unpad(decrypted, DES.block_size)
        
        return unpadded.decode('utf-8')
    
    except ValueError as ve:
        raise ve
    except Exception as e:
        raise ValueError(f"DES decryption error: {str(e)}")
