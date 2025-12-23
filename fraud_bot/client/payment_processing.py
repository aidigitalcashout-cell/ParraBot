# payment_processing.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import importlib.util
import os


def process_payment(browser, card_detail):
    card_number_element = browser.find_element(By.ID, 'card_number')
    card_number_element.send_keys(card_detail['card_number'])

    expiry_date_element = browser.find_element(By.ID, 'expiry_date')
    expiry_date_element.send_keys(card_detail['expiry_date'])

    cvv_element = browser.find_element(By.ID, 'cvv')
    cvv_element.send_keys(card_detail['cvv'])

    # Bypass 3D Secure authentication using module loaded by filename
    bypass_path = os.path.join(os.path.dirname(__file__), '3d_secure_bypass.py')
    if os.path.exists(bypass_path):
        spec = importlib.util.spec_from_file_location('secure3d', bypass_path)
        bypass_mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(bypass_mod)
        bypass_mod.bypass_3d_secure(browser, card_detail.get('3d_secure_data'))

    pay_now_element = browser.find_element(By.ID, 'pay_now_button')
    pay_now_element.click()
    