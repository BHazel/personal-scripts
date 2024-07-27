#!/Users/benedicthazel/.pyenv/shims/python

"""
Script to update all CLI tools and packages.
"""

from cli_updaters.update_dotnet_tools import update_global_dotnet_tools
from cli_updaters.update_homebrew_packages import update_homebrew_packages
from cli_updaters.update_npm_packages import update_global_npm_packages
from cli_updaters.upgrade_python import upgrade_python_version
from cli_updaters.upgrade_rust import upgrade_rust

print('Updating Homebrew packages...')
update_homebrew_packages()
print('Update complete.')

print('Updating global .NET tools...')
update_global_dotnet_tools()
print('Update complete.')

print('Updating global NPM packages...')
update_global_npm_packages()
print('Update complete.')

print('Upgrading Python...')
upgrade_python_version()
print('Upate complete.')

print('Upgrading Rust...')
upgrade_rust()
print('Update complete.')
