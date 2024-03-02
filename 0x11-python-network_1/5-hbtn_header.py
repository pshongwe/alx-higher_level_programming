#!/usr/bin/python3
"""Fetches the value of the X-Request-Id variable from a response header."""


if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
