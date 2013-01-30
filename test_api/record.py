# coding: utf-8

import argparse


def record(url, py_filepath):
    with open(py_filepath, 'w') as py_file:
        py_file.write('ok')
        