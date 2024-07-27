#!/Users/benedicthazel/.pyenv/shims/python

"""
Script to upgrade to the latest version of Rust via rustup.
"""

import subprocess

def upgrade_rust():
    """
    Upgrades to the latest version of Rust via rustup.
    """
    subprocess.run(['rustup', 'update'], check=True)

if __name__ == '__main__':
    upgrade_rust()
