import base64

def encrypt(data):
    encoded_bytes = str(data).encode()
    encoded_id = base64.b64encode(encoded_bytes).decode()
    return encoded_id

def decrypt(data):
    decoded_bytes = base64.b64decode(data)
    return decoded_bytes.decode()
