import subdomain,crawler,parameter,jsFinder,gitFinder,setup
import os
import animation,subprocess
import argparse
import sys,time
import whois
import json
from colorama import Fore

class ART(object):

    def banner(self):
        text = Fore.GREEN+"""    ___       __                               ____                           ______            __
   /   | ____/ /   ______ _____  ________     / __ \___  _________  ____     /_  __/___  ____  / /
  / /| |/ __  / | / / __ `/ __ \/ ___/ _ \   / /_/ / _ \/ ___/ __ \/ __ \     / / / __ \/ __ \/ / 
 / ___ / /_/ /| |/ / /_/ / / / / /__/  __/  / _, _/  __/ /__/ /_/ / / / /    / / / /_/ / /_/ / /  
/_/  |_\__,_/ |___/\__,_/_/ /_/\___/\___/  /_/ |_|\___/\___/\____/_/ /_/    /_/  \____/\____/_/  v 1.0  
                                                            
                                                            Coded by:  Nakba
                                                            Instagram: @hackersarena0 
                                                            Github:    github.com/nerdynerd09\n
"""+Fore.RESET
        
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.009)
    # Setting up the environment
    def setupChekcUp(self):
        setup.scriptSetup()

        try:
            os.mkdir('results')
        except FileExistsError:
            pass

    def intro(self):
        parser = argparse.ArgumentParser(description="Advanced Enumeration Tool Help Section")
        parser.add_argument('-d','--domain', help="Enter the domain name")
        parser.add_argument('-wh','--whois', action="store_true",help="Finds whois info for you.")
        parser.add_argument('-sub','--subdomain', action="store_true",help="Does Subdomain Enumeration")
        parser.add_argument('-cr','--crawl', action="store_true",help="Crawls the target using gau and waybackurls")
        parser.add_argument('-pr','--param', action="store_true",help="Finds paramters on the target")
        parser.add_argument('-js','--jsfiles', action="store_true",help="Finds js files.")
        parser.add_argument('-a','--all', action="store_true",help="Runs all the command")
        self.args = parser.parse_args()
        
        # global domain
        # domain = self.args.domain
        
        # Finding whois info
        if(self.args.whois == True):
            self.whois()

        # Finding Subdomains
        if(self.args.subdomain == True):
            subdomain.Subdomain.assetfinder(self,self.args.domain)  

        # Crawling the target
        if(self.args.crawl == True):
            crawler.Crawler.waybackUrls(self,self.args.domain)    
            crawler.Crawler.gau(self,self.args.domain)    

        # Finding Parameters
        if(self.args.param == True):
            parameter.ParamterDiscovery.paramFuzzer(self,self.args.domain)
            parameter.ParamterDiscovery.arjun(self,self.args.domain) 

        # Finding js files
        if(self.args.jsfiles == True):
            jsFinder.JSFinder.jsfinder(self,self.args.domain)   

        # Running all programs
        if(self.args.all == True):
            self.whois()
            subdomain.Subdomain.assetfinder(self,self.args.domain)
            crawler.Crawler.waybackUrls(self,self.args.domain)    
            crawler.Crawler.gau(self,self.args.domain)   
            jsFinder.JSFinder.jsfinder(self,self.args.domain)        
            parameter.ParamterDiscovery.paramFuzzer(self,self.args.domain)
            parameter.ParamterDiscovery.arjun(self,self.args.domain)
               

    @animation.wait(animation='spinner',text=" [*] Fetching Whois info....")
    def whois(self):
        try:
            os.mkdir('results/whois')
        except FileExistsError: 
            pass

        with open('results/whois/whoisInfo.txt','w') as f:
            f.write(subprocess.check_output(['whois',self.args.domain]).decode('utf-8'))
        print(f"\n{Fore.GREEN} [+] {Fore.RESET}Done!!\n{Fore.RED} [+]{Fore.RESET} Whois information for {self.args.domain} is saved in results/whois/whoisInfo.json")
       

art = ART()
art.banner()
art.setupChekcUp()
art.intro()
