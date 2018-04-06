#!/usr/bin/python3
""" Algorithm to find_peak """


def find_peak(list_of_integers):
    """ Function to find peak in an array of ints """
    if list_of_integers is None or len(list_of_integers) is 0:
        return None
    for i in range(len(list_of_integers)):
        if i == 0:
            if list_of_integers[i] > list_of_integers[i + 1]:
                return list_of_integers[i]
        elif i == len(list_of_integers) - 1:
            if list_of_integers[i] > list_of_integers[i - 1]:
                return list_of_integers[i]
        else:
            if list_of_integers[i] > list_of_integers[i + 1]\
                    and list_of_integers[i] > list_of_integers[i - 1]:
                return list_of_integers[i]
    return list_of_integers[0]
