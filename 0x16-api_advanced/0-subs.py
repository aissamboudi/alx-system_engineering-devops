#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    res = requests.get(url, allow_redirects=False)
    try:
        res = requests.get(url, allow_redirects=False)
        res.raise_for_status()  # Check for HTTP errors
        data = res.json()
        return data.get("data", {}).get("subscribers", 0)
    except requests.exceptions.RequestException:
        return 0
    except ValueError:
        return 0
