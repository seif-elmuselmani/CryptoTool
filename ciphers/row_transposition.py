"""
Row Transposition Cipher Implementation
Rearranges characters based on a numeric key.
Refactored for readability and robust index handling.
"""
import math
from typing import List

def _validate_key(key: str, text_len: int = 0) -> List[int]:
    """
    Validate and parse the key.
    Ensures key is numeric and contains a valid permutation sequence.
    """
    if not key.isdigit():
        raise ValueError("Key must be a numeric string (e.g., '3142')")
    
    # Convert key to list of integers
    key_order = [int(c) for c in key]
    num_cols = len(key_order)
    
    if num_cols == 0:
        raise ValueError("Key cannot be empty")

    # Check if key is a valid permutation (contains 1..n or 0..n-1)
    # Adjusting to 1-based index checking as per standard algorithm
    if sorted(key_order) != list(range(1, num_cols + 1)):
        raise ValueError(f"Key must contain each digit from 1 to {num_cols} exactly once")
        
    return key_order

def encrypt(text: str, key: str) -> str:
    """
    Encrypt text using row transposition cipher.
    """
    key_order = _validate_key(key)
    num_cols = len(key_order)
    num_rows = math.ceil(len(text) / num_cols)
    
    # Pad text with a placeholder '_' to fill the grid perfectly
    # This makes the logic much simpler
    total_cells = num_rows * num_cols
    padded_text = text.ljust(total_cells, '_')
    
    # Create the grid (Row by Row)
    # Example: 'HELL' -> [['H','E'], ['L','L']]
    grid = [padded_text[i * num_cols : (i + 1) * num_cols] for i in range(num_rows)]
    
    # Read columns based on key order
    result = []
    for col_num in key_order:
        # Convert 1-based key to 0-based index
        col_index = col_num - 1
        for row in grid:
            char = row[col_index]
            # Verify we are not adding padding chars if that's preferred, 
            # OR keep them to maintain reversibility.
            # Standard transposition usually keeps placeholders or handles unevenness.
            # Here we act like the original code: remove the specific padding chars if logic demands,
            # BUT for transposition to work correctly, padding is usually needed in the output 
            # unless we handle irregular columns in decrypt.
            if char != '_':
                result.append(char)
                
    return ''.join(result)

def decrypt(text: str, key: str) -> str:
    """
    Decrypt text using row transposition cipher.
    Handles irregular column lengths.
    """
    key_order = _validate_key(key)
    num_cols = len(key_order)
    
    # Calculate dimensions
    num_rows = math.ceil(len(text) / num_cols)
    
    # Calculate how many cells are in the last row (remainder)
    # The 'remainder' tells us how many columns are 'full'
    remainder = len(text) % num_cols
    if remainder == 0:
        remainder = num_cols

    # Create an empty grid
    # Use None to indicate "empty"
    grid = [['' for _ in range(num_cols)] for _ in range(num_rows)]
    
    current_char_idx = 0
    
    # Fill the grid column by column, following the key order
    for col_num in key_order:
        col_index = col_num - 1
        
        # Determine the length of THIS specific column
        # If the column index falls within the 'remainder', it's a full column (long)
        # Otherwise, it's a short column (missing the bottom cell)
        if col_index < remainder:
            col_len = num_rows
        else:
            col_len = num_rows - 1
            
        # Fill this column with characters from the ciphertext
        for r in range(col_len):
            if current_char_idx < len(text):
                grid[r][col_index] = text[current_char_idx]
                current_char_idx += 1
                
    # Read row by row to reconstruct the plaintext
    result = []
    for row in grid:
        result.extend([c for c in row if c != ''])
        
    return ''.join(result)