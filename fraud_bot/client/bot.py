# bot.py

from flask import Flask, request, jsonify
import threading
import os


app = Flask(__name__)


def automate_purchase(card_details):
    # Import heavy or environment-specific modules lazily to avoid import-time side effects
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from proxy_manager import get_proxy
    from card_manager import decrypt_card_detail
    from error_handling import handle_captcha
    from payment_processing import process_payment
    from anonymity import simulate_human_behavior

    # Initialize browser (caller is responsible for environment and webdriver availability)
    browser = webdriver.Chrome()
    proxy = get_proxy()
    # Note: applying proxy to an existing webdriver instance requires using options when creating the driver.

    for encrypted_card_detail in card_details:
        card_detail = decrypt_card_detail(encrypted_card_detail)
        if not card_detail:
            continue

        # Simulate human behavior
        simulate_human_behavior(browser)

        # Navigate to target website
        browser.get('https://example-retailer.com')

        # Handle CAPTCHA if present
        handle_captcha(browser)

        # Select product and add to cart
        product_element = browser.find_element(By.ID, 'product_id')
        product_element.click()
        add_to_cart_element = browser.find_element(By.ID, 'add_to_cart_button')
        add_to_cart_element.click()

        # Proceed to checkout
        checkout_element = browser.find_element(By.ID, 'checkout_button')
        checkout_element.click()

        # Enter shipping and billing information
        shipping_info_elements = browser.find_elements(By.CLASS_NAME, 'shipping_info')
        for element in shipping_info_elements:
            element.send_keys(card_detail['shipping_address'])

        billing_info_elements = browser.find_elements(By.CLASS_NAME, 'billing_info')
        for element in billing_info_elements:
            element.send_keys(card_detail['billing_address'])

        # Process payment
        process_payment(browser, card_detail)

    browser.quit()


@app.route('/automate', methods=['POST'])
def automate():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Ensure uploads directory exists
    os.makedirs('./uploads', exist_ok=True)

    # Save uploaded file
    file_path = f'./uploads/{file.filename}'
    file.save(file_path)

    # Import upload helper lazily
    from card_manager import upload_card_details

    card_details = upload_card_details(file_path)
    bot_thread = threading.Thread(target=automate_purchase, args=(card_details,))
    bot_thread.start()

    return jsonify({'message': 'Bot started', 'card_count': len(card_details)}), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
