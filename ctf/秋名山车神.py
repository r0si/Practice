#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
s = requests.Session()
r = s.get("http://114.67.246.176:11298/")
searchObj = re.search(r'^<div>(.*)=\?;</div>$', r.text, re.M | re.S)
d = {"value": eval(searchObj.group(1))}
r = s.post("http://114.67.246.176:11298/", data=d)
print(r.text)
