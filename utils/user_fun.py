import json
from termcolor import cprint
from datetime import datetime
def checkUser():
    try:
        with open('user_info.json', 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        name = json_object["name"]
        if(name == ""):
            return False;
        return True;
    except:
        return False;
    
    
    
def saveUser(blog_name):
    
    current_dateTime = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    user_json = json.dumps(
        {"name":blog_name,
         "created":current_dateTime
        }
        )
    with open("user_info.json", "w") as outfile:
        outfile.write(user_json)
    cprint("Sucessfuly saved","green")       

def getUserName():
    try:
        with open('user_info.json', 'r') as openfile:
            # Reading from json file
            json_object = json.load(openfile)
        name = json_object["name"]
        if(name==""):
            return "";
        return name;
    except:
        return False;