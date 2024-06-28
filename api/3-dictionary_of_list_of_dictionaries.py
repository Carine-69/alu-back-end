#!/usr/bin/python3
"""Script that gets user data (Todo list) from API
and then exports the result to a JSON file."""

import json
import requests


def main():
    """Main function"""
    todo_url = 'https://jsonplaceholder.typicode.com/todos'

    response = requests.get(todo_url)
    if response.status_code != 200:
        print("Error: Unable to fetch data from the API")
        return

    output = {}

    for todo in response.json():
        user_id = todo.get('userId')
        if user_id not in output:
            output[user_id] = []
            user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
            user_name_response = requests.get(user_url)
            if user_name_response.status_code != 200:
                print("Error: Unable to fetch user data from the API")
                return
            user_name = user_name_response.json().get('username')
        
        output[user_id].append({
            "username": user_name,
            "task": todo.get('title'),
            "completed": todo.get('completed')
        })

    with open("todo_all_employees.json", 'w') as file:
        json.dump(output, file)


if __name__ == '__main__':
    main()
