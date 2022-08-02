from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import Database

class MainUi:
    def __init__(self):
        self.db=Database.Database()

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
                    loginPageInput.setPlaceholderText("아이디 : 20자 이내로 작성")
                    loginPageInput.setAlignment(Qt.AlignCenter)
                else:
                    loginPageInput.setPlaceholderText("비밀번호 : 20자 이내로 작성")
                    loginPageInput.setAlignment(Qt.AlignCenter)

                    loginPageInput.setEchoMode(QtWidgets.QLineEdit.Password)

# ======== btn
        # login btn
        self.loginPageBtn=QtWidgets.QPushButton(self.LoginPage)
        self.loginPageBtn.setGeometry(400, 540, 400, 50)
        self.loginPageBtn.setStyleSheet("background-color : #5B9BD5; color : white; border-radius:5px;")
        self.loginPageBtn.setText("로그인")
        self.loginPageBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # go findinfo page btn
        self.loginPageFindInfoBtn=QtWidgets.QPushButton(self.LoginPage)
        self.loginPageFindInfoBtn.setGeometry(500,590,100,35)
        self.loginPageFindInfoBtn.setStyleSheet("color : #00B0F0")
        self.loginPageFindInfoBtn.setText("아이디/비번찾기")
        self.loginPageFindInfoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # go signup page btn
        self.loginPageSignupBtn=QtWidgets.QPushButton(self.LoginPage)
        self.loginPageSignupBtn.setGeometry(600,590,70,35)
        self.loginPageSignupBtn.setStyleSheet("color : #00B0F0")
        self.loginPageSignupBtn.setText("회원가입")
        self.loginPageSignupBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # go signup page btn
        self.loginPageVideoBtn=QtWidgets.QPushButton(self.LoginPage)
        self.loginPageVideoBtn.setGeometry(600,800,70,35)
        self.loginPageVideoBtn.setStyleSheet("color : #00B0F0")
        self.loginPageVideoBtn.setText("영상")
        self.loginPageVideoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.signupPageIdDoubleCheckBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # signup btn
        self.signupPageBtn=QtWidgets.QPushButton(self.SignupPage)
        self.signupPageBtn.setGeometry(400, 560, 400, 50)
        self.signupPageBtn.setStyleSheet("background-color : #5B9BD5; color : white; border-radius:5px;")
        self.signupPageBtn.setText("회원가입")
        self.signupPageBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # signup page back btn : go login page
        self.signupPageBackBtn=QtWidgets.QPushButton(self.SignupPage)
        self.signupPageBackBtn.setGeometry(550,610,100,35)
        self.signupPageBackBtn.setStyleSheet("color : #00B0F0")
        self.signupPageBackBtn.setText("뒤로가기")
        self.signupPageBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
                findIndoPageLabel.setGeometry(150+(i*600),300, 400, 100)
                font = QtGui.QFont()
                font.setFamily("Bodoni Bk BT")
                font.setPixelSize(56)
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
                forgotIdLabel.setGeometry(45, 400+(i*50), 100, 40) # change
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
                forgetIdInput.setGeometry(150, 400+(i*50), 400, 40) # change
                font = QtGui.QFont()
                font.setFamily("나눔고딕")
                font.setPixelSize(11)
                forgetIdInput.setFont(font)
                forgetIdInput.setStyleSheet("background-color:white; border-radius:5px;")

                self.forgotIdInputList.append(forgetIdInput)

                if i == 0:
                    forgetIdInput.setPlaceholderText("이름")
                    forgetIdInput.setAlignment(Qt.AlignCenter)
                else:
                    forgetIdInput.setPlaceholderText("전화번호 : - 없이 11자 작성")
                    forgetIdInput.setAlignment(Qt.AlignCenter)

