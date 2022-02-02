import subprocess
import animation
import re
from colorama import Fore

class JSFinder:
    @animation.wait(animation='spinner',text=' [*] Finding js files...')
    def jsfinder(self,domain):
        result = subprocess.check_output(['waybackurls',domain,'|','uniq'])

        with open('results/jsfiles.txt','w') as fp:
            for i in (re.findall(r'.*\.js.*',str(result.decode('utf-8')))):
                fp.write(i+'\n')
        print(f"\n{Fore.GREEN} [+] {Fore.RESET}Done!!\n{Fore.RED} [+]{Fore.RESET} JsFinder Result is saved in results/jsfiles.txt")
