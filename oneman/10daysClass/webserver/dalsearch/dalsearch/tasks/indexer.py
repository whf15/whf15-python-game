# coding=utf-8

"""A Simple Indexer
Author: Js
Python Version: 3.6+

Changes:
--------

"""


def add_to_index(index, keyword, info):
    """
    for each keyword, we can create indexer
    :param index:
    :param keyword:
    :param info:
    :return:
    """
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(info)
            return
    index.append([keyword, [info]])


def lookup(index,keyword):
    """
    simple lookup function for testing purpose
    :param index:
    :param keyword:
    :return:
    """
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return entry[0]