#!/usr/bin/python3
"""
This script fetches TODO list progress for a given employee from a REST API and
exports the data in CSV format.

It accepts an employee ID as an argument and retrieves the corresponding TODO list
information. It records all tasks for that employee in a CSV file.

Usage:
    python3 1-export_to_CSV.py <employee_id>

Requirements:
    - The script uses the `requests` library to make HTTP requests.
    - The script must be run on Ubuntu 14.04 LTS with Python 3.4.3.
    - The employee ID must be an integer passed as a command-line argument.
"""

import csv
import requests
import sys


def gather_and_export_data(employee_id):
    """
    Fetches the TODO list progress for the given employee ID, and exports it
    to a CSV file.

    Arguments:
        employee_id (int): The ID of the employee whose TODO list is to be fetched.

    The function makes two API requests:
    - One to fetch the employee's TODO list.
    - One to fetch the employee's user details (name).
    Then, it calculates the number of completed tasks and writes the data to a CSV file.
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

    # Get employee name (using a second API call to get user details)
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print("Failed to retrieve user data")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Prepare the CSV filename
    filename = f"{employee_id}.csv"

    # Open the CSV file for writing
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # Write the header row
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write each task's details to the CSV file
        for task in todos:
            writer.writerow([employee_id, employee_name, task['completed'], task['title']])

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    # Ensure the script is run with an integer as a parameter
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        gather_and_export_data(employee_id)
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)
