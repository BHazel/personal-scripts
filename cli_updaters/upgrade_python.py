#!/Users/benedicthazel/.pyenv/shims/python

"""
Script to upgrade to the latest version of Python via pyenv.
"""

import re
import subprocess

def upgrade_python_version():
    """
    Upgrades to the latest version of Python via pyenv.
    """
    pyenv_list_command = subprocess.run(['pyenv', 'install', '--list'],
                                        capture_output=True,
                                        text=True,
                                        check=True)
    pyenv_global_command = subprocess.run(['pyenv', 'global'],
                                          capture_output=True,
                                          text=True,
                                          check=True)

    semantic_version_regex = re.compile('^(\\s+)?(\\d+\\.)?(\\d+\\.)?(\\d+)$')
    cpython_versions = [
        version.strip()
        for version
        in pyenv_list_command.stdout.splitlines()
        if semantic_version_regex.match(version)
    ]

    latest_cpython_version = cpython_versions[-1]
    current_cpython_version = pyenv_global_command.stdout.strip()
    update_required = current_cpython_version != latest_cpython_version
    update_action_symbol = '->' if update_required else '=='
    print(f'{current_cpython_version} {update_action_symbol} {latest_cpython_version}')

    if update_required:
        print(f'Upgrading to Python {latest_cpython_version}...')
        subprocess.run(['pyenv', 'install', latest_cpython_version], check=True)
        subprocess.run(['pyenv', 'global', latest_cpython_version], check=True)
    else:
        print('Already up-to-date.')

if __name__ == '__main__':
    upgrade_python_version()
