from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MainUi:
    def __init__(self):
        self.MainWindow=QtWidgets.QMainWindow()
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(1200,900)
        self.MainWindow.setMaximumSize(1200,900)
        self.MainWindow.setStyleSheet("background-color : black")
        
        self.centralWidget = QtWidgets.QWidget(self.MainWindow)
        self.centralWidget.setObjectName("centralwidget")
        self.centralWidget.setStyleSheet("background-color : black")

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(0,0,1200,900)
        self.stackedWidget.setMaximumSize(1200,900)

        self.stackedWidget.setObjectName("stackedWidget")

        ##################################################################################################################################
        # login page = main page

        self.LoginPage = QtWidgets.QWidget()
        self.LoginPage.setObjectName("LoginPage")
# ======== page main logo
        # login logo
        self.loginPageLogo = QtWidgets.QLabel(self.LoginPage)
        self.loginPageLogo.setGeometry(400, 290, 400, 100)
        font = QtGui.QFont()
        font.setFamily("Bodoni Bk BT")
        font.setPixelSize(56)
        self.loginPageLogo.setFont(font)
        self.loginPageLogo.setStyleSheet("color:white")
        self.loginPageLogo.setObjectName("loginPageLogo")
        self.loginPageLogo.setText("login")
# ======== label
        # id, pw label
        self.loginPageLabelList=[]
        self.loginPageLabelTextList=["id","pw"]
        for i in range(0,2):
                loginPageLabel = QtWidgets.QLabel(self.LoginPage)
                loginPageLabel.setGeometry(345, 390+(i*50), 50, 40)
                font = QtGui.QFont()
                font.setFamily("Bodoni Bk BT")
                font.setPixelSize(36)
                loginPageLabel.setFont(font)
                loginPageLabel.setStyleSheet("color : white;")

                loginPageLabel.setText(self.loginPageLabelTextList[i])

                self.loginPageLabelList.append(loginPageLabel)
# ======== lnput
        # id, pw input
        self.loginPageInputList=[]
        for i in range(0,2):
                loginPageInput = QtWidgets.QLineEdit(self.LoginPage)
                loginPageInput.setGeometry(400, 390+(i*50), 400, 40)
                font = QtGui.QFont()
                font.setFamily("나눔고딕")
                font.setPixelSize(11)
                loginPageInput.setFont(font)
                loginPageInput.setStyleSheet("background-color:white; border-radius:5px;")

                self.loginPageInputList.append(loginPageInput)

                if i == 0:
                    loginPageInput.setPlaceholderText("아이디")
                    loginPageInput.setAlignment(Qt.AlignCenter)
                else:
                    loginPageInput.setPlaceholderText("비밀번호")
                    loginPageInput.setAlignment(Qt.AlignCenter)

                    loginPageInput.setEchoMode(QtWidgets.QLineEdit.Password)

# ======== btn
        # login btn
        self.loginPageBtn=QtWidgets.QPushButton(self.LoginPage)
        self.loginPageBtn.setGeometry(400, 540, 400, 50)
        self.loginPageBtn.setStyleSheet("background-color : #5B9BD5; color : white; border-radius:5px;")
        self.loginPageBtn.setText("로그인")

        # go findinfo page btn
        self.loginPageFindInfoBtn=QtWidgets.QPushButton(self.LoginPage)
        self.loginPageFindInfoBtn.setGeometry(500,590,100,35)
        self.loginPageFindInfoBtn.setStyleSheet("color : #00B0F0")
        self.loginPageFindInfoBtn.setText("아이디/비번찾기")

        # go signup page btn
        self.loginPageSignupBtn=QtWidgets.QPushButton(self.LoginPage)
        self.loginPageSignupBtn.setGeometry(600,590,70,35)
        self.loginPageSignupBtn.setStyleSheet("color : #00B0F0")
        self.loginPageSignupBtn.setText("회원가입")
# ======== error message
        # login error label
        self.loginPageErrorMessage = QtWidgets.QLabel(self.LoginPage)
        self.loginPageErrorMessage.setGeometry(QtCore.QRect(400, 490, 400, 50))
        self.loginPageErrorMessage.setAlignment(QtCore.Qt.AlignCenter) # 글씨 가운데 정렬 문법 
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(11)
        self.loginPageErrorMessage.setFont(font)
        self.loginPageErrorMessage.setStyleSheet("color : red")
        self.loginPageErrorMessage.setObjectName("loginPageError")
        # 에러메시지 출력 : 나중에 로그인 페이지로 옯기기, 지금 위치 설정 중 
        # self.loginPageErrorMessage.setText("아이디 또는 비밀번호를 잘못 입력했습니다.\n입력하신 내용을 다시 확인해주세요.") 

        # border line

        self.stackedWidget.addWidget(self.LoginPage)

        ##################################################################################################################################
        # signup page

        self.SignupPage = QtWidgets.QWidget()
        self.SignupPage.setObjectName("SignupPage")
