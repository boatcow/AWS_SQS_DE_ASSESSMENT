"""
This module provides utilities to encode and decode data using base64 encoding.
Note: Base64 is used for encoding and not encryption. It does not provide any security.

Functions:
    - encrypt(data): Returns base64 encoded string of the input data.
    - decrypt(data): Decodes a base64 encoded string.
"""
import base64

def encrypt(data):
    """
    Encrypts the given data using base64 encoding.
    
    Input:
        data: A value (can be of any type). It will be converted to a string before encoding.
        
    Output:
        Returns the base64 encoded string of the input data.
    """
    encoded_bytes = str(data).encode()
    encoded_id = base64.b64encode(encoded_bytes).decode()
    return encoded_id

def decrypt(data):
    """
    Decrypts the given base64 encoded data.
    
    Input:
        data: A base64 encoded string.
        
    Output:
        Returns the decoded string from the input data.
    """
    decoded_bytes = base64.b64decode(data)
    return decoded_bytes.decode()
