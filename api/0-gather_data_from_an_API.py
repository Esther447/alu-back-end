#!/usr/bin/python3
"""
This script fetches TODO list progress for a given employee from a REST API.

It accepts an employee ID as an argument and retrieves the corresponding
TODO list information. It displays the employee's name, the number of completed
tasks, the total number of tasks, and the titles of the completed tasks.

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>

Requirements:
    - The script uses the `requests` library to make HTTP requests.
    - The script must be run on Ubuntu 14.04 LTS with Python 3.4.3.
    - The employee ID must be an integer passed as a command-line argument.
"""

import requests
import sys

def gather_data(employee_id):
    """
    Fetches the TODO list progress for the given employee ID and prints it
    in the specified format.

    Arguments:
        employee_id (int): The ID of the employee whose TODO list is to
                            be fetched.
    
    The function makes two API requests:
    - One to fetch the employee's TODO list.
    - One to fetch the employee's user details (name).
    Then, it calculates the number of completed tasks and displays them.
    """
    
    # Define the URL of the API endpoint
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    
    # Send GET request to the API
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to retrieve data")
        return
    
    # Parse the JSON response
    todos = response.json()
    
    # Filter the completed tasks
    completed_tasks = [task for task in todos if task['completed']]
    
    # Get employee name (using a second API call to get user details)
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    
    if user_response.status_code != 200:
        print("Failed to retrieve user data")
        return
    
    user_data = user_response.json()
    employee_name = user_data.get('name')
    
    # Print the employee's TODO list progress
    total_tasks = len(todos)
    done_tasks = len(completed_tasks)
    
    print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
    
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    # Ensure the script is run with an integer as a parameter
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        gather_data(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
