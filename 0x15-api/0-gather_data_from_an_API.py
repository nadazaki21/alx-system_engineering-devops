#!/usr/bin/python3
""" Task 0, Script that uses an available RESTAPI to display info """
import requests
from sys import argv



if __name__ == "__main__":
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = r.json()
    counter_all = 0
    counter_completed = 0
    completed_tasks = []
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    user_name = next((user['username'] for user in users if user['id'] == int(argv[1])), None)
    for item in data:
        # print(f"{True if item['userId'] == int(argv[1]) else False}")
        if item['userId'] == int(argv[1]):
            counter_all = counter_all + 1
            if item['completed'] is True:
                counter_completed = counter_completed + 1
                completed_tasks.append(item['title'])
    
    print (f"Employee {user_name} is done with tasks({counter_completed}/{counter_all}):")
    for task in completed_tasks:
        print(f"\t{task}")
