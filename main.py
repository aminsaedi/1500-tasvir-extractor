import tweepy
from PIL import Image
import os

api_key = "pX0hIGEAMcoBbjg5Frsrtp2am"
api_key_secret = "5ovM5UirOBzMZxRaqcqp8ukjRGg8E1Up4DiUn53BNF2GGkGrSa"
access_token = "1040415070533115907-rtEoWqyZzl21VF0RMxx0vtE1dG8wMo"
access_token_secret = "7OdHO1pHjFohtHPO1GflEjZfALnj1v1Kplb854DNDqYuO"

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def get_tweet_detail(id):
    tweet = api.get_status(id, tweet_mode="extended")
    return [tweet.full_text, tweet.created_at]


def is_image_contains_box(image):
    width, height = image.size
    # if (image.getpixel((1, 1)) != (248, 241, 231)):
    #     return False
    count_in_box = 0
    count_out_box = 0
    for y in range(height):
        color = image.getpixel((1, y))
        # if all colors are between 60 and 65
        if all(50 <= c <= 70 for c in color):
            count_in_box += 1
        # if color are similar to (248, 241, 231)
        if all(220 <= c <= 250 for c in color):
            count_out_box += 1
    if count_in_box > 100 and count_out_box > 1000:
        return True
    return False


for file in os.listdir('./images'):
    if file.endswith('.jpg'):
        image = Image.open("./images/" + file)
        if is_image_contains_box(image):
            # split file name by _
            file_name = file.split('_')
            # get tweet id
            tweet_id = file_name[0]
            # get tweet text
            tweet_detail = get_tweet_detail(tweet_id)
            # remove extension from file name
            print(file)
            file = file.split('.')[0]

            first_word = tweet_detail[0].split(' ')[0][1:]
            first_word = first_word.replace('_', ' ')
            first_word = first_word.replace('،', '')

            text = f"""---
id: "{file}"
title: "{first_word}"
subtitle: "توضیحات آزمایشی"
date: "{tweet_detail[1]}"
---
{tweet_detail[0]}
"""
            # create new file
            new_file = open(f"posts/{file}.md", "w")
            new_file.write(text)
            new_file.close()
        else:
            # remove file
            os.remove("./images/" + file)
