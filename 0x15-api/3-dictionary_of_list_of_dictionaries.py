#!/usr/bin/python3
""" Task 2, Script that extends previous Python script to export data in the JSON format. """
import requests
import json

if __name__ == "__main__":
    file_name = "todo_all_employees.json"
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    
    # Create a dictionary to store user data with user id as key
    user_dict = {user['id']: user['username'] for user in users}
    
    result = {}
    
    for user_id, username in user_dict.items():
        result[str(user_id)] = []
        for todo in todos:
            if todo['userId'] == user_id:
                result[str(user_id)].append({
                    'task': todo['title'],
                    'completed': todo['completed'],
                    'username': username
                })

    with open(file_name, 'w') as file:
        json.dump(result, file, indent=4)
