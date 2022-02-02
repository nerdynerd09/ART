import subprocess
import animation
import os
from colorama import Fore

class Subdomain():

    @animation.wait(animation='spinner',text=' [*] Finding Subdomains for you...')
    def assetfinder(self,domain):
        try:
            os.mkdir('results/subdomain')
        except FileExistsError: 
            pass

        with open('results/subdomain/assetfinder_result.txt','w') as f:
            f.write(subprocess.check_output(['assetfinder','--subs-only',domain]).decode('utf-8'))
        print(f"\n{Fore.GREEN} [+] {Fore.RESET}Done!!\n{Fore.RED} [+]{Fore.RESET} Assetfinder Result is saved in results/subdomain/assetfinder.txt")

    
