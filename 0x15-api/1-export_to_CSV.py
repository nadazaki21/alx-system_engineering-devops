#!/usr/bin/python3
""" Task 1, Script that extends extend previous Python script to export data in the CSV format. """
import csv
import requests
from sys import argv


if __name__ == "__main__":
    file_name = 'USER_ID.csv'
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = r.json()
    
    
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    user_name = next((user['username'] for user in users if user['id'] == int(argv[1])), None)
    list_of_dicts = []
    
    
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    user_name = next((user['username'] for user in users if user['id'] == int(argv[1])), None)
    for item in data:
        # print(f"{True if item['userId'] == int(argv[1]) else False}")
        if item['userId'] == int(argv[1]):
            list_of_dicts.append({'USER_ID': item['userId'], 'USERNAME': user_name, 'TASK_COMPLETED_STATUS': item['completed'], 'TASK_TITLE': item['title']})
    
   
    
    
    with open(file_name, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])
        writer.writeheader()
        writer.writerows(list_of_dicts)

    