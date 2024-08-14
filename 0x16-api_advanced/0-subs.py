#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, allow_redirects=False)
    try:
        return res.json().get("data").get("subscribers")
    except requests.RequestException:
        return 0
