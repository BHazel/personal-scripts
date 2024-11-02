#!/Users/benedicthazel/.pyenv/shims/python

"""
Script to update all installed Azure CLI extensions.
"""

import json
import subprocess

def update_azure_cli_extensions():
    """
    Updates all Azure CLI extensions.
    """
    azure_cli_extensions_command = subprocess.run(['az', 'extension', 'list'],
                                                    capture_output=True,
                                                    text=True,
                                                    check=True)
    azure_cli_extensions_json = azure_cli_extensions_command.stdout
    azure_cli_extensions = [
        extension['name'] for extension in json.loads(azure_cli_extensions_json)
    ]

    print(f'Updating {len(azure_cli_extensions)} Azure CLI extensions...')
    for extension in azure_cli_extensions:
        print(f'Updating {extension}...')
        subprocess.run(['az', 'extension', 'update', '--name', extension], check=True)

if __name__ == '__main__':
    update_azure_cli_extensions()
