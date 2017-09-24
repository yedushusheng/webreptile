import urllib3
import re
import urllib.request

req = urllib3.request.urlopen('http://www.imooc.com/course/list')
buf = req.read()
buf = buf.decode('utf-8')
listurl = re.findall(r'src=.+\.jpg',buf)
print(buf)