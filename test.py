import json
import urllib.request
import urllib.parse
import time, struct, sys, re

"""postdata =dict(action = "login", username = "20154398" , password = "970228")
jsoned = json.dumps(postdata)
print(jsoned)
encoded = urllib.parse.urlencode(postdata)
print(encoded)
bed = bytes(encoded, 'utf-8')
print(bed)"""
m, s = divmod(1368232, 60)
h, m = divmod(m, 60)
#print ("%02d:%02d:%02d" % (h, m, s))
b = b'42026532482,1368232,34.14,,0,118.202.41.236'
b2 = b
print(b.decode('utf-8'))
b = b.decode('utf-8')
b.split(',')
print(b)
pattern = re.compile(r'[\d*.*,]*')
match = pattern.match('42026532482,1368232,34.14,,0,118.202.41.236')
if match:
    print(match.group())
b = b.split(',')
print(b)