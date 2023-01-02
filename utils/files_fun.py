import os
import numpy as np
from termcolor import colored, cprint
import time
from tumblr_creds.secret import path

def show_jpgs():
    list_of_files = filter( lambda x: os.path.isfile(os.path.join(path, x)),
                            os.listdir(path) )
    # Sort list of files based on last modification time in ascending order
    list_of_files = sorted( list_of_files,
                            key = lambda x: os.path.getmtime(os.path.join(path, x))
                            )
    # Iterate over sorted list of files and print file path 
    # along with last modification time of file 
    for file_name in list_of_files:
        if file_name.endswith(".jpg"):
            file_path = os.path.join(path, file_name)
            timestamp_str = time.strftime(  '%d/%m/%Y :: %H:%M:%S',
                                        time.gmtime(os.path.getmtime(file_path))) 
            cprint("File found:","green",attrs=["reverse", "blink"])
            print(timestamp_str, ' --> ', colored(file_name,"green"))  
            
def input_to_array():
    # Get input from the user
    user_input = input("Enter a list of images, separated by commas: ")

    # Split the input into a list of strings
    input_list = user_input.split(',')

    # Convert the list of strings to an array
    input_array = np.array(input_list)

    return input_array

