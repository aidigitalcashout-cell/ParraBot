# card_manager.py

from cryptography.fernet import Fernet
import pandas as pd

# Load encryption key
with open('encryption_key.key', 'rb') as file:
    encryption_key = file.read()

cipher_suite = Fernet(encryption_key)


def get_card_detail():
    # For simplicity, return a hardcoded card detail
    card_detail = {
        'card_number': '1234567890123456',
        'expiry_date': '12/25',
        'cvv': '123',
        'shipping_address': '123 Fake Street, Fake City, FA 12345',
        'billing_address': '123 Fake Street, Fake City, FA 12345',
        '3d_secure_data': 'secure_data_here'
    }
    encrypted_data = cipher_suite.encrypt(str(card_detail).encode())
    return encrypted_data


def decrypt_card_detail(encrypted_data):
    decrypted_data = cipher_suite.decrypt(encrypted_data).decode()
    return eval(decrypted_data)  # Convert string representation of dict back to dict


def upload_card_details(file_path):
    df = pd.read_csv(file_path)
    card_details = []
    for _, row in df.iterrows():
        card_detail = {
            'card_number': row['card_number'],
            'expiry_date': row['expiry_date'],
            'cvv': row['cvv'],
            'shipping_address': row['shipping_address'],
            'billing_address': row['billing_address'],
            '3d_secure_data': row['3d_secure_data']
        }
        encrypted_data = cipher_suite.encrypt(str(card_detail).encode())
        card_details.append(encrypted_data)
    return card_details
