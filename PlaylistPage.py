from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class PlaylistPage:
    def __init__(self,ui,db):
        self.ui=ui
        self.db=db

        # self.RankingCheck()

        self.ui.playlistPageLogoutkBtn.clicked.connect(self.logoutInPlaylistPage)
        self.ui.playlistPageAddBtn.clicked.connect(self.playlistAdd)

        self.dialogBox = QtWidgets.QDialog()

    # 재생목록 페이지에서 로그아웃 버튼 : 로그인 페이지로 이동
    def logoutInPlaylistPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

    # 추가 버튼 누르면, 재생목록 제목 작성하는 다이얼로그 띄우기 
    def playlistAdd(self):
        self.ui.dialogBox(self.dialogBox,"playlist title")
        self.dialogBox.show()



    # def RankingCheck(self):
    #     table = "record"
    #     column = ["numOfWin"]
    #     data= []

    #     self.db.read(table,column,data,"yes")
    #     for index in range(0,len(self.db.readResult)):
    #         self.ui.RankingLabelList[index+1].setText(str(index+1)+"\t\t"+str(self.db.readResult[index][3])+"\t\t"+str(self.db.readResult[index][0]))
    #         if index>11:
    #             break