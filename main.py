# Importing libraries
import os

# Main loop
while True:
    command = input("py@projects~$: ")

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

    elif 'quit' in command:
        break

    elif 'shutdown' in command:
        os.system("shutdown now")

    elif 'restart' in command:
        os.system("restart")

    elif 'help' in command:
        print("""
        1. Timer: a timer program (if only there was some was to infer the function of this program).
        Usage: timer

        2. Guesses: a simple hangman-like word guessing game.
        DO NOT DELETE, REMOVE, OR EXECUTE THE "guesses_data.py" FILE IT IS USED BY THE GAME FOR A LIST OF WORDS.
        Usage: guesses (guess letters in the word within ten guesses).
        Tip: (you can add or remove words from the game by modifying the "guessing_data.py").

        3. Basic Calculator: a very simple calculator (outdated)
        Usage: basic_calculator (enter in a simpe equation +-*/% execpted i.e "2 + 2", "1 % 10"

        4. Advanced Calculator: a much more complicated calculator capible of solving equations with multiple opperators with PEMDAS.
        Usage: advanced_calculator (enter an equation (only use ONE pair of paranthesis per equation or you will have a error)
        quit: to exit
        clear: to clear the calculator
        
        5. Text Replacer: simple program to replace specified characters or words with other specified characters or words.
        Usage: replace <your input file> <you output file> <character or word to replace> <replacing word of character>
    """)
    
    else:
        os.system(f"cd plugins\npython3 {command}.py")
