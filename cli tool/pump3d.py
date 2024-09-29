import argparse
from commands.welcome import welcome
from commands.version import version
from commands.help import help_command

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pump3D CLI Tools')
    
    # Adding the welcome command under -misc
    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Subcommand for welcome under -misc
    welcome_parser = subparsers.add_parser('welcome', help='Display the welcome message')
    welcome_parser.add_argument('-misc', action='store_true', help='Miscellaneous command for welcome')

    # Subcommand for version (no flags needed)
    subparsers.add_parser('version', help='Show the version of the script')

    # Subcommand for help (no flags needed)
    subparsers.add_parser('help', help='Show help information')

    args = parser.parse_args()
    
    if args.command == 'welcome' and args.misc:
        welcome()
    elif args.command == 'version':
        version()
    elif args.command == 'help':
        help_command()
    else:
        print("Usage: pump3d [command] [--misc for welcome]")
