import subprocess
import os
import requests
import animation
import re
from colorama import Fore


class ParamterDiscovery:
    @animation.wait(animation='spinner',text=' [*] Finding parameters using Arjun. This may take time...')
    def arjun(self,domain):
        if("https://" in domain):
            domain = domain
        else:
            domain = "https://"+domain
        if (domain[-1] == '/'):
            domain = domain
        else:
            domain = domain + '/'

        try:
            os.mkdir('results/parameter')
        except FileExistsError:
            pass
        subprocess.check_output(['arjun','-u',domain,'-oT','results/parameter/arjun.txt'])
        print(f"\n{Fore.GREEN} [+] {Fore.RESET}Done!!\n{Fore.RED} [+]{Fore.RESET} Arjun Result is saved in results/parameter/arjun.txt")

    @animation.wait(animation='spinner',text=' [*] Finding parameters using Paramfuzzer...')
    def paramFuzzer(self,domain):
        url=f"https://web.archive.org/cdx/search/cdx?url=*.{domain}&output=txt&fl=original&collapse=urlkey&page=/"

        try:
            result = requests.get(url).text

            with open('results/parameter/paramfuzzer.txt','w') as fp:
                for i in(re.findall(r".*=.*",result)):
                    # print(i)
                    fp.write(i+'\n')
            print(f"\n{Fore.GREEN} [+] {Fore.RESET}Done!!\n{Fore.RED} [+]{Fore.RESET} ParamFuzzer Result is saved in results/parameter/paramfuzzer.txt")
        except:
            print(f"\n{Fore.RED} [-] {Fore.RESET}Some error occured with ParamFuzzer!!\n{Fore.RED} [-] {Fore.RESET}Sorry for the inconvenience.")
            pass