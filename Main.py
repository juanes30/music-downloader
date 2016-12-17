import sys

from Login import Login
from ui.Dashboard import *

__author__ = "Juan Esteban Londoño Tabares"


if __name__ == "__main__":
    app_music = QtGui.QApplication(sys.argv)
    frm_login = Login()
    frm_login.show()
    sys.exit(app_music.exec_())
