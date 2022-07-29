class SignupPage:
    def __init__(self,ui,db):
        self.ui=ui
        self.db=db

        self.ui.signupPageBackBtn.clicked.connect(self.goBackPageInSignupPage)
        self.ui.signupPageIdDoubleCheckBtn.clicked.connect(self.idDoubleCheck)
        self.ui.signupPageBtn.clicked.connect(self.signup)

    # 회원가입 페이지에서 뒤로가기 버튼 : 로그인 페이지로 이동
    def goBackPageInSignupPage(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

    # 길이 예외처리+중복처리
    def idDoubleCheck(self): 
        # id=self.ui.signupPageInputId.text()
        id=self.ui.signupPageInputList[0].text()

        table ="profile"
        column = ["id"]
        data=[id]

        self.db.read(table,column,data,"")

        if len(id)>20:
            self.ui.sginupPageDoubleCheckErrorMessage.setText("20자 이내로 작성!") 
        else:
            if len(self.db.readResult)>0:
                print("존재하는 아이디")

                self.ui.sginupPageDoubleCheckErrorMessage.setText("이미 존재하는 아이디입니다.\n다시 입력해주세요.") 
            else:
                print("사용가능 아이디")

                self.ui.sginupPageDoubleCheckErrorMessage.setText("사용가능 아이디")
            
 
    # 회원가입 진행 : 연락처 중복 처리 + 비밀번호(20자), 연락처(11자) 길이 예외 처리 -> 길이 예외처리 먼저 !! 
    def signup(self):
        # data=[]
        # for index in range(0,len(self.ui.signupPageInputList)):
        #     value=self.ui.signupPageInputList[index].text()
        #     data.append(value)
        # print(data) # 확인, 나중에 주석 처리 하기

        # table ="profile"
        # column = ["name","contact"] # column 값 입력 때무네 그냥 변수 하나씩 입력받겠슴당 !

        # self.db.read(table,column,data,"")

        id=self.ui.signupPageInputList[0].text()
        pw=self.ui.signupPageInputList[1].text()
        name=self.ui.signupPageInputList[2].text()
        contact=self.ui.signupPageInputList[3].text()

        # 비밀번호 길이 예외 처리
        if len(pw)>20:
            self.ui.signupPageErrorMessage.setText("\npw : 20자 이내로 작성 !") 
        else:
            # 연락처 길이 예외 처리
            if len(contact)!=11:
                self.ui.signupPageErrorMessage.setText("\ncontact : 11자 작성 !") 
            else:
                # 연락처 중복 예외처리 진행
                table="profile"
                column=["contact"]
                data=[contact]

                self.db.read(table,column,data,"")

                if len(self.db.readResult)>0:
                    self.clearInput()

                    self.ui.signupPageErrorMessage.setText("이미 존재하는 연락처입니다.\n로그인을 진행해주세요.") 

                else:
                    print("회원가입 성공")

                    tableSignup="profile"
                    columnSignup=["id","pw","name","contact"]
                    dataSignup=[id,pw,name,contact]

                    self.db.insert(tableSignup,columnSignup,dataSignup)

                    self.clearInput()

                    self.ui.signupPageErrorMessage.setText(" ")

                    # 회원가입 성공시, 1. 바로 로그인 페이지로 이동하게 고치기
                    self.ui.stackedWidget.setCurrentWidget(self.ui.LoginPage)

                    # 회원가입 성공시, 2. 나의 플레이리스트 공백(=0? none?)으로 미리 설정
                    # table = "playlist"
                    # column = ["playlistTitle","videoTitle","userId"]
                    # data=[0,0,id]

                    # self.db.insert(table,column,data)

    # 정보 초기화 : 아이디 비번 입력한거 초기화
    def clearInput(self):
            for i in range(0,len(self.ui.signupPageInputList)):
                self.ui.signupPageInputList[i].setText("")