# anonymity.py

import time
import random


def simulate_human_behavior(browser):
    time.sleep(random.uniform(2, 5))
    try:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    except Exception:
        # If scrolling fails (e.g., headless driver without page), ignore
        pass
    time.sleep(random.uniform(1, 3))
    