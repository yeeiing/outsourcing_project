from PyQt5 import QtCore, QtGui, QtWidgets

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

        # login logo
        self.loginPageLogo = QtWidgets.QLabel(self.LoginPage)
        self.loginPageLogo.setGeometry(410, 190, 150, 100)
        font = QtGui.QFont()
        font.setFamily("Bodoni Bk BT")
        font.setPixelSize(56)
        self.loginPageLogo.setFont(font)
        self.loginPageLogo.setStyleSheet("color:white")
        self.loginPageLogo.setObjectName("loginPageLogo")
        self.loginPageLogo.setText("login")

        # id, pw label
        self.loginPageLabelList=[]
        self.loginPageLabelTextList=["id","pw"]
        for i in range(0,2):
                loginPageLabel = QtWidgets.QLabel(self.LoginPage)
                loginPageLabel.setGeometry(320, 300+(i*50), 50, 35)
                font = QtGui.QFont()
                font.setFamily("Bodoni Bk BT")
                font.setPixelSize(36)
                loginPageLabel.setFont(font)
                loginPageLabel.setStyleSheet("color : white;")

                loginPageLabel.setText(self.loginPageLabelTextList[i])

                self.loginPageLabelList.append(loginPageLabel)

        # id, pw input
        self.loginPageInputList=[]
        for i in range(0,2):
                loginPageInput = QtWidgets.QLineEdit(self.LoginPage)
                loginPageInput.setGeometry(400, 300+(i*50), 400, 35)
                font = QtGui.QFont()
                font.setFamily("나눔고딕")
                font.setPixelSize(11)
                loginPageInput.setFont(font)
                loginPageInput.setStyleSheet("background-color:white; border-radius:5px;")

                self.loginPageInputList.append(loginPageInput)

        # login btn
        self.loginPageBtn=QtWidgets.QPushButton(self.LoginPage)
        self.loginPageBtn.setGeometry(400, 600, 400, 35)
        self.loginPageBtn.setStyleSheet("background-color : #5B9BD5; color : white;")
        self.loginPageBtn.setText("로그인")

        # go findinfo page btn
        self.loginPageFindInfoBtn=QtWidgets.QPushButton(self.LoginPage)
        self.loginPageFindInfoBtn.setGeometry(500,640,100,35)
        self.loginPageFindInfoBtn.setStyleSheet("color : #00B0F0")
        self.loginPageFindInfoBtn.setText("아이디/비번찾기")

        # go signup page btn
        self.loginPageSignupBtn=QtWidgets.QPushButton(self.LoginPage)
        self.loginPageSignupBtn.setGeometry(600,640,100,35)
        self.loginPageSignupBtn.setStyleSheet("color : #00B0F0")
        self.loginPageSignupBtn.setText("회원가입")

        # login error label
        # self.loginPageErrorMessage = QtWidgets.QLabel(self.LoginPage)
        # self.loginPageErrorMessage.setGeometry()
        # font = QtGui.QFont()
        # font.setFamily("나눔고딕")
        # font.setPointSize(20)
        # self.loginPageErrorMessage.setFont(font)
        # self.loginPageErrorMessage.setStyleSheet("color : red")
        # self.loginPageErrorMessage.setObjectName("loginPageError")

        self.stackedWidget.addWidget(self.LoginPage)

        ##################################################################################################################################
        # signup page

        self.SignupPage = QtWidgets.QWidget()
        self.SignupPage.setObjectName("SignupPage")

        # signup logo
        self.loginPageLogo = QtWidgets.QLabel(self.SignupPage)
        self.loginPageLogo.setGeometry(410, 190, 200, 100)
        font = QtGui.QFont()
        font.setFamily("Bodoni Bk BT")
        font.setPixelSize(56)
        self.loginPageLogo.setFont(font)
        self.loginPageLogo.setStyleSheet("color:white")
        self.loginPageLogo.setObjectName("loginPageLogo")
        self.loginPageLogo.setText("signup")

        self.stackedWidget.addWidget(self.SignupPage)

        ##################################################################################################################################
        # findinfo page

        self.FindInfoPage = QtWidgets.QWidget()
        self.FindInfoPage.setObjectName("FindInfoPage")

        # forgotid logo
        self.loginPageLogo = QtWidgets.QLabel(self.FindInfoPage)
        self.loginPageLogo.setGeometry(410, 190, 200, 100)
        font = QtGui.QFont()
        font.setFamily("Bodoni Bk BT")
        font.setPixelSize(56)
        self.loginPageLogo.setFont(font)
        self.loginPageLogo.setStyleSheet("color:white")
        self.loginPageLogo.setObjectName("loginPageLogo")
        self.loginPageLogo.setText("signup")

        # forgetpw logo
        self.loginPageLogo = QtWidgets.QLabel(self.FindInfoPage)
        self.loginPageLogo.setGeometry(410, 190, 200, 100)
        font = QtGui.QFont()
        font.setFamily("Bodoni Bk BT")
        font.setPixelSize(56)
        self.loginPageLogo.setFont(font)
        self.loginPageLogo.setStyleSheet("color:white")
        self.loginPageLogo.setObjectName("loginPageLogo")
        self.loginPageLogo.setText("signup")

        self.stackedWidget.addWidget(self.FindInfoPage)

        ##################################################################################################################################
        # playlist page

        self.PlaylistPage = QtWidgets.QWidget()
        self.PlaylistPage.setObjectName("PlaylistPage")

        self.stackedWidget.addWidget(self.PlaylistPage)

        ##################################################################################################################################
        # video page

        self.videoPage = QtWidgets.QWidget()
        self.videoPage.setObjectName("videoPage")

        self.stackedWidget.addWidget(self.videoPage)



        self.MainWindow.setCentralWidget(self.centralWidget) # 얘를 기본으로 하겠다 선언 
        self.MainWindow.show() # MainWindow를 출혁하는 옵션 
    ##################################################################################################################################
    # 다이얼로그 함수 

    def dialogGame(self,Dialog,text):

        Dialog.setObjectName("Dialog")
        Dialog.resize(350,250)
        Dialog.setStyleSheet("background-color:#E2F0D9;")

        self.gameText = QtWidgets.QLabel(Dialog)
        self.gameText.setGeometry(QtCore.QRect(0,0,300,200))
        
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        font.setPointSize(10) # 더 조은 방법 : font에 픽셀 사이즈 주는 방법 / 해상도마다 글씨크기가 자동으로 달라짐 : pixelsize 사용하기
        
        self.gameText.setFont(font)
        self.gameText.setStyleSheet("color:black;")
        self.gameText.setAlignment(QtCore.Qt.AlignCenter)
        self.gameText.setObjectName("gameText")

        self.gameText.setText(text)

