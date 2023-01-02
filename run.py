from utils.user_fun import saveUser,checkUser,getUserName
from tumblr_creds.client import post_queue_photo,post_photo,post_draft_multiple
from tumblr_creds.client import client
from termcolor import  cprint
from utils.files_fun import show_jpgs,input_to_array
import os
os.system("")




best_tags=["#tumblr", "#aesthetic", "#love", "#like", "#tumblrgirl", "#follow",
           "#instagram" ,"#instagood","#photography" ,"#likeforlikes" ,"#s",
           "#art" ,"#likes" ,"#tumblrboy" ,"#frasi" ,"#grunge","#girl","#o" ,"#cute","#fashion" 
           ,"#sad" ,"#photooftheday" ,"#photo", "#frases" ,"#followforfollowback" ,"#frasitumblr" ,
           "#a" ,"#amor" ,"#tumblraesthetic" ,"#tiktok"]


my_tags= ["#love", "#art", "#life", "#hot", "#tumblr", "#art style ",
            "#digital art", "#me", "#roshi", "#zxxxcx", "#women","#aesthetic"]




blog_name="";  
    
if(checkUser()): ## if true
    blog_name=getUserName()
    cprint("WELCOME BACK "+blog_name.upper()+"!!","green")
else:
    blog_name=input("Enter yours blog name: ")      
    save_blog_name=input("Do you want to save it type y/n: ")
    if(save_blog_name=="y"):
            saveUser(blog_name)
    elif(save_blog_name=="n"):
       print("Consider saving it so u dont have to type it all over again :)")






print("Hello first of all choose picture post type:")
print("[0] post_queue_photo\n[1] post_photo\n[2] post_draft_multiple")
choose_post_type=int(input())

post_type=[post_queue_photo,
           post_photo,
           post_draft_multiple]


if(choose_post_type==0):
    #DISPLAYS FILES IN PATH INPUTED
    show_jpgs()

    caption=input("Enter caption: ")
    pic=input("Enter photo name: ")
    post_queue_photo(client,blog_name,caption,pic,my_tags)
elif(choose_post_type==1):
    #DISPLAYS FILES IN PATH INPUTED
    show_jpgs()

    caption=input("Enter caption: ")
    pic=input("Enter photo name: ") 
    post_photo(client,blog_name,caption,pic,my_tags)
##TODO upload multiple files   
elif(choose_post_type==2):
    #DISPLAYS FILES IN PATH INPUTED
    show_jpgs()

    cprint("Psst, heads up: You can upload up to 30 image files!","blue")
    caption=input("Enter caption: ")
    photos=input_to_array()
    post_draft_multiple(client,blog_name,caption,photos,my_tags)
else:
    print("You've choose no option.Shutting down... :(")
    exit;
    


    





