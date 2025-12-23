"""Wrapper to run the server with imports resolving to project layout."""
import os
import sys

# Ensure project root and client directory are on sys.path so modules imported
# without package qualifiers (e.g., `card_manager`) can be found.
ROOT = os.path.dirname(__file__)
CLIENT = os.path.join(ROOT, 'fraud_bot', 'client')
SERVER = os.path.join(ROOT, 'fraud_bot', 'server')
for p in (ROOT, CLIENT, SERVER):
    if p not in sys.path:
        sys.path.insert(0, p)

from fraud_bot.server.app import start_server


if __name__ == '__main__':
    start_server()
