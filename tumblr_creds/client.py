from tumblr_creds.secret import key1_os, key2_os, sec1_os, sec2_os
from termcolor import  cprint
from tumblr_creds.secret import path
import pytumblr2
import numpy as np

client = pytumblr2.TumblrRestClient(
    key1_os, sec1_os, key2_os, sec2_os,
)




#QUEONE ONE PHOTO  
def post_queue_photo(client,blogName,caption,pic,tag_list):
    if (client):
        client.legacy_create_photo(blogName, state="queue", tags=tag_list,
                            caption=caption,
                            #HERE YOU ENTER YOUR PATH WHERE IS THE IMAGE OR IMAGES
                           data=path+"{}.jpg".format(pic))
                          
        cprint("Queued successfully.","green")
    else:
        cprint("Failed.","red")
        
#POST ONE PHOTO INSTATLY    
def post_photo(client,blogName,caption,photo,tag_list):
    if(client):
        client.create_post(
            blogName,
            content=[
                {"type": "image", "media": [
                    {"type": "image/jpeg", "identifier": "my_media_identifier"}]},
            ],
            tags=tag_list,
            caption=caption,
            media_sources={
                "my_media_identifier": "C:\\Users\\Korisnik\\Desktop\\Creativity Mode ON\\Untitled Export\\CHAPTER 3\\{}.jpg".format(photo)}
        )
        print("Published photo.")
    else:
        print("Failed.")

##FOR MULTIPLE PHOTOS
def post_draft_multiple(client,blogName,caption,photos,tag_list):
    modified_photos=[]
    for p in photos:
        val=path+p+".jpg"
        modified_photos.append(val)
   
    if (client):
        client.legacy_create_photo(blogName, state="draft", tags=tag_list, format="markdown",
                            data=modified_photos,
                            caption=caption)
        cprint("Successfully drafted content.","green")
    else:
        cprint("Failed.Please try again.","red")
