#!/usr/bin/python3
import json
import requests

def fetch_users():
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    users = response.json()
    return users

def fetch_tasks():
    response = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = response.json()
    return tasks

def main():
    users = fetch_users()
    tasks = fetch_tasks()

    data = {}
    
    for user in users:
        user_id = user['id']
        username = user['username']
        user_tasks = [
            {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            for task in tasks if task['userId'] == user_id
        ]
        data[user_id] = user_tasks
    
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    main()
