import os
import time
import keyboard
import pyautogui
from termcolor import colored
from colorant import Colorant

#Settings
TOGGLE_KEY = 'F1'  # Toggle on/off colorant key
XFOV = 35  # X-Axis FOV
YFOV = 31  # Y-Axis FOV

INGAME_SENSITIVITY = 0.41
NEW_FLICKSPEED = 5.0  # Substitua este valor pelo que desejar
FLICKSPEED = NEW_FLICKSPEED
MOVESPEED = 2 / (5 * INGAME_SENSITIVITY)

print(f"Flick Speed: {FLICKSPEED}")
print(f"Move Speed: {MOVESPEED}")
monitor = pyautogui.size()
CENTER_X, CENTER_Y = monitor.width // 2, monitor.height // 2

def main():
    os.system('title Colorant')
    colorant = Colorant(CENTER_X - XFOV // 2, CENTER_Y - YFOV // 2, XFOV, YFOV, FLICKSPEED, MOVESPEED)
    print(colored('''
                     ▄████▄   ▒█████   ██▓     ▒█████   ██▀███   ▄▄▄       ███▄    █ ▄▄▄█████▓
                    ▒██▀ ▀█  ▒██▒  ██▒▓██▒    ▒██▒  ██▒▓██ ▒ ██▒▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒
                    ▒▓█    ▄ ▒██░  ██▒▒██░    ▒██░  ██▒▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░
                    ▒▓▓▄ ▄██▒▒██   ██░▒██░    ▒██   ██░▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ 
                    ▒ ▓███▀ ░░ ████▓▒░░██████▒░ ████▓▒░░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ 
                    ░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   
                      ░  ▒     ░ ▒ ▒░ ░ ░ ▒  ░  ░ ▒ ▒░   ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░    ░    
                    ░        ░ ░ ░ ▒    ░ ░   ░ ░ ░ ▒    ░░   ░   ░   ▒      ░   ░ ░   ░      
                    ░ ░          ░ ░      ░  ░    ░ ░     ░           ░  ░         ░          
                    ░                                                                         
                                              COLOR AIMBOT - v1.1''', 'magenta'))
    print()
    print(colored('[Info]', 'green'), colored('Set enemies to', 'white'), colored('Purple', 'magenta'))
    print(colored('[Info]', 'green'), colored(f'Press {colored(TOGGLE_KEY, "magenta")} to toggle ON/OFF Colorant', 'white'))
    print(colored('[Info]', 'green'), colored(f'Press', 'white'), colored('F2', 'magenta'), colored('to toggle ON/OFF Detection Window', 'white'))
    print(colored('[Info]', 'green'), colored('RightMB', 'magenta'), colored('= Aimbot,', 'white'))
    print(colored('[Info]', 'green'), colored('LeftAlt', 'magenta'), colored('= Triggerbot', 'white'))
    print(colored('[Info]', 'green'), colored('LeftCtrl', 'magenta'), colored('= Silentaim', 'white'))
    print(colored('[Info]', 'green'), colored('GitHub Repo:', 'white'),
          '\033[35;4mhttps://github.com/hafyzwithawhy/Colorant\033[0m')
    print(colored('[Info]', 'green'), colored('Made By', 'white'), colored('Hafez#6866', 'magenta'))
    status = 'Disabled'
    
    try:
        while True:
            if keyboard.is_pressed(TOGGLE_KEY):
                colorant.toggle()
                status = 'Enabled ' if colorant.toggled else 'Disabled'
            print(f'\r{colored("[Status]", "green")} {colored(status, "white")}', end='')
            time.sleep(0.01)
    except (KeyboardInterrupt, SystemExit):
        print(colored('\n[Info]', 'green'), colored('Exiting...', 'white') + '\n')
    finally:
        colorant.close()

if __name__ == '__main__':
    main()
