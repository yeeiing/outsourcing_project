from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import pafy
import vlc 
import time
import threading

import Play

class VideoPage:
    def __init__(self,ui,db):
        self.ui=ui
        self.db=db

        # self.videoPrint()

        # 페이지 이동
        self.ui.videoPageBackBtn.clicked.connect(self.goBackPageInVideoPage)
        self.ui.videoPageLogoutBtn.clicked.connect(self.logoutInVideoPage)

        # 추가, 삭제 버튼 관련 다이얼로그 출력
        self.ui.videoPageAddBtn.clicked.connect(self.showAddDialog)
        self.ui.videoPageRemoveBtn.clicked.connect(self.showRemoveDialog)

        self.addVideoDialog = QtWidgets.QDialog()
        self.removeVideoDialog = QtWidgets.QDialog()

    # 영상 페이지에서 뒤로가기 버튼 : 재생목록 페이지로 이동
    def goBackPageInVideoPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.PlaylistPage)

    # 영상 페이지에서 로그아웃 버튼 : 로그인 페이지로 이동
    def logoutInVideoPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

    # 영상 추가 버튼 : update
    def showAddDialog(self):
        self.ui.addVideoDialog(self.addVideoDialog,"add playlist :")
        self.addVideoDialog.show()

    # 영상 삭제 버튼 : delete
    def showRemoveDialog(self):
        self.ui.removeVideoDialog(self.removeVideoDialog,"진짜 영상 삭제?")
        self.removeVideoDialog.show()

    # 크롤링, 미디어 플레이어 : 영상 띄워보기 -> 스레드 사용  ,, ? 
    # def videoPrint(self):
    #     self.play = Play.Play(self.ui)

    # 재생 버튼 


    # 일시정지 버튼 


    # 정지 버튼

    
    # 재생목록 + 제목 띄우기 