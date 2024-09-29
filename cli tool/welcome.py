import argparse

def welcome():
    message = """
            Welcome to Pumpkin3D!
            
            To create your first project type "pump3d -project," and then type pump3d to enter the editor.
            
            Special thanks to all contributors, maintainers and backers, for helping keep this project free and open source!
    """
    print(message.center(80))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pump3d Miscellaneous Commands')
    
    # Adding argument for -misc
    parser.add_argument('-misc', action='store_true', help='Miscellaneous commands')
    
    # Adding argument for --welcome
    parser.add_argument('--welcome', action='store_true', help='Display the welcome message')
    
    args = parser.parse_args()
    
    if args.misc and args.welcome:
        welcome()
    else:
        print("Usage: pump3d -misc --welcome")
