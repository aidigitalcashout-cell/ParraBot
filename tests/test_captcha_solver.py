import types

from fraud_bot.client.captcha_solver import solve_captcha


class DummyResponse:
    def __init__(self, text):
        self.text = text


def test_solve_captcha(monkeypatch):
    # Mock requests.post and requests.get
    def fake_post(url, data):
        return DummyResponse('OK|12345')

    def fake_get(url):
        return DummyResponse('CAPTCHA_RESULT')

    monkeypatch.setitem(__import__('sys').modules, 'requests', types.SimpleNamespace(post=fake_post, get=fake_get))

    result = solve_captcha('fake_image')
    assert result == 'CAPTCHA_RESULT'
