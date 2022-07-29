from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FindInfoPage:
    def __init__(self,ui,db):
        self.ui=ui
        self.db=db

        self.ui.findInfoPageBackBtn.clicked.connect(self.goBackPageInFindInfoPage)
        self.ui.forgotIdBtn.clicked.connect(self.forgotId)
        self.ui.forgotPwBtn.clicked.connect(self.forgotPw)

        self.dialogBox = QtWidgets.QDialog()

    # 정보 찾기 페이지에서 뒤로가기 버튼 : 로그인 페이지로 이동
    def goBackPageInFindInfoPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

    # 아이디 찾기 
    def forgotId(self):
        # data=[]

        # for index in range(0,len(self.ui.forgotIdInputList)):
        #     value=self.ui.forgotIdInputList[index].text()
        #     data.append(value)
        # print(data)

        name=self.ui.forgotIdInputList[0].text()
        contact=self.ui.forgotIdInputList[1].text()

        table ="profile"
        column = ["name","contact"]
        data=[name,contact]

        self.db.read(table,column,data,"")

        if len(self.db.readResult)>0:
            print("아이디 찾기 성공")

            self.ui.dialogBox(self.dialogBox,"아이디\n"+str(self.db.readResult[0][0]))
            self.dialogBox.show()

        else:
            print("아이디 찾기 실패")
            self.ui.forgotIdErrorMessage.setText("존재하지 않는 정보입니다.\n다시 정확하게 입력하거나 회원가입을 진행해주세요.") 


    # 비밀번호 찾기
    def forgotPw(self):
        # data=[]

        # for index in range(0,len(self.ui.forgotPwInputList)):
        #     value=self.ui.forgotPwInputList[index].text()
        #     data.append(value)
        # print(data)

        id=self.ui.forgotPwInputList[0].text()
        name=self.ui.forgotPwInputList[1].text()
        contact=self.ui.forgotPwInputList[2].text()

        table ="profile"
        column = ["id","name","contact"]
        data=[id,name,contact]

        self.db.read(table,column,data,"")

        if len(self.db.readResult)>0:
            print("비밀번호 찾기 성공")

            self.ui.dialogBox(self.dialogBox,"비밀번호\n"+str(self.db.readResult[0][1]))
            self.dialogBox.show()

        else:
            print("아이디 찾기 실패")
            self.ui.forgotPwErrorMessage.setText("존재하지 않는 정보입니다.\n다시 정확하게 입력해주세요.") 