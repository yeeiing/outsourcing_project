from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class PlaylistPage:
    def __init__(self,ui,db):
        self.ui=ui
        self.db=db

        # 페이지 이동 
        self.ui.playlistPageLogoutkBtn.clicked.connect(self.logoutInPlaylistPage)
        # self.ui.playlistPageVideoBtn.clicked.connect(self.goVideoPage) # *** 고치기 ***

        # 해당 다이얼로그 출력
        self.ui.playlistPageAddBtn.clicked.connect(self.showAddDialog)
        self.ui.playlistPageRemoveBtn.clicked.connect(self.showRemoveDialog)
        self.ui.playlistPageModifyBtn.clicked.connect(self.showModifyDialog)

        self.addDialog = QtWidgets.QDialog()
        self.removeDialog = QtWidgets.QDialog()
        self.modifyDialog = QtWidgets.QDialog()

    # 재생목록 페이지에서 로그아웃 버튼 : 로그인 페이지로 이동
    def logoutInPlaylistPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

    # 추가 버튼 누르면, 재생목록 제목 작성하는 다이얼로그 띄우는 함수 
    # 다이얼로그에서 입력 값 받고 , 그 입력 값을 playlist table의 playlistTitle 에 저장
    # 로그인할 떄, 아이디 값도 받아와야 됨 -> playlist table의 userId 에 저장
    # db.insert 이용
    def showAddDialog(self):
        self.ui.addDialog(self.addDialog,"add playlist :")
        self.addDialog.show()

    # 수정 버튼 : 각 재생목록 위에 ✏️ , 다이얼로그
    # 추가 다이얼로그랑 똑같음 !! -> 근데 db.update 이용
    def showModifyDialog(self):
        self.ui.modifyDialog(self.modifyDialog,"modify playlist title :")
        self.modifyDialog.show()

    # 삭제 버튼 : 각 재생목록 위에 ❌ , 다이얼로그
    # db.delete 
    def showRemoveDialog(self):
        self.ui.removeDialog(self.removeDialog,"진짜 플리 삭제?")
        self.removeDialog.show()