# ======== page main logo
        # signup logo
        self.loginPageLogo = QtWidgets.QLabel(self.SignupPage)
        self.loginPageLogo.setGeometry(400, 200, 400, 100) 
        font = QtGui.QFont()
        font.setFamily("Bodoni Bk BT")
        font.setPixelSize(56)
        self.loginPageLogo.setFont(font)
        self.loginPageLogo.setStyleSheet("color:white")
        self.loginPageLogo.setObjectName("loginPageLogo")
        self.loginPageLogo.setText("signup")
# ========
        # id, pw, name, contact label
        self.signupPageLabelList=[]
        self.sigupPageLabelTextList=["id","pw","name","contact"]
        for i in range(0,4):
                signupPageLabel = QtWidgets.QLabel(self.SignupPage)
                signupPageLabel.setGeometry(290, 300+(i*50), 100, 40)
                font = QtGui.QFont()
                font.setFamily("Bodoni Bk BT")
                font.setPixelSize(36)
                signupPageLabel.setFont(font)
                signupPageLabel.setStyleSheet("color : white;")

                signupPageLabel.setText(self.sigupPageLabelTextList[i])

                self.signupPageLabelList.append(signupPageLabel)

        # id, pw, name, contact input
        self.signupPageInputList=[]
        for i in range(0,4):
                signupPageInput = QtWidgets.QLineEdit(self.SignupPage)
                signupPageInput.setGeometry(400, 300+(i*50), 400, 40)
                font = QtGui.QFont()
                font.setFamily("나눔고딕")
                font.setPixelSize(11)
                signupPageInput.setFont(font)
                signupPageInput.setStyleSheet("background-color:white; border-radius:5px;")

                self.signupPageInputList.append(signupPageInput)

                if i == 0:
                    signupPageInput.setPlaceholderText("아이디 : 20자 이내로 작성")
                    signupPageInput.setAlignment(Qt.AlignCenter)
                elif i == 1:
                    signupPageInput.setPlaceholderText("비밀번호 : 20자 이내로 작성")
                    signupPageInput.setAlignment(Qt.AlignCenter)

                    signupPageInput.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)

                elif i == 2 :
                    signupPageInput.setPlaceholderText("이름")
                    signupPageInput.setAlignment(Qt.AlignCenter)

                else:
                    signupPageInput.setPlaceholderText("전화번호 : - 없이 11자 작성")
                    signupPageInput.setAlignment(Qt.AlignCenter)
                        
# ======== btn
        # id : double check btn
        self.signupPageIdDoubleCheckBtn=QtWidgets.QPushButton(self.SignupPage)
        self.signupPageIdDoubleCheckBtn.setGeometry(690, 305, 100, 30)
        self.signupPageIdDoubleCheckBtn.setStyleSheet("background-color : #5B9BD5; color : white;")
        self.signupPageIdDoubleCheckBtn.setText("중복확인")

        # signup btn
        self.signupPageBtn=QtWidgets.QPushButton(self.SignupPage)
        self.signupPageBtn.setGeometry(400, 560, 400, 50)
        self.signupPageBtn.setStyleSheet("background-color : #5B9BD5; color : white; border-radius:5px;")
        self.signupPageBtn.setText("회원가입")

        # signup page back btn : go login page
        self.signupPageBackBtn=QtWidgets.QPushButton(self.SignupPage)
        self.signupPageBackBtn.setGeometry(550,610,100,35)
        self.signupPageBackBtn.setStyleSheet("color : #00B0F0")
        self.signupPageBackBtn.setText("뒤로가기")