# ======== forgot pw
        # forgot pw label
        self.forgotPwLabelList=[]
        self.forgotPwLabelTextList=["id","name","contact"]
        for i in range(0,3):
                forgotPwLabel = QtWidgets.QLabel(self.FindInfoPage)
                forgotPwLabel.setGeometry(645, 400+(i*50), 100, 40) # change
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
                forgetPwInput.setGeometry(750, 400+(i*50), 400, 40) # change
                font = QtGui.QFont()
                font.setFamily("나눔고딕")
                font.setPixelSize(11)
                forgetPwInput.setFont(font)
                forgetPwInput.setStyleSheet("background-color:white; border-radius:5px;")

                self.forgotPwInputList.append(forgetPwInput)

                if i == 0:
                    forgetPwInput.setPlaceholderText("아이디 : 20자 이내로 작성")
                    forgetPwInput.setAlignment(Qt.AlignCenter)
                elif i == 1:
                    forgetPwInput.setPlaceholderText("이름")
                    forgetPwInput.setAlignment(Qt.AlignCenter)
                else:
                    forgetPwInput.setPlaceholderText("전화번호 : - 없이 11자 작성")
                    forgetPwInput.setAlignment(Qt.AlignCenter)

# ======== btn 
        # forget id btn 
        self.forgotIdBtn=QtWidgets.QPushButton(self.FindInfoPage)
        self.forgotIdBtn.setGeometry(450, 510, 100, 50) # change
        self.forgotIdBtn.setStyleSheet("background-color : #5B9BD5; color : white; border-radius:5px;")
        self.forgotIdBtn.setText("아이디 찾기")
        self.forgotIdBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # forget pw btn
        self.forgotPwBtn=QtWidgets.QPushButton(self.FindInfoPage)
        self.forgotPwBtn.setGeometry(1050, 560, 100, 50) # change
        self.forgotPwBtn.setStyleSheet("background-color : #5B9BD5; color : white; border-radius:5px;")
        self.forgotPwBtn.setText("비밀번호 찾기")
        self.forgotPwBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # find info page back btn : go login page
        self.findInfoPageBackBtn=QtWidgets.QPushButton(self.FindInfoPage)
        self.findInfoPageBackBtn.setGeometry(550,700,100,35)
        self.findInfoPageBackBtn.setStyleSheet("color : #00B0F0")
        self.findInfoPageBackBtn.setText("뒤로가기")
        self.findInfoPageBackBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
# ======== error
        # forgot id error message
        self.forgotIdErrorMessage = QtWidgets.QLabel(self.FindInfoPage)
        self.forgotIdErrorMessage.setGeometry(150, 620, 400, 35) # change
        self.forgotIdErrorMessage.setAlignment(Qt.AlignCenter) # 글씨 가운데 정렬 문법 
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
        self.forgotPwErrorMessage.setGeometry(750, 620, 400, 35) 
        self.forgotPwErrorMessage.setAlignment(Qt.AlignCenter) # 글씨 가운데 정렬 문법 
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
        # playlist page *** 

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
        self.playlistPageLogo.setStyleSheet("color:white;")
        self.playlistPageLogo.setObjectName("playlistPageLogo")
        self.playlistPageLogo.setText("playlist")

# ======== scroll : playlist scroll / 나중에 가로 스크롤로 바꾸기 
        self.scrollPlaylist=QtWidgets.QScrollArea(self.PlaylistPage)
        self.scrollPlaylist.setGeometry(QtCore.QRect(100, 300, 1000, 300)) # 픽셀 나중에 조정 
        self.scrollPlaylist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollPlaylist.setWidgetResizable(True)
        self.scrollPlaylist.setObjectName("scrollPlaylist")

        # 도화지
        self.scrollArea = QtWidgets.QWidget()
        self.scrollArea.setGeometry(QtCore.QRect(0,0,300,150))
        self.scrollArea.setObjectName("scrollArea")
        
        # 그냥 위젯들을 묶어주는 컨테이너 : 레이아웃 적용할려고, 함수처럼 사용 
        self.groupBoxPlaylist = QtWidgets.QGroupBox(self.scrollArea)
        self.groupBoxPlaylist.setGeometry(25,25,300,150)
        self.groupBoxPlaylist.setObjectName("groupBoxPlaylist")

        # 레이아웃 적용 : 그냥 좌표만으로 위젯 배치 자동화
        self.verticalLayout = QtWidgets.QFormLayout(self.groupBoxPlaylist)
        self.verticalLayout.setContentsMargins(25, 25, 300, 150) #(100, 100, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

