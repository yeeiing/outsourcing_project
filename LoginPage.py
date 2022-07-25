from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from PyQt5 import QtWidgets

import Database
import MainUi
import SignupPage, FindInfoPage, VideoPage

class LoginPage:
    def __init__(self):
        self.loginPage=QMainWindow()

        # 객체 여기서 한번만 생성
        self.ui=MainUi.MainUi()
        self.db=Database.Database()

        self.signup=SignupPage.SignupPage(self.ui,self.db)

        # # 버튼, 이동 페이지 연결 
        # self.ui.loginPageFindInfoBtn.clicked.connect(self.goFindInfo)
        # self.ui.loginPageSignupBtn.clicked.connect(self.goSignup)

        # for index in range(0,len(self.ui.mainPageBtnList)):
            
        #     self.ui.mainPageBtnList[index].clicked.connect(lambda event, nowIndex=index : self.moveEvent(event,nowIndex))
        #     self.ui.mainPageBtnList[index].enterEvent = lambda event, nowIndex=index : self.enterEvent(event,nowIndex)
        #     self.ui.mainPageBtnList[index].leaveEvent = lambda event, nowIndex=index : self.leaveEvent(event,nowIndex)


    # === 이벤트 함수 생성 ===

    # 페이지 이동 함수
    def moveEvent(self,event,index):
        if index == 0:
            self.ui.stackedWidget.setCurrentWidget(self.ui.PlaylistPage)
                
        elif index == 1:
            self.ui.stackedWidget.setCurrentWidget(self.ui.FindInfoPage)

        elif index == 2:
            self.ui.stackedWidget.setCurrentWidget(self.ui.SignupPage)


    def enterEvent(self,event,index):
        self.ui.mainPageBtnList[index].setStyleSheet(
            "background-color:white"
        )

    def leaveEvent(self,event,index):
        self.ui.mainPageBtnList[index].setStyleSheet(
           ( "background-color:#2E75B6; color:white; border-radius:10px;")
        )


    # # === 페이지 이동 함수 === 

    # def goFindInfo(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.FindInfoPage)

    # def goSignup(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.SignupPage)

    # def showRecord(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.RecordCheckPage)

    # def showRanking(self):
    #     self.ui.stackedWidget.setCurrentWidget(self.ui.RankingPage)

    def show(self):
        self.loginPage.show()

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv) # gui 시작

    loginPage=LoginPage() # Main page Logic Class 를 객체로 만들어주는 줄
    # loginPage.show()

    sys.exit(app.exec_()) # gui 종료