# ======== error message
        # signup double check error label
        self.sginupPageDoubleCheckErrorMessage = QtWidgets.QLabel(self.SignupPage)
        self.sginupPageDoubleCheckErrorMessage.setGeometry(805, 290, 400, 50)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(11)
        self.sginupPageDoubleCheckErrorMessage.setFont(font)
        self.sginupPageDoubleCheckErrorMessage.setStyleSheet("color : red")
        self.sginupPageDoubleCheckErrorMessage.setObjectName("signupPageDoubleCheckError")
        # 에러메시지 출력 : 나중에 회원가입 페이지로 옯기기, 지금 위치 설정 중 
        # self.sginupPageDoubleCheckErrorMessage.setText("이미 존재하는 아이디입니다.\n다시 입력해주세요.") 

        # signup error label : contact double check
        self.signupPageErrorMessage = QtWidgets.QLabel(self.SignupPage)
        self.signupPageErrorMessage.setGeometry(QtCore.QRect(400, 500, 400, 35))
        self.signupPageErrorMessage.setAlignment(QtCore.Qt.AlignCenter) # 글씨 가운데 정렬 문법 
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(11)
        self.signupPageErrorMessage.setFont(font)
        self.signupPageErrorMessage.setStyleSheet("color : red")
        self.signupPageErrorMessage.setObjectName("loginPageError")
        # 에러메시지 출력 : 나중에 회원가입 페이지로 옯기기, 지금 위치 설정 중 
        # self.signupPageErrorMessage.setText("이미 존재하는 연락처입니다.\n로그인을 진행해주세요.") 


        self.stackedWidget.addWidget(self.SignupPage)

        ##################################################################################################################################
        # findinfo page

        self.FindInfoPage = QtWidgets.QWidget()
        self.FindInfoPage.setObjectName("FindInfoPage")
# ======== page main logo
        # find info page logo : forgot id, pw 
        self.findInfoPageLabelList=[]
        self.findInfoPageLabelTextList=["forgot id","forgot pw"]
        for i in range(0,2):
                findIndoPageLabel = QtWidgets.QLabel(self.FindInfoPage)
                findIndoPageLabel.setGeometry(150+(i*580),300, 500, 50)
                font = QtGui.QFont()
                font.setFamily("Bodoni Bk BT")
                font.setPixelSize(36)
                findIndoPageLabel.setFont(font)
                findIndoPageLabel.setStyleSheet("color : white;")

                findIndoPageLabel.setText(self.findInfoPageLabelTextList[i])

                self.findInfoPageLabelList.append(findIndoPageLabel)
# ======== forgot id
        # forgot id label
        self.forgotIdLabelList=[]
        self.forgorIdLabelTextList=["name","contact"]
        for i in range(0,2):
                forgotIdLabel = QtWidgets.QLabel(self.FindInfoPage)
                forgotIdLabel.setGeometry(30, 360+(i*50), 100, 35) # change
                font = QtGui.QFont()
                font.setFamily("Bodoni Bk BT")
                font.setPixelSize(36)
                forgotIdLabel.setFont(font)
                forgotIdLabel.setStyleSheet("color : white;")

                forgotIdLabel.setText(self.forgorIdLabelTextList[i])

                self.forgotIdLabelList.append(forgotIdLabel)

        # name, contact input in forget id 
        self.forgotIdInputList=[]
        for i in range(0,2):
                forgetIdInput = QtWidgets.QLineEdit(self.FindInfoPage)
                forgetIdInput.setGeometry(150, 360+(i*50), 400, 35) # change
                font = QtGui.QFont()
                font.setFamily("나눔고딕")
                font.setPixelSize(11)
                forgetIdInput.setFont(font)
                forgetIdInput.setStyleSheet("background-color:white; border-radius:5px;")

                self.forgotIdInputList.append(forgetIdInput)
# ======== forgot pw
        # forgot pw label
        self.forgotPwLabelList=[]
        self.forgotPwLabelTextList=["id","name","contact"]
        for i in range(0,3):
                forgotPwLabel = QtWidgets.QLabel(self.FindInfoPage)
                forgotPwLabel.setGeometry(595, 360+(i*50), 100, 35) # change
                font = QtGui.QFont()
                font.setFamily("Bodoni Bk BT")
                font.setPixelSize(36)
                forgotPwLabel.setFont(font)
                forgotPwLabel.setStyleSheet("color : white;")

                forgotPwLabel.setText(self.forgotPwLabelTextList[i])

                self.forgotPwLabelList.append(forgotPwLabel)

        # id, name, contact input in forget pw 
        self.forgotPwInputList=[]
        for i in range(0,3):
                forgetPwInput = QtWidgets.QLineEdit(self.FindInfoPage)
                forgetPwInput.setGeometry(710, 360+(i*50), 400, 35) # change
                font = QtGui.QFont()
                font.setFamily("나눔고딕")
                font.setPixelSize(11)
                forgetPwInput.setFont(font)
                forgetPwInput.setStyleSheet("background-color:white; border-radius:5px;")

                self.forgotPwInputList.append(forgetPwInput)
