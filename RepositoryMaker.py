# -*- coding=utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from assets.utils.Process import Process
from assets.utils.UI_Main import *
import urllib.request

# /**
# * Created by alejandrorioscalera
# * On 21/9/17
# *
# * -- SOCIAL NETWORKS --
# *
# * GitHub: https://github.com/clonalejandro or @clonalejandro
# * Website: https://clonalejandro.me/
# * Twitter: https://twitter.com/clonalejandro11/ or @clonalejandro11
# * Keybase: https://keybase.io/clonalejandro/
# *
# * -- LICENSE --
# *
# * All rights reserved for clonalejandro ©RepositoryMaker 2017 / 2018
# */


class RepositoryMaker(Process, QMainWindow, UI_Main):

    # SMALL CONSTRUCTORS

    def __init__(self, parent=None):
        self.__ui = super(RepositoryMaker, self).__init__(parent)
        self.setupUi(self)
        self.jar = "poop"
        self.toolButton.clicked.connect(lambda: self.__uploadFile())  # Event Uploader
        self.show()

    def __onClick(self, jar, group, artifact, version):
        process = Process
        process.makeRepo(self, jar, group, artifact, version)
        print("END")

    def __uploadFile(self):
        j = self.jar; g = self.groupId.text(); a = self.artifactId.text(); v = self.version.text()
        self.jar = str(QFileDialog.getOpenFileName(QWidget.__init__(self), 'Open File', '.')).replace("(\'", "").replace("\', \'All Files (*)\')", "").replace(Process.config(self)['raid'], "")
        j = self.jar
        self.pushButton.clicked.connect(lambda: self.__onClick(j, g, a, v))  # Event Submit

    def __configureWindow(self):
        self.setWindowTitle("RepositoryMaker")
        self.setWindowIconText("RepositoryMaker")
        icon = QtGui.QIcon()
        # ARRAY IMAGES
        path = ['https://i.imgur.com/IBWf2jb.png', 'https://i.imgur.com/Wd8xfkM.png', 'https://i.imgur.com/EcESpz7.png', 'https://i.imgur.com/nfLwmKk.png', 'https://i.imgur.com/SQVDMRf.png', 'https://i.imgur.com/C1erbU6.png', 'https://i.imgur.com/O0haNwj.png']
        # REQUEST
        a = urllib.request.urlopen(path[0]).read(); b = urllib.request.urlopen(path[1]).read(); c = urllib.request.urlopen(path[2]).read(); d = urllib.request.urlopen(path[3]).read(); e = urllib.request.urlopen(path[4]).read(); f = urllib.request.urlopen(path[5]).read(); g = urllib.request.urlopen(path[6]).read()
        aa = QtGui.QImage(); bb = QtGui.QImage(); cc = QtGui.QImage(); dd = QtGui.QImage(); ee = QtGui.QImage(); ff = QtGui.QImage(); gg = QtGui.QImage()
        aa.loadFromData(a); bb.loadFromData(b); cc.loadFromData(c); dd.loadFromData(d); ee.loadFromData(e); ff.loadFromData(f); gg.loadFromData(g)
        # IMAGES
        icon.addFile(aa, QtCore.QSize(16, 16))
        icon.addFile(bb, QtCore.QSize(24, 24))
        icon.addFile(cc, QtCore.QSize(32, 32))
        icon.addFile(dd, QtCore.QSize(48, 48))
        icon.addFile(ee, QtCore.QSize(64, 64))
        icon.addFile(ff, QtCore.QSize(128, 128))
        icon.addFile(gg, QtCore.QSize(256, 256))
        # OTHERS
        self.setWindowIcon(icon)
        self.setWindowOpacity(0.9)


# RUNNER

if __name__ == "__main__":

    app = QApplication(sys.argv)
    Window = RepositoryMaker()
    sys.exit(app.exec_())
