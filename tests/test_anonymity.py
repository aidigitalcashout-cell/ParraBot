class DummyBrowser:
    def __init__(self):
        self.scripts = []

    def execute_script(self, script):
        self.scripts.append(script)


from fraud_bot.client.anonymity import simulate_human_behavior


def test_simulate_human_behavior(monkeypatch):
    # Patch time.sleep to speed up test
    monkeypatch.setitem(__import__('sys').modules, 'time', __import__('types').SimpleNamespace(sleep=lambda x: None))

    browser = DummyBrowser()
    # call function
    simulate_human_behavior(browser)
    # verify script executed
    assert any('scrollTo' in s for s in browser.scripts)
