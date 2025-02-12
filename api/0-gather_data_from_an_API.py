#!/usr/bin/python3
import sys
import requests

def fetch_employee_todo_list(employee_id):
    """
    Fetches the TODO list for a given employee ID from the REST API.

    Args:
        employee_id (int): The ID of the employee to fetch the TODO list for.

    Returns:
        list: A list of dictionaries representing the TODO tasks if successful, or None if an error occurs.
    """
    # URL of the REST API that provides employee data
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    # Send a GET request to the API
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        print("Error fetching data.")
        return None
    
    # Return the JSON response, which contains the TODO list
    return response.json()

def fetch_employee_name(employee_id):
    """
    Fetches the name of an employee given their employee ID from the REST API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        str: The employee's name if successful, or None if an error occurs.
    """
    # URL to fetch the employee's details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    
    # Send a GET request to fetch employee data
    employee_response = requests.get(employee_url)
    
    # Check if the request was successful
    if employee_response.status_code != 200:
        print("Error fetching empl
