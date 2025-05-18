# Importing libraries
import os

# Main loop
while True:
    command = input("james@python~$: ")

    if 'plugins' in command:
        os.system("cd plugins\nls")
    
    elif 'clear' in command:
        os.system("clear")
    
    elif "get" in command:
        os.system(f"cd Downloads\n w{command}")
    
    elif "update" in command:
        os.system("sudo apt update\nsudo apt upgrade\napt list upgradable\nsudo apt autoremove\napt clean")
    
    elif 'ls' in command:
        os.system("ls")
    
    else:
        os.system(f"cd plugins\npython3 {command}.py")