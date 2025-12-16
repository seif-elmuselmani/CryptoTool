"""
Permutation Cipher Implementation
Rearranges characters in fixed-size blocks based on a permutation key
"""

def encrypt(text, key):
    """
    Encrypt text using permutation cipher
    Args:
        text: Plain text to encrypt
        key: Permutation key (e.g., "3,1,4,2" for block size 4)
    Returns:
        Encrypted text (padded to complete blocks with 'X')
    """
    try:
        perm = [int(x) - 1 for x in key.replace(' ', '').split(',')]
    except ValueError:
        raise ValueError("Key must be comma-separated numbers (e.g., '3,1,4,2')")
    
    block_size = len(perm)
    
    # Validate permutation
    if sorted(perm) != list(range(block_size)):
        raise ValueError(f"Key must be a permutation of numbers 1 to {block_size}")
    
    # Pad text with 'X' to complete blocks (standard practice in cryptography)
    padding_needed = (block_size - len(text) % block_size) % block_size
    padded_text = text + 'X' * padding_needed
    
    # Apply permutation to each block
    result = []
    for i in range(0, len(padded_text), block_size):
        block = padded_text[i:i + block_size]
        permuted_block = ''.join([block[perm[j]] for j in range(block_size)])
        result.append(permuted_block)
    
    # Return complete encrypted text including padding
    return ''.join(result)


def decrypt(text, key):
    """
    Decrypt text using permutation cipher
    Args:
        text: Cipher text to decrypt
        key: Permutation key (e.g., "3,1,4,2" for block size 4)
    Returns:
        Decrypted text (with padding removed)
    """
    try:
        perm = [int(x) - 1 for x in key.replace(' ', '').split(',')]
    except ValueError:
        raise ValueError("Key must be comma-separated numbers (e.g., '3,1,4,2')")
    
    block_size = len(perm)
    
    # Validate permutation
    if sorted(perm) != list(range(block_size)):
        raise ValueError(f"Key must be a permutation of numbers 1 to {block_size}")
    
    # Create inverse permutation
    inv_perm = [0] * block_size
    for i in range(block_size):
        inv_perm[perm[i]] = i
    
    # Apply inverse permutation to each block
    result = []
    for i in range(0, len(text), block_size):
        block = text[i:i + block_size]
        unpermuted_block = ''.join([block[inv_perm[j]] for j in range(block_size)])
        result.append(unpermuted_block)
    
    # Remove padding (trailing 'X' characters)
    return ''.join(result).rstrip('X')
