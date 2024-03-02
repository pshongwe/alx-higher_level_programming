#!/usr/bin/python3
"""Sends a POST request with an email parameter
and displays the response body."""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
