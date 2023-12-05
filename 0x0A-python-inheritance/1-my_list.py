#!/usr/bin/python3
""" my list """


class MyList(list):
    def print_sorted(self):
        """ Print the list in ascending order. """
        print(sorted(self))
