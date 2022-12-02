#!/usr/bin/python3
import requests

def count_words(subreddit, word_list):
    if subreddit is None or type(subreddit) is not str:
        return 0
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "0x16-api_advanced:project:\
v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    response = response.json().get("data")
    after = response.get("after")
    count += response.get("dist")