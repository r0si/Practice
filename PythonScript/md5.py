import requests
import hashlib
import re

req = requests.session()
url = "http://167.99.85.197:32033/"

rget = req.get(url)
html = rget.content

def html_tags(html):
    clean = re.compile('<.*?>')
    return re.sub(clean, '',html)

out1 = html_tags(html)
out2 = out1.split('string')[1]
out3 = out2.rstrip()

mdHash = hashlib.md5(out3).hexdigest()

data = dict(hash=mdHash)
rpost = req.post(url=url,data=data)

print(rpost.text)