# ======== btn 
        # forget id btn 
        self.forgotIdBtn=QtWidgets.QPushButton(self.FindInfoPage)
        self.forgotIdBtn.setGeometry(400, 600, 100, 35) # change
        self.forgotIdBtn.setStyleSheet("background-color : #5B9BD5; color : white; border-radius:5px;")
        self.forgotIdBtn.setText("아이디 찾기")

        # forget pw btn
        self.forgotPwBtn=QtWidgets.QPushButton(self.FindInfoPage)
        self.forgotPwBtn.setGeometry(1000, 600, 100, 35) # change
        self.forgotPwBtn.setStyleSheet("background-color : #5B9BD5; color : white; border-radius:5px;")
        self.forgotPwBtn.setText("비밀번호 찾기")

        # find info page back btn : go login page
        self.findInfoPageBackBtn=QtWidgets.QPushButton(self.FindInfoPage)
        self.findInfoPageBackBtn.setGeometry(550,650,100,35)
        self.findInfoPageBackBtn.setStyleSheet("color : #00B0F0")
        self.findInfoPageBackBtn.setText("뒤로가기")
# ======== error
        # forgot id error message
        self.forgotIdErrorMessage = QtWidgets.QLabel(self.FindInfoPage)
        self.forgotIdErrorMessage.setGeometry(QtCore.QRect(150, 700, 400, 35)) # change
        self.forgotIdErrorMessage.setAlignment(QtCore.Qt.AlignCenter) # 글씨 가운데 정렬 문법 
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(11)
        self.forgotIdErrorMessage.setFont(font)
        self.forgotIdErrorMessage.setStyleSheet("color : red")
        self.forgotIdErrorMessage.setObjectName("forgotIdErrorMessage")
        # 에러메시지 출력 : 나중에 회원가입 페이지로 옯기기, 지금 위치 설정 중 
        # self.forgotIdErrorMessage.setText("이미 존재하는 연락처입니다.\n로그인을 진행해주세요.") 

        # forgot pw error message
        self.forgotPwErrorMessage = QtWidgets.QLabel(self.FindInfoPage)
        self.forgotPwErrorMessage.setGeometry(QtCore.QRect(710, 700, 400, 35)) # change
        self.forgotPwErrorMessage.setAlignment(QtCore.Qt.AlignCenter) # 글씨 가운데 정렬 문법 
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(11)
        self.forgotPwErrorMessage.setFont(font)
        self.forgotPwErrorMessage.setStyleSheet("color : red")
        self.forgotPwErrorMessage.setObjectName("forgotPwErrorMessage")
        # 에러메시지 출력 : 나중에 회원가입 페이지로 옯기기, 지금 위치 설정 중 
        # self.forgotPwErrorMessage.setText("이미 존재하는 연락처입니다.\n로그인을 진행해주세요.") 


        self.stackedWidget.addWidget(self.FindInfoPage)

        ##################################################################################################################################
        # playlist page

        self.PlaylistPage = QtWidgets.QWidget()
        self.PlaylistPage.setObjectName("PlaylistPage")

# ======== page main logo
        # playlist logo
        self.playlistPageLogo = QtWidgets.QLabel(self.PlaylistPage)
        self.playlistPageLogo.setGeometry(100, 190, 170, 100)
        font = QtGui.QFont()
        font.setFamily("Bodoni Bk BT")
        font.setPixelSize(56)
        self.playlistPageLogo.setFont(font)
        self.playlistPageLogo.setStyleSheet("color:white")
        self.playlistPageLogo.setObjectName("playlistPageLogo")
        self.playlistPageLogo.setText("playlist")

        # logout btn : go login page
        self.playlistPageLogoutkBtn=QtWidgets.QPushButton(self.PlaylistPage)
        self.playlistPageLogoutkBtn.setGeometry(550,640,100,35) # change
        self.playlistPageLogoutkBtn.setStyleSheet("color : #00B0F0")
        self.playlistPageLogoutkBtn.setText("로그아웃")

