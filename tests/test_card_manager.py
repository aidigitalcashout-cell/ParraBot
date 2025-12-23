import os
import csv
import tempfile
from fraud_bot.client.card_manager import upload_card_details, decrypt_card_detail, get_card_detail


def test_get_card_detail_decrypt():
    encrypted = get_card_detail()
    assert encrypted is not None
    card = decrypt_card_detail(encrypted)
    assert isinstance(card, dict)
    assert 'card_number' in card


def test_upload_card_details_and_decrypt(tmp_path):
    csv_path = tmp_path / "cards.csv"
    headers = ['card_number', 'expiry_date', 'cvv', 'shipping_address', 'billing_address', '3d_secure_data']
    rows = [
        ['4111111111111111', '12/25', '123', 'Addr1', 'Addr1', 'secure1'],
        ['4222222222222', '11/24', '321', 'Addr2', 'Addr2', 'secure2'],
    ]

    with open(csv_path, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    card_list = upload_card_details(str(csv_path))
    assert isinstance(card_list, list)
    assert len(card_list) == 2

    # decrypt first entry
    card = decrypt_card_detail(card_list[0])
    # Card numbers may be read as int by pandas; compare as string
    assert str(card['card_number']) == '4111111111111111'
