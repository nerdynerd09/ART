import os
import animation
from colorama import Fore
import subprocess

class Crawler:
    @animation.wait(animation='spinner',text=' [*] Crawling target using waybackurls...')
    def waybackUrls(self,domain):
        try:
            os.mkdir('results/crawler')
        except FileExistsError: 
            pass

        with open('results/crawler/waybackurls.txt','w') as f:
            f.write(subprocess.check_output(['waybackurls',domain]).decode('utf-8'))
        print(f"\n{Fore.GREEN} [+] {Fore.RESET}Done!!\n{Fore.RED} [+]{Fore.RESET} Waybackurl Result is saved in results/crawler/waybackurls.txt")
    
    @animation.wait(animation='spinner',text=' [*] Crawling target using GAU...')
    def gau(self,domain):
        with open('results/crawler/gau.txt','w') as f:
            f.write(subprocess.check_output(['gau',domain]).decode('utf-8'))
        print(f"\n{Fore.GREEN} [+] {Fore.RESET}Done!!\n{Fore.RED} [+]{Fore.RESET} Gau Result is saved in results/crawler/gau.txt")
    