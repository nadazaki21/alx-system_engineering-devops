#!/usr/bin/python3
""""
 function to return all list of titles but with paginattion

"""
import requests


def recurse_hepler(subreddit, hot_list=[], after_param=None):
    if after_param == 'null':
        print("reached end of pages")
        return hot_list

    api_url = f"https://www.reddit.com/r/{subreddit}.json"
    api_params = {"raw_json": 1, "after": after_param}
    headers = {"User-Agent": "My Reddit API Client"}
    response = requests.get(
        api_url, allow_redirects=False, params=api_params, headers=headers
    )
    if response.status_code == 200:
        
        lists_of_posts = response.json().get("data").get("children")
        for post in lists_of_posts:
            hot_list.append(post.get("data").get("title"))

        print(len(hot_list))
        after_param = response.json().get("data").get("after")

        if after_param == "null":
            print("reached end of pages")
            return hot_list

        recurse_hepler(subreddit, hot_list, after_param)


def recurse(subreddit, hot_list=[]):
    api_url = f"https://www.reddit.com/r/{subreddit}.json"
    api_params = {"raw_json": 1}  # must be a dictionary
    headers = {"User-Agent": "My Reddit API Client"}
    response = requests.get(
        api_url, allow_redirects=False, params=api_params, headers=headers
    )
    print(response.status_code)
    if response.status_code == 200:
        titles = []
        lists_of_posts = response.json().get("data").get("children")
        for post in lists_of_posts:
            titles.append(post.get("data").get("title"))

        after_param = response.json().get("data").get("after")

        res = recurse_hepler(subreddit, titles, after_param)
        print(len(res))
        return res
    else:
        return(None)