# ======== btn 
        # playlist btn 
        # table = "playlist"
        # column = ["playlistTitle"]
        # data=["title"]

        # self.db.read(table,column,data) 

        # self.playlistPageVideoBtnList=[]
        # self.removeBtnList=[]
        # self.modifyBtnList=[]

        # for index in range(0,10):
        #         self.playlistPageVideoBtn=QtWidgets.QPushButton(self.groupBoxPlaylist)
        #         self.removeBtn=QtWidgets.QPushButton(self.groupBoxPlaylist)
        #         # modifyBtn=QtWidgets.QPushButton(self.groupBoxPlaylist)

        #         self.playlistPageVideoBtn.setGeometry(25+(index*10),25,200,180)
        #         self.removeBtn.setGeometry(1100,100,200,180)
        #         # modifyBtn.setGeometry(900,100,200,180)

        #         self.playlistPageVideoBtn.setStyleSheet("background-color : #404040")

        #         # playlistPageVideoBtn.setText()
        #         self.removeBtn.setText("❌")
        #         # modifyBtn.setText("✏️")

        #         font = QtGui.QFont()
        #         font.setFamily("맑은 고딕")
        #         font.setPixelSize(180)
        #         self.playlistPageVideoBtn.setFont(font)

        #         self.playlistPageVideoBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #         self.removeBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #         # modifyBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        #         # self.playlistPageVideoBtnList.append(self.playlistPageVideoBtn)
        #         # self.removeBtnList.append(removeBtn)
        #         # self.modifyBtnList.append(modifyBtn)

        #         self.verticalLayout.addWidget(self.playlistPageVideoBtn)
        #         self.verticalLayout.addWidget(self.removeBtn)
        #         # self.verticalLayout.addWidget(modifyBtn)

        # self.groupBoxPlaylist.setLayout(self.verticalLayout)
        # self.scrollPlaylist.setWidget(self.groupBoxPlaylist)

        # add btn
        self.playlistPageAddBtn=QtWidgets.QPushButton(self.PlaylistPage)
        self.playlistPageAddBtn.setGeometry(265,190,50,100) 
        font = QtGui.QFont()
        font.setFamily("Bodoni Bk BT")
        font.setPixelSize(40)
        self.playlistPageAddBtn.setFont(font)
        self.playlistPageAddBtn.setText("🆕")
        self.playlistPageAddBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # remove btn

        # for index in range(0,10):
        #         self.playlistPageRemoveBtn=QtWidgets.QToolButton(self.groupBoxPlaylist)
        #         self.playlistPageRemoveBtn.setGeometry(550,640,100,35) 
        #         self.playlistPageRemoveBtn.setStyleSheet("color : #00B0F0")
        #         self.playlistPageRemoveBtn.setText("❌")
        #         self.playlistPageRemoveBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #         self.verticalLayout.addWidget(self.playlistPageRemoveBtn)
        # self.groupBoxPlaylist.setLayout(self.verticalLayout)
        # self.scrollPlaylist.setWidget(self.groupBoxPlaylist)

        self.playlistPageRemoveBtn=QtWidgets.QPushButton(self.PlaylistPage)
        self.playlistPageRemoveBtn.setGeometry(600,50,50,100) 
        font = QtGui.QFont()
        font.setFamily("Bodoni Bk BT")
        font.setPixelSize(40)
        self.playlistPageRemoveBtn.setFont(font)
        self.playlistPageRemoveBtn.setText("❌")
        self.playlistPageRemoveBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # modify btn 
        self.playlistPageModifyBtn=QtWidgets.QPushButton(self.PlaylistPage)
        self.playlistPageModifyBtn.setGeometry(500,50,50,100) 
        font = QtGui.QFont()
        font.setFamily("Bodoni Bk BT")
        font.setPixelSize(40)
        self.playlistPageModifyBtn.setFont(font)
        self.playlistPageModifyBtn.setText("✏️")
        self.playlistPageModifyBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # logout btn : go login page
        self.playlistPageLogoutkBtn=QtWidgets.QPushButton(self.PlaylistPage)
        self.playlistPageLogoutkBtn.setGeometry(550,640,100,35) # change
        self.playlistPageLogoutkBtn.setStyleSheet("color : #00B0F0")
        self.playlistPageLogoutkBtn.setText("로그아웃")
        self.playlistPageLogoutkBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.stackedWidget.addWidget(self.PlaylistPage)

        ##################################################################################################################################
        # video page

        self.VideoPage = QtWidgets.QWidget()
        self.VideoPage.setObjectName("VideoPage")

        # video logo
        self.videoPageLogo = QtWidgets.QLabel(self.VideoPage)
        self.videoPageLogo.setGeometry(200,40, 150, 100)
        font = QtGui.QFont()
        font.setFamily("Bodoni Bk BT")
        font.setPixelSize(56)
        self.videoPageLogo.setFont(font)
        self.videoPageLogo.setStyleSheet("color:white")
        self.videoPageLogo.setObjectName("videoPageLogo")
        self.videoPageLogo.setText("video")

