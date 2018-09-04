import sys
import re, time
import urllib.parse
from main0 import http_post
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui import Ui_MainWindow

class Myform(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.logout)
        self.pushButton_2.clicked.connect(self.pc)
        self.pushButton.clicked.connect(self.phone)
        self.pushButton_4.clicked.connect(self.test)

    def data(self, a):
        account = self.lineEdit.text()
        password = self.lineEdit_2.text()
        self.textEdit.setText(account + password)
        if a == 1:
            d = {'action': 'login', 'username': account, 'password': password}
        else:
            d = {'action': 'logout', 'username': account, 'password': password}
        en = urllib.parse.urlencode(d)
        return bytes(en, 'utf-8')

    def test(self):
        data = {"action": "get_online_info"}
        en = urllib.parse.urlencode(data)
        data = bytes(en, 'utf-8')
        url = "http://ipgw.neu.edu.cn/include/auth_action.php?k=32187"
        req = urllib.request.Request(url, data)
        response = urllib.request.urlopen(req)
        result = response.read()
        print(result)

    def post1(self, a):
        url = "http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1&"
        if a == 1:
            req = urllib.request.Request(url, self.data(1))
        else:
            req = urllib.request.Request(url, self.data(2))
        req.add_header("accept", "*/*")
        req.add_header("connection", "Keep-Alive")
        req.add_header("user-agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36)")
        response = urllib.request.urlopen(req)
        result = response.read().decode('utf-8')
        return (result)

    def link2(self):
        data = {"action": "get_online_info"}
        en = urllib.parse.urlencode(data)
        data = bytes(en, 'utf-8')
        url = "http://ipgw.neu.edu.cn/include/auth_action.php?k=32187"
        req = urllib.request.Request(url, data)
        response = urllib.request.urlopen(req)
        result = response.read()
        b = result.decode('utf-8')
        b = b.split(',')
        self.lineEdit_6.setText(b[5])
        data_usage = str(b[0])
        data_usage = data_usage[:2] + '.' + data_usage[2:] + 'G'
        self.lineEdit_3.setText(data_usage)
        time_using = int(b[1])
        m, s = divmod(time_using, 60)
        h, m = divmod(m, 60)
        time_using = str(h) + ':' + str(m) + ':' + str(s)
        self.lineEdit_4.setText(time_using)
        self.lineEdit_5.setText(b[2])



    def pc(self):
        self.textEdit.setText(self.post1(1))
        self.label_3.setText("网络已连接")
        time.sleep(0.3)
        self.link2()


    def logout(self):
        self.textEdit.setText(self.post1(2))

    """def re1(self, a):
        result = re.match("<td height="40" style="font-weight:bold;color:orange;">(.*?)</td>(.*?)<p>(.*?)</p>", a)
        print(result)"""

    def phone(self):
        account = self.lineEdit.text()
        password = self.lineEdit_2.text()
        url = "http://ipgw.neu.edu.cn/srun_portal_pc.php?ac_id=1&"
        d = {'action': 'login', 'username': account, 'password': password}
        data = bytes(urllib.parse.urlencode(d), 'utf-8')
        req = urllib.request.Request(url, data)
        req.add_header("accept", "*/*")
        req.add_header("connection", "Keep-Alive")
        req.add_header("user-agent", "Mozilla/5.0 (iPhone 84; CPU iPhone OS 10_3_3 like Mac OS X) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.0 MQQBrowser/7.8.0 Mobile/14G60 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1")
        response = urllib.request.urlopen(req)
        result = response.read().decode('utf-8')
        self.textEdit.setText(result)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Myform()
    w.show()
    app.exec_()