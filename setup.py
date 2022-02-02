import subprocess
import shutil
import animation

@animation.wait(animation='spinner',text=' [*] Setting Up Environment for You!!')
def scriptSetup():

    #Waybackurls
    subprocess.check_output(['go','install','github.com/tomnomnom/waybackurls@latest'])
    shutil.copy('/root/go/bin/waybackurls','/usr/local/bin')

    #Gau
    subprocess.check_output(['go','install','github.com/lc/gau/v2/cmd/gau@latest'])
    shutil.copy('/root/go/bin/gau','/usr/local/bin')

    # Assetfinder
    subprocess.check_output(['go','install','github.com/tomnomnom/assetfinder@latest'])
    shutil.copy('/root/go/bin/assetfinder','/usr/local/bin')

    # Arjun
    subprocess.check_output(['pip3','install','arjun'])
    
    

