########Vulnerability###############
def vulnerability_scan(self):
    self.textBrowser_4.setPlainText("Please Wait While Scanning ... \n")
    self.get_thread2.get_link = self.lineEdit.text()
    self.get_thread2.start()
    self.get_thread2.finished.connect(self.show_scan_result)


def show_scan_result(self):
    txt = open('scan.txt').read()
    self.textBrowser_4.setPlainText(txt)


def clear_scan_result(self):
    self.textBrowser_4.setPlainText("")




class ThreadScan(QThread):
    signal = pyqtSignal('PyQt_PyObject')

    def __init__(self):
        QThread.__init__(self)
        self.get_link = ""

    def __del__(self):
        self.wait()

    def run(self):
       main.start(self.get_link)