# ======= btn
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

        # add btn
        self.videoPageAddBtn=QtWidgets.QPushButton(self.VideoPage)
        self.videoPageAddBtn.setGeometry(200,500,50,100) 
        font = QtGui.QFont()
        font.setFamily("Bodoni Bk BT")
        font.setPixelSize(40)
        self.videoPageAddBtn.setFont(font)
        self.videoPageAddBtn.setText("🆕")
        self.videoPageAddBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        # remove btn
        self.videoPageRemoveBtn=QtWidgets.QPushButton(self.VideoPage)
        self.videoPageRemoveBtn.setGeometry(200,600,50,100) 
        font = QtGui.QFont()
        font.setFamily("Bodoni Bk BT")
        font.setPixelSize(40)
        self.videoPageRemoveBtn.setFont(font)
        self.videoPageRemoveBtn.setText("❌")
        self.playlistPageRemoveBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.stackedWidget.addWidget(self.VideoPage)

# ======== scroll : playlist scroll in video page
        self.scrollVideolist=QtWidgets.QScrollArea(self.VideoPage)
        self.scrollVideolist.setGeometry(QtCore.QRect(850, 50, 300, 800)) # 픽셀 나중에 조정 다시 
        self.scrollVideolist.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollVideolist.setWidgetResizable(True)
        self.scrollVideolist.setObjectName("scrollVideolist")

        # 도화지
        self.scrollAreaVideo = QtWidgets.QWidget()
        self.scrollAreaVideo.setGeometry(QtCore.QRect(850, 50, 300, 800)) # 픽셀 나중에 조정 다시 
        self.scrollAreaVideo.setObjectName("scrollAreaVideo")
        
        # 그냥 위젯들을 묶어주는 컨테이너 : 레이아웃 적용할려고, 함수처럼 사용 
        self.groupBoxVideo = QtWidgets.QGroupBox(self.scrollAreaVideo)
        self.groupBoxVideo.setGeometry(0,0,300,800)
        self.groupBoxVideo.setObjectName("groupBoxVideo")

        # 레이아웃 적용 : 그냥 좌표만으로 위젯 배치 자동화
        self.verticalLayoutV = QtWidgets.QFormLayout(self.groupBoxVideo)
        self.verticalLayoutV.setContentsMargins(0, 0, 0, 0) #(100, 100, 0, 0)
        self.verticalLayoutV.setObjectName("verticalLayoutV")
        self.verticalLayoutV.setSpacing(50)
        self.verticalLayoutV.setVerticalSpacing(100)


    ##################################################################################################################################

        self.MainWindow.setCentralWidget(self.centralWidget) # 얘를 기본으로 하겠다 선언 
        self.MainWindow.show() # MainWindow를 출혁하는 옵션 

    ##################################################################################################################################
    # 다이얼로그 함수 
    # 나중에 QInputDialog 사용해서 하나로 합치기 : add, modify
    # QMessageBox : remove 하나로 합치기 

# ======== find info page dialog : forget id, pw 둘 다 사용
    def findInfoDialog(self,Dialog,text):

        Dialog.setObjectName("find info Dialog")
        Dialog.setWindowTitle("find info page !")
        Dialog.resize(300,150)
        Dialog.setStyleSheet("background-color:#E7E6E6;")

        self.findInfoDialogLabel = QtWidgets.QLabel(Dialog)
        self.findInfoDialogLabel.setGeometry(QtCore.QRect(0,25,300,50))
        
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPixelSize(14)
        
        self.findInfoDialogLabel.setFont(font)
        self.findInfoDialogLabel.setStyleSheet("color:black;")
        self.findInfoDialogLabel.setAlignment(QtCore.Qt.AlignCenter) # 가운데 정렬 
        self.findInfoDialogLabel.setObjectName("dialogText")

        self.findInfoDialogLabel.setText(text)


