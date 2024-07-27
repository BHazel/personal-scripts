#!/Users/benedicthazel/.pyenv/shims/python

"""
Script to update installed Homebrew packages.
"""

import subprocess

def update_homebrew_packages():
    """
    Updates installed Homebrew packages.
    """
    brew_update_comnand = subprocess.run(['brew', 'update'],
                                         capture_output=True,
                                         text=True,
                                         check=True)

    if 'Already up-to-date.' not in brew_update_comnand.stdout:
        subprocess.run(['brew', 'upgrade'], check=True)

    subprocess.run(['brew', 'cleanup'], check=True)

if __name__ == '__main__':
    update_homebrew_packages()
