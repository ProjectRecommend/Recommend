from lxml import objectify
import requests
import sys
import re

apiurl = "http://api.lololyrics.com/0.5/getLyric"


def getLyrics(artist, track):
    try:
        payload = {'artist': artist, 'track': track}
        print(payload)
        r = requests.get(apiurl, params=payload)
        # print(r)
        result = objectify.fromstring(r.text.encode("utf-8"))
        # print(result)
        if result.status == 'OK':
            # print(result.response)
            print(result.response)
            print('****OK***')
            return result.response
        else:
            print("Not 200 ")
            print(result.status)
    except:
        print("Not OK")
