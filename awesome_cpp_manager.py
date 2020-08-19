#imports
import requests
from bs4 import BeautifulSoup
#import cmake
from git.repo.base import Repo
import zipfile
import io
import random
import string
import os
#end of imports

#initalization
print("""
   ___                                _____  __    __ 
  / _ |_    _____ ___ ___  __ _  ___ / ___/_/ /___/ /_
 / __ | |/|/ / -_|_-</ _ \/  ' \/ -_) /__/_  __/_  __/
/_/ |_|__,__/\__/___/\___/_/_/_/\__/\___/ /_/   /_/  
               __  ___                           
              /  |/  /__ ____  ___ ____ ____ ____
             / /|_/ / _ `/ _ \/ _ `/ _ `/ -_) __/
            /_/  /_/\_,_/_//_/\_,_/\_, /\__/_/   
                                  /___/    
Awesome C++ Manager \u00A9 2020 S\u00B7Frydrych             
Featured: BOOST (https://www.boost.org/) and POCO (https://pocoproject.org/) library collections
You can download standart cpp libraries here: https://github.com/apache/stdcxx
Usage: find 'library', build 'path to folder', 'github repo link' or 'zip file link', exit
""")
#initalized

#scraping html
r = requests.get('https://github.com/fffaraz/awesome-cpp')
soup = BeautifulSoup(r.content, 'html.parser')
#html saved

#program loop
while True:
    lib = input("> ")
    if lib.find("find") != -1:
        search = lib.split(" ")[1]
        for link in soup.find_all("a"): ##finding all anchors
            if search in link.get('href') and "//" in link.get('href') or search in link: ###if input in hypertext and its a valid url or if input is in html text
                print(link.get('href'))
    elif lib.find("build") != -1:
        if os.path.exists("libs"): pass
        else: os.mkdir("libs")
        print("Download cmake if you haven't done it before> https://cmake.org/download!")
        url = lib.split(" ")[1]
        foldername = ""
        if "github.com/" in url: ##git clone
            repo = url.split("/")[4] ###splitting repo name
            cloneresult = Repo.clone_from(url, os.path.dirname(os.path.realpath(__file__)) + "/libs/" + repo)
            print(cloneresult)
            foldername = "/libs/" + repo
        elif ".zip" in url: ##downloading and unpacking zip
            r = requests.get(url)
            z = zipfile.ZipFile(io.BytesIO(r.content))
            folder = "".join(random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase) for _ in range(8))
            z.extractall("/libs/" + folder)
            foldername = "/libs/" + folder ##generate random foldername because we dont know the actual zip name
        else: ##if url is local path
            foldername = url
        os.system("cmake " + os.path.dirname(os.path.realpath(__file__)) + foldername)
        os.system("make") #building with cmake
        print(f"Check {foldername}!")
    elif lib=="exit":
        exit(0)
    else:
        print("Wrong command")
