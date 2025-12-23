# purchase_automation.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from proxy_manager import get_proxy
from card_manager import get_card_detail, decrypt_card_detail, upload_card_details
from error_handling import handle_captcha
from payment_processing import process_payment
from anonymity import simulate_human_behavior


def automate_purchase(card_details):
    browser = webdriver.Chrome()
    try:
        # Get a proxy if available (not applied automatically here)
        _proxy = get_proxy()

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
                element.send_keys(card_detail.get('shipping_address', ''))

            billing_info_elements = browser.find_elements(By.CLASS_NAME, 'billing_info')
            for element in billing_info_elements:
                element.send_keys(card_detail.get('billing_address', ''))

            # Process payment
            process_payment(browser, card_detail)
    finally:
        try:
            browser.quit()
        except Exception:
            pass
