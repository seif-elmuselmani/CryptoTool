"""
AES Cipher Implementation
Uses PyCryptodome for AES-256 encryption
"""
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

def encrypt(text, key):
    """
    Encrypt text using AES-256
    Args:
        text: Plain text to encrypt
        key: Key (will be hashed to 32 bytes for AES-256)
    Returns:
        Encrypted text in hexadecimal (includes IV)
    """
    try:
        # Prepare key (AES-256 requires 32 bytes)
        key_bytes = key.encode('utf-8')
        if len(key_bytes) < 32:
            key_bytes = key_bytes + b'0' * (32 - len(key_bytes))
        elif len(key_bytes) > 32:
            key_bytes = key_bytes[:32]
        
        # Generate random IV
        iv = get_random_bytes(AES.block_size)
        
        # Create cipher
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
        
        # Pad and encrypt
        text_bytes = text.encode('utf-8')
        padded_text = pad(text_bytes, AES.block_size)
        encrypted = cipher.encrypt(padded_text)
        
        # Combine IV and encrypted text
        result = iv + encrypted
        
        # Return as hex string
        return binascii.hexlify(result).decode('utf-8')
    
    except Exception as e:
        raise ValueError(f"AES encryption error: {str(e)}")


def decrypt(text, key):
    """
    Decrypt text using AES-256
    Args:
        text: Cipher text in hexadecimal (includes IV)
        key: Key used for encryption
    Returns:
        Decrypted text
    """
    try:
        # Prepare key
        key_bytes = key.encode('utf-8')
        if len(key_bytes) < 32:
            key_bytes = key_bytes + b'0' * (32 - len(key_bytes))
        elif len(key_bytes) > 32:
            key_bytes = key_bytes[:32]
        
        # Decode hex
        encrypted_data = binascii.unhexlify(text)
        
        # Extract IV and ciphertext
        iv = encrypted_data[:AES.block_size]
        ciphertext = encrypted_data[AES.block_size:]
        
        # Create cipher
        cipher = AES.new(key_bytes, AES.MODE_CBC, iv)
        
        # Decrypt
        decrypted = cipher.decrypt(ciphertext)
        unpadded = unpad(decrypted, AES.block_size)
        
        return unpadded.decode('utf-8')
    
    except Exception as e:
        raise ValueError(f"AES decryption error: {str(e)}")
