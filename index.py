from PyQt5.QtWidgets import *
import socket
from lib import admin
import Dorkmain
import sys
import time
import scan
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.uic import loadUiType


ui, _ = loadUiType('mainUI.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handle_ui_change()
        self.handle_buttons()
        self.about()
        self.ip_address()
        self.get_thread = ThreadAdmin()
        self.get_thread1 = ThreadDork()
        self.get_thread_scan = ThreadScan()


    ########## Handling GUI ############
    def handle_ui_change(self):
        self.hide_theme()
        self.tabWidget.tabBar().setVisible(False)


    ######### Handling Buttons ############
    def handle_buttons(self):
        self.themesButton.clicked.connect(self.show_theme)
        self.hideButton.clicked.connect(self.hide_theme)
        self.homeButton.clicked.connect(self.open_home)
        self.adminButton.clicked.connect(self.open_admin)
        self.uploadButton.clicked.connect(self.open_upload)
        self.aboutButton.clicked.connect(self.open_about)
        self.theme1button.clicked.connect(self.theme_darkorange)
        self.theme2button.clicked.connect(self.theme_light)
        self.theme3button.clicked.connect(self.theme_grey)
        self.theme4button.clicked.connect(self.theme_blue)
        self.adminButton_2.clicked.connect(self.admin_finder)
        self.AdminClearBtn.clicked.connect(self.clear_admin_result)
        self.pushButton_2.clicked.connect(self.dork_finder)
        self.pushButton_7.clicked.connect(self.clear_dork)
        self.pushButton_4.clicked.connect(self.Uscript)
        self.pushButton_5.clicked.connect(self.Ascript)
        self.pushButton.clicked.connect(self.vulnerability_scan)
        self.pushButton_6.clicked.connect(self.clear_scan_result)


    def Ascript(self):
        QMessageBox.question(self,'Admin Script', "Sucessfully Uploaded", QMessageBox.Ok)

    def Uscript(self):
        QMessageBox.question(self, 'Upload Script', "Sucessfully Uploaded", QMessageBox.Ok)



    ######## Themes Changing #############
    def show_theme(self):
        self.themegroupBox.show()

    def hide_theme(self):
        self.themegroupBox.hide()

    ###theme ui
    def theme_darkorange(self):
        style = open('themes/DarkOrange.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def theme_light(self):
        style = open('themes/light.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def theme_grey(self):
        style = open('themes/grey.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    def theme_blue(self):
        style = open('themes/san.css', 'r')
        style = style.read()
        self.setStyleSheet(style)

    ############ Openning Tabs ###########
    def open_home(self):
        self.tabWidget.setCurrentIndex(0)

    def open_admin(self):
        self.tabWidget.setCurrentIndex(1)

    def open_upload(self):
        self.tabWidget.setCurrentIndex(2)

    def open_about(self):
        self.tabWidget.setCurrentIndex(3)

    ######## Admin _finder ######
    def admin_finder(self):
        self.textBrowser_2.setPlainText("Please Wait While searching ... \n")
        self.get_thread.git_url = self.lineEdit_3.text()
        self.get_thread.start()
        self.get_thread.finished.connect(self.show_admin_result)


    def show_admin_result(self):
        txt = open('Admins.txt').read()
        self.textBrowser_2.setPlainText(txt)

    def clear_admin_result(self):
        self.textBrowser_2.setPlainText("")

    ####### Dork FInder #########
    def dork_finder(self):
        self.textBrowser_3.setPlainText(":::   Please Wait While scanning   :::\n")
        self.get_thread1.start()
        self.get_thread1.finished.connect(self.show_dork_result)


    def show_dork_result(self):
        txt = open('sql_vuln.txt').read()
        self.textBrowser_3.setPlainText(txt)

    def clear_dork(self):
        self.textBrowser_3.setPlainText("")

    ####### about #########
    def about(self):
        text = open('about.txt').read()
        self.textBrowser.setPlainText(text)

    ####### Host Name & Ip Address #########
    def ip_address(self):
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        self.label_11.setText(host)
        self.label_13.setText(ip)

    ########Vulnerability###############
    def vulnerability_scan(self):
        self.textBrowser_4.setPlainText("Please Wait While Scanning ... \n")
        scan.get_link = self.lineEditx.text()
        self.get_thread_scan.start()
        self.get_thread_scan.finished.connect(self.show_scan_result)



    def show_scan_result(self):
        txt = open('scan.txt').read()
        self.textBrowser_4.setPlainText(txt)

    def clear_scan_result(self):
        self.textBrowser_4.setPlainText("")


class ThreadScan(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        start = time.time()
        scan.start()
        end = time.time()
        print("Execution time:")
        print(end - start)




class ThreadAdmin(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)
        self.git_url = ""

    def __del__(self):
        self.wait()

    def run(self):
        start2 = time.time()
        admin.url = self.git_url
        admin.find()
        end2 = time.time()
        print("Execution time:")
        print(end2 - start2)


class ThreadDork(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def scan(self):
        scan.start()

    def run(self):
        start1 = time.time()
        Dorkmain.start()
        end1 = time.time()
        print("Execution time:")
        print(end1 - start1)


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()


