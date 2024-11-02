#!/Users/benedicthazel/.pyenv/shims/python

"""
Script to update all GitHub CLI extensions.
"""

import subprocess

def update_github_cli_extensions():
    """
    Updates all GitHub CLI extensions.
    """
    subprocess.run(['gh', 'extension', 'upgrade', '--all'],
                   text=True,
                   check=True)

if __name__ == '__main__':
    update_github_cli_extensions()
