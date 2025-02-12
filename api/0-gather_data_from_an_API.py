#!/usr/bin/python3

import requests
import sys

def gather_data(employee_id):
    """
    Fetches and prints employee's TODO list progress.
    
    Parameters:
        employee_id (int): The employee's ID.
    """
    # URLs for the user and todo list API
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'

    # Fetch user details
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("User not found")
        return

    # Get employee name
    user_data = user_response.json()
    employee_name = user_data['name']

    # Fetch TODO list details
    todo_response = requests.get(todo_url)
    if todo_response.status_code != 200:
        print("Failed to retrieve TODO list")
        return

    todos = todo_response.json()
    completed_tasks = [task['title'] for task in todos if task['completed']]
    total_tasks = len(todos)

    # Print employee's progress
    print(f'Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):')
    for task in completed_tasks:
        print(f'\t {task}')

if __name__ == '__main__':
    """
    Main function to get employee ID and fetch their TODO progress.
    
    Usage:
    python3 0-gather_data_from_an_API.py <employee_id>
    """
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys
