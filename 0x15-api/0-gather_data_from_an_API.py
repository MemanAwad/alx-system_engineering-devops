#!/usr/bin/python3
""" Take the employee id and returuns its TODO list"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params=("userId:" sys.argv[1]}).json()

    c_task = [td.get("title") for td in todos if td.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name", len(c_task), len(todos))))
    [print("\t {}".format(ti)) for ti in c_task]
