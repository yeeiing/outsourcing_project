class SignupPage:
    def __init__(self,ui,db):
        self.ui=ui
        self.db=db

        # self.ui,signupPageHomeBtn.clicked.connect(self.goMainPage)

    # 회원가입 페이지 홈 버튼
    def goMainPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.MainPage)