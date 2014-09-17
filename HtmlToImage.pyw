# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui, QtWebKit, QtNetwork


class MainWindow(QtGui.QMainWindow):
    def __init__(self, url):
        super(MainWindow, self).__init__()

        #网页内容
        self.view = QtWebKit.QWebView()
        self.view.load(url)
        self.webpage = self.view.page()
        #self.view.loadFinished.connect(self.ExportImage)


        #地址栏
        self.addressEdit = QtGui.QLineEdit(self)
        self.addressEdit.setSizePolicy(QtGui.QSizePolicy.Expanding,
                                       self.addressEdit.sizePolicy().verticalPolicy())
        self.addressEdit.returnPressed.connect(self.ChangeAddress)

        #添加工具栏
        toolbar = self.addToolBar("Navigation")
        toolbar.addAction(self.view.pageAction(QtWebKit.QWebPage.Back))
        toolbar.addAction(self.view.pageAction(QtWebKit.QWebPage.Forward))
        toolbar.addAction(self.view.pageAction(QtWebKit.QWebPage.Reload))
        toolbar.addAction(self.view.pageAction(QtWebKit.QWebPage.Stop))
        #地址栏加入工具栏
        toolbar.addWidget(self.addressEdit)

        #菜单栏（File）
        file_menu = self.menuBar().addMenu("&File")
        export_img_action = QtGui.QAction("Export", self)
        export_img_action.triggered.connect(self.ExportImage)
        file_menu.addAction(export_img_action)

        #菜单栏（About）
        about_menu = self.menuBar().addMenu("&File")
        about_Qt_action = QtGui.QAction("About Qt", self)
        about_Qt_action.triggered.connect(QtGui.qApp.aboutQt)
        about_menu.addAction(about_Qt_action)

        self.setCentralWidget(self.view)
        self.setWindowTitle(QtCore.QString("HTML TO IMAGE"))
        #最小浏览器大小
        #self.setMinimumSize(1000, 800)

    #地址栏变化action
    def ChangeAddress(self):
        self.view.load(QtCore.QUrl.fromUserInput(self.addressEdit.text()))
        #self.view.setFocus()

    def ExportImage(self):
        #设置图片保存路径
        file_name = QtGui.QFileDialog().getSaveFileName()

        if file_name:
            self.saveImage(file_name)

    #保存图片到指定内容
    def saveImage(self, filename):
        size = self.webpage.mainFrame().contentsSize()
        img = QtGui.QImage(size, QtGui.QImage.Format_ARGB32)
        painter = QtGui.QPainter(img)
        self.webpage.setViewportSize(QtCore.QSize(size.width(), size.height()))
        self.webpage.mainFrame().render(painter)
        painter.end()
        img.save(filename)

    #关于本程序
    def about(self):
        QtGui.QMessageBox.about(self, "HTML TO IMAGE",
                "This <b>HTML TO IMAGE</b> demonstrates how to convert html"
                "to a long iamge file.")

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    if len(sys.argv) > 1:
        url = QtCore.QUrl(sys.argv[1])
    else:
        url = QtCore.QUrl('http://www.baidu.com')
    browser = MainWindow(url)
    browser.show()
    sys.exit(app.exec_())