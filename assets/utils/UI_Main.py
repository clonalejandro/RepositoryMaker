# -*- coding=utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

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
# * All rights reserved for clonalejandro ©Repository 2017 / 2018
# */


class UI_Main(object):

    # SMALL CONSTRUCTORS (NONE)
    # REST
    def setupUi(self, MainWindow):
        self.__setupWindow(MainWindow)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setMouseTracking(False)
        self.centralWidget.setObjectName("centralWidget")
        self.__artifactField()
        self.__groupField()
        self.__versionField()
        self.__fileDropper()
        self.__submit()
        self.__menuBar(MainWindow)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RepositoryMaker"))
        self.artifactId.setPlaceholderText(_translate("MainWindow", " artifactId"))
        self.groupId.setPlaceholderText(_translate("MainWindow", " groupId"))
        self.version.setPlaceholderText(_translate("MainWindow", " version"))
        # self.toolButton.setText(_translate("MainWindow", "..."))
        self.pushButton.setText(_translate("MainWindow", "Make a repo"))

    # OTHERS
    def __setupWindow(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 400)
        MainWindow.setMouseTracking(True)

    def __artifactField(self):
        self.artifactId = QtWidgets.QLineEdit(self.centralWidget)
        self.artifactId.setGeometry(QtCore.QRect(190, 140, 261, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.artifactId.sizePolicy().hasHeightForWidth())
        self.artifactId.setSizePolicy(sizePolicy)
        self.artifactId.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.artifactId.setAcceptDrops(False)
        self.artifactId.setToolTip("")
        self.artifactId.setAutoFillBackground(False)
        self.artifactId.setStyleSheet("border-radius: 13px;\n""text-align: center;")
        self.artifactId.setInputMask("")
        self.artifactId.setText("")
        self.artifactId.setFrame(True)
        self.artifactId.setCursorPosition(0)
        self.artifactId.setDragEnabled(True)
        self.artifactId.setClearButtonEnabled(True)
        self.artifactId.setObjectName("artifactId")

    def __groupField(self):
        self.groupId = QtWidgets.QLineEdit(self.centralWidget)
        self.groupId.setGeometry(QtCore.QRect(190, 90, 261, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupId.sizePolicy().hasHeightForWidth())
        self.groupId.setSizePolicy(sizePolicy)
        self.groupId.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.groupId.setAcceptDrops(False)
        self.groupId.setToolTip("")
        self.groupId.setAutoFillBackground(False)
        self.groupId.setStyleSheet("border-radius: 13px;")
        self.groupId.setInputMask("")
        self.groupId.setText("")
        self.groupId.setFrame(True)
        self.groupId.setDragEnabled(True)
        self.groupId.setClearButtonEnabled(True)
        self.groupId.setObjectName("groupId")

    def __versionField(self):
        self.version = QtWidgets.QLineEdit(self.centralWidget)
        self.version.setGeometry(QtCore.QRect(190, 190, 261, 29))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.version.sizePolicy().hasHeightForWidth())
        self.version.setSizePolicy(sizePolicy)
        self.version.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.version.setAcceptDrops(False)
        self.version.setToolTip("")
        self.version.setAutoFillBackground(False)
        self.version.setStyleSheet("border-radius: 13px;")
        self.version.setInputMask("")
        self.version.setText("")
        self.version.setFrame(True)
        self.version.setDragEnabled(True)
        self.version.setClearButtonEnabled(True)
        self.version.setObjectName("version")

    def __fileDropper(self):
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(560, 0, 81, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolButton = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.toolButton.setMouseTracking(True)
        self.toolButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.toolButton.setAcceptDrops(True)
        self.toolButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolButton.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./assets/img/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(64, 64))
        self.toolButton.setAutoRaise(True)
        self.toolButton.setArrowType(QtCore.Qt.NoArrow)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout.addWidget(self.toolButton)

    def __submit(self):
        self.pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 260, 251, 31))
        self.pushButton.setMouseTracking(True)
        self.pushButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("background: qlineargradient(spread:pad, x1:0.507222, y1:0.982955, x2:0.492611, "
                                      "y2:0, stop:0 rgba(251, 194, 235, 200), stop:1 rgba(166, 193, 238, "
                                      "200));\n" "border-radius: 15px;\n" "font: 14pt \"Apple SD Gothic Neo\";")
        self.pushButton.setIconSize(QtCore.QSize(16, 16))
        self.pushButton.setObjectName("pushButton")

    def __menuBar(self, MainWindow):
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 639, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
