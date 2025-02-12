#!/usr/bin/python3

import requests
import sys

def gather_data(employee_id):
    # Define the API URL to get user and TODOs
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    # Get the user data (employee name)
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found")
        return

    user_data = user_response.json()
    employee_name = user_data['name']

    # Get the TODO list data
    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print("Failed to retrieve TODO list")
        return

    todos = todo_response.json()

    # Count completed tasks
    completed_tasks = [task['title'] for task in todos if task['completed']]
    total_tasks = len(todos)

    # Print the result
    print(f'Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):')
    for task in completed_tasks:
        print(f'\t {task}')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        gather_data(employee_id)
    except ValueError:
        print("Employee ID should be an integer")
