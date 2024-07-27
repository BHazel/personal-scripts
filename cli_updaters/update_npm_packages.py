#!/Users/benedicthazel/.pyenv/shims/python

"""
Script to update all installed global NPM packages.
"""

import subprocess

def update_global_npm_packages():
    """
    Updates all installed global NPM packages.
    """
    npm_list_command = subprocess.run(['npm', 'list', '-g', '-p'],
                                      capture_output=True,
                                      text=True,
                                      check=True)
    npm_packages_root = f'{npm_list_command.stdout.splitlines()[0]}/node_modules'
    npm_packages = [
        line.removeprefix(f'{npm_packages_root}/')
        for line
        in npm_list_command.stdout.splitlines()[1:]
    ]

    print(f'Updating {len(npm_packages)} NPM packages...')
    subprocess.run(['npm', 'update', '-g', *npm_packages], check=True)

if __name__ == '__main__':
    update_global_npm_packages()
