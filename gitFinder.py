from re import sub
import re
import animation
import subprocess

class GitFinder:
    def getLink(self):
        gitLink = input("Enter a git repo link: ")
        # print(gitLink)
        GitFinder.trufflehog(self,gitLink)

    def trufflehog(self,gitLink):
        print(f"new: {gitLink}")
        try:
            # result = subprocess.check_output(["trufflehog","--regex","--entropy","=","False","https://github.com/dxa4481/truffleHog.git"])
            result = subprocess.check_output(['trufflehog','--regex','--entropy','=','False','https://github.com/dxa4481/truffleHog.git'])
            print(result)
        except subprocess.CalledProcessError as e:
            # print(e.output)
            # print(e.returncode)
            print("Coder")