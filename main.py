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
    for y in range(height):
        # target color r: 22.0 g:21.6 b:20.7
        color = image.getpixel((1, y))
        box_color = (64, 63, 61)
        if color == box_color:
            return True
    return False


for file in os.listdir('./images'):
    if file.endswith('.jpg'):
        image = Image.open("./images/" + file)
        width, height = image.size
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


# get tweet text by id
