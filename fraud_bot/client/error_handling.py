# error_handling.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from captcha_solver import solve_captcha


def handle_captcha(browser):
        try:
                captcha_element = browser.find_element(By.ID, 'captcha_image')
        except Exception:
                return

        if captcha_element:
                captcha_image = captcha_element.screenshot_as_png
                solution = solve_captcha(captcha_image)
                captcha_input = browser.find_element(By.ID, 'captcha_input')
                captcha_input.send_keys(solution)
                