#!/usr/bin/python3
"""
    returns the number of subscribers (not active users,
    total subscribers) for a given subreddit. If an invalid
    subreddit is given, the function should return 0.

"""
import requests
from json import loads, dump, dumps


def number_of_subscribers(subreddit):
    api_url = f"https://www.reddit.com/r/{subreddit}/\
    about.json"
    api_params = {"raw_json": 1}  # must be a dictionary
    headers = {"User-Agent": "My Reddit API Client"}
    response = requests.get(
        api_url, allow_redirects=False, params=api_params, headers=headers
    )
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