# ======== playlist page dialog : add dialog
        # 나중에 QInputDialog 사용해서 간단하게 바꾸기 
    def addDialog(self,addDialog,text):
        addDialog.setObjectName("playlist page add dialog")
        addDialog.setWindowTitle("playlist page add dialog !")
        addDialog.resize(300,150)
        addDialog.setStyleSheet("background-color:#E7E6E6;")

        self.playlistAddDialogLabel = QtWidgets.QLabel(addDialog)
        self.playlistAddDialogLabel.setGeometry(QtCore.QRect(0,20,300,50))
                
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPixelSize(14) # 더 조은 방법 : font에 픽셀 사이즈 주는 방법 / 해상도마다 글씨크기가 자동으로 달라짐 : pixelsize 사용하기
                
        self.playlistAddDialogLabel.setFont(font)
        self.playlistAddDialogLabel.setStyleSheet("color:black;")
        self.playlistAddDialogLabel.setAlignment(QtCore.Qt.AlignCenter) # 가운데 정렬 
        self.playlistAddDialogLabel.setObjectName("addDialogText")
        self.playlistAddDialogLabel.setText(text)

        self.addDialogInput = QtWidgets.QLineEdit(addDialog)
        self.addDialogInput.setGeometry(25,75, 250, 40)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPixelSize(11)
        self.addDialogInput.setFont(font)
        self.addDialogInput.setStyleSheet("background-color:white; border-radius:5px;")

        self.addDialogDoneBtn=QtWidgets.QPushButton(addDialog)
        self.addDialogDoneBtn.setGeometry(125,120,50,20)
        self.addDialogDoneBtn.setStyleSheet("background-color:#404040; color:white; border-radius:5px;")
        self.addDialogDoneBtn.setText("done")

#         #
#     def addDialog(self,text):
#         self.text, self.ok = QInputDialog(self,'playlist add dialog','playlist title :')

#         # 해당 페이지에서 입력받기
#         if self.ok : 
#                 self.setText(str(text))
#         else:
#                 pass

# ======== playlist page dialog : remove dialog 
        # 나중에 QMessageBox 사용해서 간단하게 바꾸기
    def removeDialog(self,removeDialog,text):
        removeDialog.setObjectName("playlist page remove dialog")
        removeDialog.setWindowTitle("playlist page remove dialog !")
        removeDialog.resize(300,150)
        removeDialog.setStyleSheet("background-color:#E7E6E6;")

        self.playlistRemoveDialogLabel = QtWidgets.QLabel(removeDialog)
        self.playlistRemoveDialogLabel.setGeometry(QtCore.QRect(0,25,300,50))
                
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPixelSize(14) # 더 조은 방법 : font에 픽셀 사이즈 주는 방법 / 해상도마다 글씨크기가 자동으로 달라짐 : pixelsize 사용하기
                
        self.playlistRemoveDialogLabel.setFont(font)
        self.playlistRemoveDialogLabel.setStyleSheet("color:black;")
        self.playlistRemoveDialogLabel.setAlignment(QtCore.Qt.AlignCenter) # 가운데 정렬 
        self.playlistRemoveDialogLabel.setObjectName("removeDialogText")

        self.playlistRemoveDialogLabel.setText(text)

        self.removeDialogDoneBtn=QtWidgets.QPushButton(removeDialog)
        self.removeDialogDoneBtn.setGeometry(125,120,50,20)
        self.removeDialogDoneBtn.setStyleSheet("background-color:#404040; color:white; border-radius:5px;")
        self.removeDialogDoneBtn.setText("yes")

        # 
#     def removeDialog(self):
#         self.removeDialog = QtWidgets.QMessageBox()
#         self.removeDialog.setWindowTitle("remove")
#         self.removeDialog.setGeometry(450,100,300,150)

#         self.reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
#                              QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

#         if self.reply == QMessageBox.Yes:
#                 # event.accept()
#                 pass
#         else:
#                 # event.ignore()
#                 pass

