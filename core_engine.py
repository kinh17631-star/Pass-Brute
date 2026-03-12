import time
import sys
import os

def start_attack(username, list_path):
    if not os.path.exists(list_path):
        print(f"\033[1;31m[X] Error: {list_path} not found!\033[0m")
        return

    print(f"\033[1;34m[*] Target User: {username}\033[0m")
    print(f"\033[1;34m[*] Loading Dictionary: {list_path}\033[0m")
    print("\033[1;33m[*] BRUTE-FORCE SEQUENCE ENGAGED...\033[0m\n")
    time.sleep(1.5)

    with open(list_path, "r") as f:
        for password in f:
            password = password.strip()
            # Fast-scrolling effect for video
            sys.stdout.write(f"\r\033[1;37m[#] TRYING: {username} -> {password} \033[0m")
            sys.stdout.flush()
            time.sleep(0.08) 

    print("\n\n\033[1;32m[!] SUCCESS! CREDENTIALS EXTRACTED.\033[0m")
    print(f"\033[1;32m[+] KEY: {password}\033[0m")

if __name__ == "__main__":
    if len(sys.argv) > 2:
        start_attack(sys.argv[1], sys.argv[2])

