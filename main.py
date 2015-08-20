#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple command-line tool for Translate.
Command-line application that translates some text.
"""
from __future__ import print_function

__author__ = 'nurul@ferdous (Nurul Ferdous)'

import json
import argparse
from googleapiclient.discovery import build


def call_api(q, src_lang, target_lang):
    service = build('translate', 'v2', developerKey='CHANGE_ME')
    print(service.translations().list(
        source=src_lang,
        target=target_lang,
        q=q
    ).execute())


def read_data(d):
    for k, v in d.items():
        if isinstance(v, dict):
            read_data(v)
        else:
            # print(v)
            print("{0} => {1}".format(k, v))
            # call_api(v)


def do_translate(args):
    print('reading folder: ' + args.file)
    data = json.load(open(args.file))
    read_data(data)


def run(args):
    answer = do_translate(args)
    if args.quiet:
        print(answer)
    elif args.verbose:
        print("{} to the power {} equals {}".format(args.file, args.lang, answer))
    else:
        print("{}^{} == {}".format(args.file, args.lang, answer))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="calculate X to the power of Y")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    group.add_argument("-q", "--quiet", action="store_true", help="run quietly")
    parser.add_argument("file", type=str, help="file that need to be translated")
    parser.add_argument("lang", type=str, help="to which language it need to translated")
    args = parser.parse_args()


    # parser = argparse.ArgumentParser()
    # parser.add_argument("file", type=str, help="file that need to be translated")
    # parser.add_argument("lang", type=str, help="to which language it need to translated")
    # parser.add_argument("-v", "--verbose", action="store_true", help="increase output verbosity")
    # args = parser.parse_args()
    run(args)
