#!/usr/bin/python3
"""Sends a request to a URL and displays the body
of the response or an error code."""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
