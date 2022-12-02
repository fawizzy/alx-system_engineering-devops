#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""

import requests

client_id = "KR3WYTJDillnHTGIE2lMzw"
secret_key = "09hHAPWLH4ghnvAaTsgTzhe-hYySZg"
developer = "Affectionate_Earth_9"

auth = requests.auth.HTTPBasicAuth(client_id, secret_key)


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get('http://www.reddit.com/r/{}/about.json'.format(subreddit),
                     headers={'User-Agent': 'hello'}).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs