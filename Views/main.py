# coding:utf-8

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout
from qfluentwidgets import NavigationItemPosition,  SplitFluentWindow, SubtitleLabel, setFont, NavigationInterface, FluentWindow
from qfluentwidgets import FluentIcon as FIF

from Interfaces.MainInterface import MainInterface
from Interfaces.VersionsInterfaces.VersionListsInterface import VersionListInterface
from Interfaces.SettingsInterfaces.SettingsInterface import SettingsInterface

class Window(SplitFluentWindow):

    def __init__(self):
        super().__init__()

        # create sub interface
        self.HomeInterface = MainInterface()
        self.VersionsListInterface = VersionListInterface()
        self.SettingsInterface = SettingsInterface()
        self.stackedWidget.hBoxLayout.setContentsMargins(0, 40, 0, 0)
        self.initNavigation()
        self.initWindow()

    def initNavigation(self):
        self.addSubInterface(self.HomeInterface, FIF.HOME, '主页')
        self.navigationInterface.addSeparator()
        self.addSubInterface(self.VersionsListInterface, FIF.BOOK_SHELF, '版本列表')
        self.addSubInterface(self.SettingsInterface, FIF.SETTING, '设置', NavigationItemPosition.BOTTOM)

        # NOTE: enable acrylic effect
        # self.navigationInterface.setAcrylicEnabled(True)

    def initWindow(self):
        self.resize(1200, 750)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('Python Minecraft Launcher Beta')

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)
