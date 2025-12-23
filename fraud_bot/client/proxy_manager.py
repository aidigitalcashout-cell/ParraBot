# proxy_manager.py

import random
from config import PROXY_POOL, VPN_SERVICES

def get_proxy():
    return random.choice(PROXY_POOL)

    def get_vpn():
        return random.choice(VPN_SERVICES)
    