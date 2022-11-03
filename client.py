from secret import key, secret, key2, secret2
import pytumblr
import pytumblr2


client = pytumblr2.TumblrRestClient(
    key, secret, key2, secret2,
)

blogName = "zxxxcx"
tag_list = ["#love", "#art", "#life", "#hot", "#tumblr", "#art style ",
            "#digital art", "#me", "#roshi", "#zxxxcx", "#women"]
photo="dancingonheadstorypost";

def post_queue_photo():
    client.legacy_create_photo(blogName, state="queue", tags=tag_list,
                           caption="Dancing MANipulation. Made by Roshi.",
                           data="C:\\Users\\Korisnik\\Desktop\\Creativity Mode ON\\Untitled Export\\{}.jpg".format(photo))

def post_draft_multiple():
    if (client):
        client.create_photo(blogName, state="draft", tags=tag_list, format="markdown",
                            data=[
                                "C:\\Users\\Korisnik\\Desktop\\Creativity Mode ON\\Untitled Export\\layer0.jpg",
                                "C:\\Users\\Korisnik\\Desktop\\Creativity Mode ON\\Untitled Export\\layer1.jpg",
                                "C:\\Users\\Korisnik\\Desktop\\Creativity Mode ON\\Untitled Export\\layer3.jpg"],
                            caption="Telapatija. Made by Roshi.")
        print("Published.")
    else:
        print("Failed.")


def post_photo():
    if(client):
        client.create_post(
            blogName,
            content=[
                {"type": "image", "media": [
                    {"type": "image/jpeg", "identifier": "my_media_identifier"}]},
            ],
            tags=tag_list,
            caption="Voices. Made by Roshi.",
            media_sources={
                "my_media_identifier": "C:\\Users\\Korisnik\\Desktop\\Creativity Mode ON\\Untitled Export\\touch.jpg"}
        )
        print("Published.")
    else:
        print("Failed.")


post_queue_photo();