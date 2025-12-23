# captcha_solver.py

try:
    from fraud_bot.client.config import CAPTCHA_API_KEY
except Exception:
    from config import CAPTCHA_API_KEY


def solve_captcha(captcha_image):
    import requests

    response = requests.post(
        'https://2captcha.com/in.php',
        data={
            'key': CAPTCHA_API_KEY,
            'method': 'base64',
            'body': captcha_image
        }
    )

    captcha_id = response.text.split('|')[1]
    result = requests.get(f'https://2captcha.com/res.php?key={CAPTCHA_API_KEY}&action=get&id={captcha_id}')
    return result.text
