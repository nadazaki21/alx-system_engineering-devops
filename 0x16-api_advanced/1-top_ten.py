#!/usr/bin/python3
"""
    queries the Reddit API and prints
    the titles of the first 10 hot posts
    listed for a given subreddit.


"""
import requests


def top_ten(subreddit):
    api_url = f"https://www.reddit.com/r/{subreddit}.json"
    api_params = {"raw_json": 1}  # must be a dictionary
    headers = {"User-Agent": "My Reddit API Client"}
    response = requests.get(
        api_url, allow_redirects=False, params=api_params, headers=headers
    )
    if response.status_code == 200:
        titles = []
        lists_of_posts = response.json().get("data").get("children")
        for post in lists_of_posts:
            titles.append(post.get("data").get("title"))
        for title in titles[:10]:
            print(title)
    else:
        print(None)
