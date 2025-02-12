#!/usr/bin/python3
"""
A script that fetches an employee's TODO list progress from a REST API.
"""

import requests
import sys

def fetch_todo_list(employee_id):
    """Fetches and displays TODO list progress for a given employee ID."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"
    
    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)
    
    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data")
        return
    
    user_data = user_response.json()
    todos_data = todos_response.json()
    
    employee_name = user_data.get("name")
    total_tasks = len(todos_data)
    completed_tasks = [task["title"] for task in todos_data if task.get("completed")]
    
    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
    
    fetch_todo_list(employee_id)
