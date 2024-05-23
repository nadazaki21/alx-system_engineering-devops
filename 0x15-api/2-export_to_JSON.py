#!/usr/bin/python3
""" Task 3, Script that extends extend previous Python script to export data in the JSON format. """
import requests
from sys import argv
import json


if __name__ == "__main__":
    file_name = 'USER_ID.json'
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = r.json()
    
    
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    user_name = next((user['username'] for user in users if user['id'] == int(argv[1])), None)
    result  = {f'{argv[1]}':[]}
    
    
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    user_name = next((user['username'] for user in users if user['id'] == int(argv[1])), None)
    for item in data:
        if item['userId'] == int(argv[1]):
            result[f'{argv[1]}'].append({ 'task': item['title'], 'completed': item['completed'], 'username': user_name,})

    with open(file_name, 'w') as file:
        json.dump(result, file, indent=4)

    
    
    