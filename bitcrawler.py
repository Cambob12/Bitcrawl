import random 
import string 
import time
import ctypes

ctypes.windll.kernel32.SetConsoleTitleA(" ")

print('''
    ____  _ __  ______                    __         
   / __ )(_) /_/ ____/________ __      __/ /__  _____
  / __  / / __/ /   / ___/ __ `/ | /| / / / _ \/ ___/
 / /_/ / / /_/ /___/ /  / /_/ /| |/ |/ / /  __/ /    
/_____/_/\__/\____/_/   \__,_/ |__/|__/_/\___/_/     
''')

input("[+][v1.34] Press Enter to continue...")
print("This will crawl trough Bitcoin wallets untill it finds a valid address.")
print("[+] Starting...")
time.sleep(2)
print("[+] Contacting server...")
time.sleep(3)
print("[+] Connected to server.")
time.sleep(2)
print("[+] Starting crawler...")


letters = string.ascii_letters
numbers = string.digits
special = string.punctuation

ammount = 0


while True:
    # Generate a random string of letters numbers and punctuation
    password = ''.join(random.choice(letters + numbers + special) for i in range(random.randint(48, 48)))
    print(f"{password} [0BTC]")

    # Wait for a bit
    time.sleep(0.01)
    ammount += 1

    if ammount == 100:
        rand = random.randint(1, 5)

        if rand == 1:
            random_float = random.uniform(0.01, 0.1)
            print(f"\n{password} [{random_float}BTC]")
        else:
            ammount = 0

