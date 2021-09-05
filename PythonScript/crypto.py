#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import base64

def eb64(code):
    print(base64.b64encode(code))
def db64(code):
    print(base64.b64decode(code))
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="各种骚B编码")
    parser.add_argument('-eb64',type=str,help='base64编码')
    parser.add_argument('-db64',type=str,help='base64解码')
    args = parser.parse_args()



