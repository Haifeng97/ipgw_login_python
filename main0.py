import urllib.request
import urllib.parse
import json
#先parse 再bytes

def http_post():
    url = "http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1&"
    postdata =dict(action = "login", username = "20154398" , password = "970228")
    req = urllib.request.Request(url)
    data = bytes(urllib.parse.urlencode(postdata),'utf-8')
    #data = bytes(json.dumps(postdata),'utf-8')
    req = urllib.request.Request(url, data)
    req.add_header("accept", "*/*")
    req.add_header("connection", "Keep-Alive")
    req.add_header("user-agent","Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)")
    response = urllib.request.urlopen(req)
    result = response.read().decode('utf-8')
    print (result)
    print(data)


if __name__ == '__main__':
    http_post()
