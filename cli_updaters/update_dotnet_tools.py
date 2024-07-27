#!/Users/benedicthazel/.pyenv/shims/python

"""
Script to update all installed global .NET tools.
"""

import subprocess

def update_global_dotnet_tools():
    """
    Updates all installed global .NET tools.
    """
    dotnet_tools_command = subprocess.run(['dotnet', 'tool', 'list', '-g'],
                                          capture_output=True,
                                          text=True,
                                          check=True)
    dotnet_tool_lines = dotnet_tools_command.stdout.splitlines()[2:]
    dotnet_tools = [line.split()[0] for line in dotnet_tool_lines]

    print(f'Updating {len(dotnet_tools)} .NET tools...')
    for tool in dotnet_tools:
        print(f'Updating {tool}...')
        subprocess.run(['dotnet', 'tool', 'update', '-g', tool], check=True)

if __name__ == '__main__':
    update_global_dotnet_tools()
