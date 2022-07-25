from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from PyQt5 import QtWidgets

import MainUi


# 이거 로그인 페이로 옮기기, 로그인 페이지가 메인 페이지임 !! 

class Main:
    def __init__(self):
        self.ui=MainUi.MainUi()

if __name__=="__main__":
    app = QtWidgets.QApplication(sys.argv) # gui 시작

    main=Main() # Main page Logic Class 를 객체로 만들어주는 줄
    main.show()

    sys.exit(app.exec_()) # gui 종료