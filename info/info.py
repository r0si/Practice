#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import sys
import os
from rich.console import Console
if sys.version_info < (3, 7):
    sys.stdout.write("Sorry, info requires Python 3.7 or higher\n")
    sys.exit(1)
console = Console()
INFO_COOL_LOOKING = '''
!    __      _____  ___     _______      ______    
!   |" \    (\"   \|"  \   /"     "|    /    " \   
!   ||  |   |.\\   \    | (: ______)   // ____  \  
!   |:  |   |: \.   \\  |  \/    |    /  /    ) :) 
!   |.  |   |.  \    \. |  // ___)   (: (____/ //  
!   /\  |\  |    \    \ | (:  (       \        /   
!  (__\_|_)  \___|\____\)  \__/        \"_____/    
!                                                  
    '''


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u',
                        '--url',
                        type=str,
                        help='This is the url to scan')
    return parser


def get_parsed_args(parser, args):
    args_parsed = parser.parse_args(args)
    return args_parsed


def url_scan(url):
    pass


if __name__ == '__main__':
    console.print(INFO_COOL_LOOKING, style="bold red")
    parser = get_parser()
    args = get_parsed_args(parser, sys.argv[1:])
    if args.url:
        url_scan(args.url[0])
