# config_loader.py

import importlib
import os
import sys

def load_config():
    try:
        # Try importing config.py (local secrets, not under version control)
        import config
        return config
    except ModuleNotFoundError:
        # Fall back to user_config.py if config.py doesn't exist
        print("⚠️ 'config.py' not found. Falling back to 'user_config.py', don't forget to fill out user_config.py with your email information!.")
        import user_config as config
        return config
