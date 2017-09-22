# -*- coding=utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from assets.utils.Process import Process
from assets.utils.UI_Main import *

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


class RepositoryMaker(Process, QMainWindow, UI_Main):

    # SMALL CONSTRUCTORS

    def __init__(self, parent=None):
        super(RepositoryMaker, self).__init__(parent)
        self.setupUi(self)
        self.show()


# RUNNER

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = RepositoryMaker()
    sys.exit(app.exec_())
