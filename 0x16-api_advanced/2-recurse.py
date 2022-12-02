import requests


def recurse(subreddit, after="", hot_list=[], count=0):
    """returns the number of subscribers for a given subreddit"""
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
    
    for list in response.get("children"):
        hot_list.append(list.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, after, hot_list, count)
    return hot_list