# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import urllib.request
from PyQt5 import QtCore, QtGui, QtWidgets
from os import environ       # environ 를 import 해야 아래 suppress_qt_warnings 가 정상 동작하니다
import json
import webbrowser

def suppress_qt_warnings():   # 해상도별 글자크기 강제 고정하는 함수
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"




class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(280, 52)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.google = QtWidgets.QPushButton(Form)
        self.google.setMinimumSize(QtCore.QSize(50, 0))
        self.google.setObjectName("google")
        self.horizontalLayout.addWidget(self.google)
        self.n1688_2 = QtWidgets.QPushButton(Form)
        self.n1688_2.setMinimumSize(QtCore.QSize(50, 0))
        self.n1688_2.setObjectName("n1688_2")
        self.horizontalLayout.addWidget(self.n1688_2)
        self.taobao = QtWidgets.QPushButton(Form)
        self.taobao.setMinimumSize(QtCore.QSize(50, 0))
        self.taobao.setObjectName("taobao")
        self.horizontalLayout.addWidget(self.taobao)
        self.ali = QtWidgets.QPushButton(Form)
        self.ali.setMinimumSize(QtCore.QSize(50, 0))
        self.ali.setObjectName("ali")
        self.horizontalLayout.addWidget(self.ali)
        self.rakuten = QtWidgets.QPushButton(Form)
        self.rakuten.setMinimumSize(QtCore.QSize(50, 0))
        self.rakuten.setObjectName("rakuten")
        self.horizontalLayout.addWidget(self.rakuten)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # event
        self.google.clicked.connect(self.google_url)
        self.n1688_2.clicked.connect(self.n1688_2_url)
        self.taobao.clicked.connect(self.taobao_url)
        self.ali.clicked.connect(self.ali_url)
        self.rakuten.clicked.connect(self.rakuten_url)

    def google_url(self):
        srcText = self.lineEdit.text()
        client_id = "j6V6dD6f1YCjncBEOBas"
        client_secret = "9E9BIJvIQ5"
        trantext_list = []
        encText = urllib.parse.quote(srcText)
        ########################### ch ####################################
        data = "source=ko&target=zh-CN&text=" + encText

        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(
            request, data=data.encode("utf-8"))
        rescode = response.getcode()
        response_body = response.read()
        # print(response_body.decode('utf-8'))

        # json 형 변환
        res = json.loads(response_body.decode('utf-8'))

        res = res['message']
        res = res['result']
        chtr = res['translatedText']
        url = "https://www.google.com/search?q=" + chtr + "&source=lnms&tbm=isch&sa"
        webbrowser.open(url)


    def n1688_2_url(self):
        srcText = self.lineEdit.text()
        client_id = "j6V6dD6f1YCjncBEOBas"
        client_secret = "9E9BIJvIQ5"
        trantext_list = []
        encText = urllib.parse.quote(srcText)
        ########################### ch ####################################
        data = "source=ko&target=zh-CN&text=" + encText

        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(
            request, data=data.encode("utf-8"))
        rescode = response.getcode()
        response_body = response.read()
        # print(response_body.decode('utf-8'))

        # json 형 변환
        res = json.loads(response_body.decode('utf-8'))

        res = res['message']
        res = res['result']
        chtr = res['translatedText']
        t = chtr.encode('EUC-CN')
        t = str(t)
        t = t.replace('\\x','%')
        chtr=t.split("'")[1]
        url = "https://s.1688.com/selloffer/offer_search.htm?keywords=" + chtr
        webbrowser.open(url)    

    def taobao_url(self):
        srcText = self.lineEdit.text()
        client_id = "j6V6dD6f1YCjncBEOBas"
        client_secret = "9E9BIJvIQ5"
        trantext_list = []
        encText = urllib.parse.quote(srcText)
        ########################### ch ####################################
        data = "source=ko&target=zh-CN&text=" + encText

        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(
            request, data=data.encode("utf-8"))
        rescode = response.getcode()
        response_body = response.read()
        # print(response_body.decode('utf-8'))

        # json 형 변환
        res = json.loads(response_body.decode('utf-8'))

        res = res['message']
        res = res['result']
        chtr = res['translatedText']
        url = "https://s.taobao.com/search?q=" + chtr
        webbrowser.open(url)            

    def ali_url(self):
        srcText = self.lineEdit.text()
        client_id = "j6V6dD6f1YCjncBEOBas"
        client_secret = "9E9BIJvIQ5"
        trantext_list = []
        encText = urllib.parse.quote(srcText)
        ########################### ch ####################################
        data = "source=ko&target=zh-CN&text=" + encText

        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(
            request, data=data.encode("utf-8"))
        rescode = response.getcode()
        response_body = response.read()
        # print(response_body.decode('utf-8'))

        # json 형 변환
        res = json.loads(response_body.decode('utf-8'))

        res = res['message']
        res = res['result']
        chtr = res['translatedText']
        url = "https://ko.aliexpress.com/af/%25E7%25A0%2582%25E6%2599%2582%25E8%25A8%2588.html?d=y&origin=n&SearchText=" + chtr
        webbrowser.open(url)        
        

    def rakuten_url(self):
        srcText = self.lineEdit.text()
        client_id = "j6V6dD6f1YCjncBEOBas"
        client_secret = "9E9BIJvIQ5"
        trantext_list = []
        encText = urllib.parse.quote(srcText)
        ########################### ch ####################################
        data = "source=ko&target=ja&text=" + encText

        url = "https://openapi.naver.com/v1/papago/n2mt"
        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)
        response = urllib.request.urlopen(
            request, data=data.encode("utf-8"))
        rescode = response.getcode()
        response_body = response.read()
        # print(response_body.decode('utf-8'))

        # json 형 변환
        res = json.loads(response_body.decode('utf-8'))

        res = res['message']
        res = res['result']
        chtr = res['translatedText']
   
        url = "https://search.rakuten.co.jp/search/mall/" + chtr
        webbrowser.open(url)    
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.google.setText(_translate("Form", "google"))
        self.n1688_2.setText(_translate("Form", "1688"))
        self.taobao.setText(_translate("Form", "taobao"))
        self.ali.setText(_translate("Form", "alliexpress"))
        self.rakuten.setText(_translate("Form", "rakuten"))


if __name__ == "__main__":
    import sys
    suppress_qt_warnings()
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
