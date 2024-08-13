#!/usr/bin/python3
"""contains the definiton of number_of_subscribers function"""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if response.ok:
        return response.json().get('data').get('subscribers')
    else:
        return 0
