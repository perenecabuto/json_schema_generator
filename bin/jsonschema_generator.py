#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import re

from json_schema_generator import Recorder, Validator


def record(args):
    rec = Recorder.from_url(args.json_source)
    rec.save_json_schema(args.json_schema_file_path, indent=4)


def validate(args):
    from urllib2 import urlopen

    json_data = urlopen(args.json_source).read()
    validator = Validator.from_path(args.json_schema_file_path)
    is_valid = validator.assert_json(json_data)

    if is_valid:
        print " * JSON is valid"
    else:
        print " ! JSON is broken "
        print validator.error_message


def homologate(args):
    print "homolotate"


def main():
    parser = argparse.ArgumentParser()

    default_parser = argparse.ArgumentParser(add_help=False)
    default_parser.add_argument('json_source', type=str, help='url or file')
    default_parser.add_argument('--path', dest='path', help='set path')

    subparsers = parser.add_subparsers(help='sub-command help')

    parser_record = subparsers.add_parser('record', parents=[default_parser])
    parser_record.add_argument('json_schema_file_path', type=str, help='json schema file path')
    parser_record.set_defaults(func=record)

    parser_validate = subparsers.add_parser('validate', parents=[default_parser])
    parser_validate.add_argument('json_schema_file_path', type=str, help='json schema file path')
    parser_validate.set_defaults(func=validate)

    parser_homologate = subparsers.add_parser('homologate', parents=[default_parser])
    parser_homologate.add_argument('homolation_name', type=str, help='json schema file path')
    parser_homologate.set_defaults(func=homologate)

    args = parser.parse_args()
    args.func(args)


if __name__ == '__main__':
    main()

