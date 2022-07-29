class VideoPage:
    def __init__(self,ui,db):
        self.ui=ui
        self.db=db

        # 페이지 이동
        self.ui.videoPageBackBtn.clicked.connect(self.goBackPageInVideoPage)
        self.ui.videoPageLogoutBtn.clicked.connect(self.logoutInVideoPage)

    # 영상 페이지에서 뒤로가기 버튼 : 재생목록 페이지로 이동
    def goBackPageInVideoPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.PlaylistPage)

    # 영상 페이지에서 로그아웃 버튼 : 로그인 페이지로 이동
    def logoutInVideoPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)