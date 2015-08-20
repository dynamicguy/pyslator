# -*- coding: utf-8 -*-
# !/usr/bin/env python


__author__ = 'ferdous'

import optparse
import os
from os.path import join, getsize


def run(folder):
    print('reading folder: ' + folder)
    for root, dirs, files in os.walk(folder):
        print(root, "consumes", end=" ")
        print(sum(getsize(join(root, name)) for name in files), end=" ")
        print("bytes in", len(files), "non-directory files")
        for file in files:
            body = open(folder + '/' + file).readline()
            print(body)


if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("-d", "--directory", metavar="DIR", help="Directory to scan for image files")

    opts, args = parser.parse_args()
    print('scanning directory: ', opts.directory)
    run(opts.directory)
