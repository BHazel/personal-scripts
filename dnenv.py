#!/Users/benedicthazel/.pyenv/shims/python

"""
Script to set the .NET version for the current directory and children.
"""

import argparse
import os
import subprocess

GLOBAL_JSON_FILENAME = 'global.json'

def generate_global_json(version: str):
    """
    Generates a global.json file with the specified .NET version.

    Args:
        version (str): The .NET version to use.
    """
    global_json_contents = f"""{{
  "sdk": {{
    "version": "{version}"
  }}
}}
"""
    if os.path.exists(GLOBAL_JSON_FILENAME):
        print('.NET global.json already exists.')
    else:
        with open(GLOBAL_JSON_FILENAME, 'w', encoding='utf-8') as global_json_file:
            global_json_file.write(global_json_contents)

def delete_global_json():
    """
    Deletes the global.json file.
    """
    if os.path.exists(GLOBAL_JSON_FILENAME):
        os.remove(GLOBAL_JSON_FILENAME)

def list_dotnet_sdks(sdks: list[str]):
    """
    Lists the available .NET SDKs.

    Args:
        sdks (list[str]): The available .NET SDKs.
    """
    for sdk in sdks:
        print(sdk)

def get_dotnet_version():
    """
    Gets the current .NET version.
    """
    dotnet_version_command = subprocess.run(['dotnet', '--version'],
                                            capture_output=True,
                                            text=True,
                                            check=True)
    print(dotnet_version_command.stdout.strip())

parser = argparse.ArgumentParser(description='Sets the .NET version for the current directory tree')
parser.add_argument('-l', '--list',
                    action='store_true',
                    help='Lists the .NET versions available.')
parser.add_argument('-s', '--set',
                    type=str,
                    dest='sdk',
                    help='Sets the .NET SDK version to use.')
parser.add_argument('-g', '--get',
                    action='store_true',
                    help='Gets the current .NET SDK version.')
parser.add_argument('-c', '--clear',
                    action='store_true',
                    help='Clears the .NET version to use the default.')
arguments = parser.parse_args()

dotnet_list_sdks_command = subprocess.run(['dotnet', '--list-sdks'],
                                          capture_output=True,
                                          text=True,
                                          check=True)
dotnet_sdk_lines = dotnet_list_sdks_command.stdout.splitlines()
dotnet_sdks = [line.split()[0] for line in dotnet_sdk_lines]

if arguments.clear:
    delete_global_json()
elif arguments.list:
    list_dotnet_sdks(dotnet_sdks)
elif arguments.sdk:
    generate_global_json(arguments.sdk)
elif arguments.get:
    get_dotnet_version()
