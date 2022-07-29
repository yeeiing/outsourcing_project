from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

from PyQt5 import QtWidgets

import Database
import MainUi
import SignupPage, FindInfoPage, PlaylistPage, VideoPage

class LoginPage:
    def __init__(self):
        self.loginPage=QMainWindow()

        # 객체 여기서 한번만 생성
        self.ui=MainUi.MainUi()
        self.db=Database.Database()

        self.signup=SignupPage.SignupPage(self.ui,self.db)
        self.findinfo=FindInfoPage.FindInfoPage(self.ui,self.db)
        self.playlist=PlaylistPage.PlaylistPage(self.ui,self.db)
        self.video=VideoPage.VideoPage(self.ui,self.db)

        # === 버튼, 이동 페이지 연결 ===
        self.ui.loginPageFindInfoBtn.clicked.connect(self.goFindInfo)
        self.ui.loginPageSignupBtn.clicked.connect(self.goSignup)
        self.ui.loginPageBtn.clicked.connect(self.login)

        # for index in range(0,len(self.ui.mainPageBtnList)):
            
        #     self.ui.mainPageBtnList[index].clicked.connect(lambda event, nowIndex=index : self.moveEvent(event,nowIndex))
        #     self.ui.mainPageBtnList[index].enterEvent = lambda event, nowIndex=index : self.enterEvent(event,nowIndex)
        #     self.ui.mainPageBtnList[index].leaveEvent = lambda event, nowIndex=index : self.leaveEvent(event,nowIndex)


    # === 이벤트 함수 생성 ===

    # # 페이지 이동 함수
    # def moveEvent(self,event,index):
    #     if index == 0:
    #         self.ui.stackedWidget.setCurrentWidget(self.ui.PlaylistPage)
                
    #     elif index == 1:
    #         self.ui.stackedWidget.setCurrentWidget(self.ui.FindInfoPage)

    #     elif index == 2:
    #         self.ui.stackedWidget.setCurrentWidget(self.ui.SignupPage)


    def enterEvent(self,event,index):
        self.ui.mainPageBtnList[index].setStyleSheet(
            "background-color:white"
        )

    def leaveEvent(self,event,index):
        self.ui.mainPageBtnList[index].setStyleSheet(
           ( "background-color:#2E75B6; color:white; border-radius:10px;")
        )


    # === 페이지 이동 함수 === 
    def goFindInfo(self):
        self.ui.loginPageErrorMessage.setText(" ") 

        self.ui.stackedWidget.setCurrentWidget(self.ui.FindInfoPage)

    def goSignup(self):
        self.ui.loginPageErrorMessage.setText(" ") 

        self.ui.stackedWidget.setCurrentWidget(self.ui.SignupPage)


    # === 로그인 진행 ===
    def login(self):
        data=[]
        for i in range(0,len(self.ui.loginPageInputList)):
            value=self.ui.loginPageInputList[i].text()
            data.append(value)
        print(data)

        # self.id = self.ui.loginPageInputList[0].text()
        # self.pw = self.ui.loginPageInputList[1].text()

        table ="profile"
        column = ["id","pw"]
        # data = [self.id,self.pw]

        self.db.read(table,column,data,"")

        if len(self.db.readResult)>0:
            # print("로그인 성공")

            self.clearInput()

            self.ui.loginPageErrorMessage.setText(" ") # 일단 이렇게 해놓고 , 입력할때 없어지는거 구현하면 지우기

            self.ui.stackedWidget.setCurrentWidget(self.ui.PlaylistPage)
        else:
            # print("로그인 실패") 

            self.clearInput()

            self.ui.loginPageErrorMessage.setText("아이디 또는 비밀번호를 잘못 입력했습니다.\n입력하신 내용을 다시 확인해주세요.") 

            # self.ui.loginPageErrorMessage.setText(" ") 

    # 정보 초기화 : 아이디 비번 입력한거 초기화
    def clearInput(self):
            for i in range(0,len(self.ui.loginPageInputList)):
                self.ui.loginPageInputList[i].setText("")

    def show(self):
        self.loginPage.show()

if __name__ =="__main__":
    app = QtWidgets.QApplication(sys.argv) # gui 시작

    loginPage=LoginPage() # Main page Logic Class 를 객체로 만들어주는 줄
    # loginPage.show()

    sys.exit(app.exec_()) # gui 종료