# ======== playlist page dialog : modify dialog
        # 나중에 QInputDialog 사용해서 간단하게 바꾸기 
    def modifyDialog(self,modifyDialog,text):
        modifyDialog.setObjectName("playlist page modify dialog")
        modifyDialog.setWindowTitle("playlist page modify dialog !")
        modifyDialog.resize(300,150)
        modifyDialog.setStyleSheet("background-color:#E7E6E6;")

        self.playlistModifyDialogLabel = QtWidgets.QLabel(modifyDialog)
        self.playlistModifyDialogLabel.setGeometry(QtCore.QRect(0,20,300,50))
                
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPixelSize(14) 
                
        self.playlistModifyDialogLabel.setFont(font)
        self.playlistModifyDialogLabel.setStyleSheet("color:black;")
        self.playlistModifyDialogLabel.setAlignment(QtCore.Qt.AlignCenter) # 가운데 정렬 
        self.playlistModifyDialogLabel.setObjectName("modifyDialogText")
        self.playlistModifyDialogLabel.setText(text)

        self.modifyDialogInput = QtWidgets.QLineEdit(modifyDialog)
        self.modifyDialogInput.setGeometry(25,75, 250, 40)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPixelSize(11)
        self.modifyDialogInput.setFont(font)
        self.modifyDialogInput.setStyleSheet("background-color:white; border-radius:5px;")

        self.modifyDialogDoneBtn=QtWidgets.QPushButton(modifyDialog)
        self.modifyDialogDoneBtn.setGeometry(125,120,50,20)
        self.modifyDialogDoneBtn.setStyleSheet("background-color:#404040; color:white; border-radius:5px;")
        self.modifyDialogDoneBtn.setText("done")

# ======== video page dialog : add dialog
        # 나중에 QInputDialog 사용해서 간단하게 바꾸기 
    def addVideoDialog(self,addVideoDialog,text):
        addVideoDialog.setObjectName("video page add dialog")
        addVideoDialog.setWindowTitle("video page add dialog !")
        addVideoDialog.resize(300,150)
        addVideoDialog.setStyleSheet("background-color:#E7E6E6;")

        self.videoAddDialogLabel = QtWidgets.QLabel(addVideoDialog)
        self.videoAddDialogLabel.setGeometry(QtCore.QRect(0,20,300,50))
                
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPixelSize(14) # 더 조은 방법 : font에 픽셀 사이즈 주는 방법 / 해상도마다 글씨크기가 자동으로 달라짐 : pixelsize 사용하기
                
        self.videoAddDialogLabel.setFont(font)
        self.videoAddDialogLabel.setStyleSheet("color:black;")
        self.videoAddDialogLabel.setAlignment(QtCore.Qt.AlignCenter) # 가운데 정렬 
        self.videoAddDialogLabel.setObjectName("addDialogText")
        self.videoAddDialogLabel.setText(text)

        self.addVideoDialogInput = QtWidgets.QLineEdit(addVideoDialog)
        self.addVideoDialogInput.setGeometry(25,75, 250, 40)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPixelSize(11)
        self.addVideoDialogInput.setFont(font)
        self.addVideoDialogInput.setStyleSheet("background-color:white; border-radius:5px;")

        self.addVideoDialogDoneBtn=QtWidgets.QPushButton(addVideoDialog)
        self.addVideoDialogDoneBtn.setGeometry(125,120,50,20)
        self.addVideoDialogDoneBtn.setStyleSheet("background-color:#404040; color:white; border-radius:5px;")
        self.addVideoDialogDoneBtn.setText("done")

# ======== video page dialog : remove dialog 
    def removeVideoDialog(self,removeVideoDialog,text):
        removeVideoDialog.setObjectName("video page remove dialog")
        removeVideoDialog.setWindowTitle("video page remove dialog !")
        removeVideoDialog.resize(300,150)
        removeVideoDialog.setStyleSheet("background-color:#E7E6E6;")

        self.videoRemoveDialogLabel = QtWidgets.QLabel(removeVideoDialog)
        self.videoRemoveDialogLabel.setGeometry(QtCore.QRect(0,25,300,50))
                
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPixelSize(14) 
                
        self.videoRemoveDialogLabel.setFont(font)
        self.videoRemoveDialogLabel.setStyleSheet("color:black;")
        self.videoRemoveDialogLabel.setAlignment(QtCore.Qt.AlignCenter) # 가운데 정렬 
        self.videoRemoveDialogLabel.setObjectName("removeDialogText")

        self.videoRemoveDialogLabel.setText(text)

        self.removeVideoDialogDoneBtn=QtWidgets.QPushButton(removeVideoDialog)
        self.removeVideoDialogDoneBtn.setGeometry(125,120,50,20)
        self.removeVideoDialogDoneBtn.setStyleSheet("background-color:#404040; color:white; border-radius:5px;")
        self.removeVideoDialogDoneBtn.setText("yes")

    ##################################################################################################################################


