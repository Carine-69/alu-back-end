#!/usr/bin/python3
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetch and display the TODO list progress for a given employee ID
    """
    url_user = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    url_todos = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    
    user_response = requests.get(url_user)
    todos_response = requests.get(url_todos)
    
    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data from the API")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()
    
    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    number_of_done_tasks = len(done_tasks)
    
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    
    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
    
    get_employee_todo_progress(employee_id)