# ======== scroll : 일단 랭킹 페이지 긁어옴 -> 나중에 !!! 가로 스크롤로 바꾸기 

        # 플레이리스트 페이지 가로 스크롤에서 출력해야 되는 거 : 영상페이지로 갈 수 있는 버튼 구현 (썸네일 말고 제목 누르면 갈 수 있게 하기) 아마도
        # 2개 다 동시에 가짐, 스크롤 영역
        # 나중에 변수 이름 바꿔주기 
        self.scroll=QtWidgets.QScrollArea(self.PlaylistPage)
        self.scroll.setGeometry(QtCore.QRect(100, 300, 1000, 300)) # 픽셀 나중에 조정 
        self.scroll.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scroll.setWidgetResizable(True)
        self.scroll.setObjectName("scroll")

        # 도화지
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(100,300,1000,300))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        
        # 그냥 위젯들을 묶어주는 컨테이너 : 레이아웃 적용할려고, 함수처럼 사용 
        self.scrollGroupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.scrollGroupBox.setGeometry(0,0,1000,300)
        self.scrollGroupBox.setObjectName("scrollGroupBox")

        # 레이아웃 적용 : 그냥 좌표만으로 위젯 배치 자동화
        self.verticalLayout = QtWidgets.QFormLayout(self.scrollGroupBox)
        self.verticalLayout.setContentsMargins(100,100, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setVerticalSpacing(70)
        
        # # 나중에 버튼 리스트로 바꾸기 
        # self.RankingLabelList=[]
        
        # for i in range(0,11):
        #         RankingPageLabel=QtWidgets.QLabel(self.scrollGroupBox)
        #         font=QtGui.QFont()
        #         font.setFamily("나눔고딕")
        #         font.setPixelSize(11)
        #         font.setBold(False)
        #         RankingPageLabel.setFont(font)
        #         self.RankingLabelList.append(RankingPageLabel)
        #         self.verticalLayout.addWidget(RankingPageLabel)
        #         if i==0:
        #                 RankingPageLabel.setText("등수\t\t이름\t\t이긴횟수")
# ======== btn 
        # add btn 
        self.playlistPageAddBtn=QtWidgets.QPushButton(self.PlaylistPage)
        self.playlistPageAddBtn.setGeometry(280,190,100,100) 
        self.playlistPageAddBtn.setStyleSheet("color : white")
        self.playlistPageAddBtn.setText("+")


        # remove btn


        # change btn 


        self.stackedWidget.addWidget(self.PlaylistPage)

        ##################################################################################################################################
        # video page

        self.VideoPage = QtWidgets.QWidget()
        self.VideoPage.setObjectName("VideoPage")

        # video logo
        self.videoPageLogo = QtWidgets.QLabel(self.VideoPage)
        self.videoPageLogo.setGeometry(200,150, 150, 100)
        font = QtGui.QFont()
        font.setFamily("Bodoni Bk BT")
        font.setPixelSize(56)
        self.videoPageLogo.setFont(font)
        self.videoPageLogo.setStyleSheet("color:white")
        self.videoPageLogo.setObjectName("videoPageLogo")
        self.videoPageLogo.setText("video")

        # logout btn : go login page
        self.videoPageLogoutBtn=QtWidgets.QPushButton(self.VideoPage)
        self.videoPageLogoutBtn.setGeometry(550,640,100,35) # change
        self.videoPageLogoutBtn.setStyleSheet("color : #00B0F0")
        self.videoPageLogoutBtn.setText("로그아웃")

        # back btn : go playlist page
        self.videoPageBackBtn=QtWidgets.QPushButton(self.VideoPage)
        self.videoPageBackBtn.setGeometry(550,640,100,35) # change
        self.videoPageBackBtn.setStyleSheet("color : #00B0F0")
        self.videoPageBackBtn.setText("뒤로가기")

        self.stackedWidget.addWidget(self.VideoPage)


    ##################################################################################################################################

        self.MainWindow.setCentralWidget(self.centralWidget) # 얘를 기본으로 하겠다 선언 
        self.MainWindow.show() # MainWindow를 출혁하는 옵션 

    ##################################################################################################################################
    # 다이얼로그 함수 

    def dialogBox(self,Dialog,text):

        Dialog.setObjectName("Dialog")
        Dialog.resize(300,150)
        Dialog.setStyleSheet("background-color:#E7E6E6;")

        self.dialogText = QtWidgets.QLabel(Dialog)
        self.dialogText.setGeometry(QtCore.QRect(0,10,300,50))
        
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPixelSize(10) # 더 조은 방법 : font에 픽셀 사이즈 주는 방법 / 해상도마다 글씨크기가 자동으로 달라짐 : pixelsize 사용하기
        
        self.dialogText.setFont(font)
        self.dialogText.setStyleSheet("color:black;")
        self.dialogText.setAlignment(QtCore.Qt.AlignCenter) # 가운데 정렬 
        self.dialogText.setObjectName("dialogText")

        self.dialogText.setText(text)

    ##################################################################################################################################
    # # 텍스트 초기화 함수 : 모든 input에 사용 / 안됨 걍 하나씩 만들어주기 ~~
    # def clear(self):
    #     pass

