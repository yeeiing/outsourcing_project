import sqlite3

class Database:
    def __init__(self):
        # 연결
        self.connect=sqlite3.connect("data.db")
        self.cursor=self.connect.cursor()
        
        # 프로필
        self.cursor.execute("CREATE TABLE IF NOT EXISTS profile(id TEXT PRIAMRY KEY, pw TEXT, name TEXT, contact TEXT)")
        # 개인 플레이스트 정보
        self.cursor.execute("CREATE TABLE IF NOT EXISTS playlist(playlisyTitle TEXT, videoTitle TEXT, userId TEXT, FOREIGN KEY(userId) REFERENCES profile(id))")    
    
    # insert 합치기 
    def insert(self,table,column,data):
        sql="INSERT INTO "+ table + "("
        # column 값 넣어주기 
        for index in range(0,len(column)):
            sql+=column[index]
            # 쉼표 찍어주기 
            if index>=0 and index + 1 != len(column):
                sql+=","
        sql+=")VALUES("
        # data 값 넣어주기 
        for index in range(0,len(data)):
            sql+="?"
            # 쉼표 찍어주기 
            if index >= 0 and index + 1 != len(data):
                sql+=","
        sql+=")"
        self.cursor.execute(sql,data)
        self.connect.commit()    

    # read 합치기 
    def read(self,table,column,data,yes):
        if yes=="yes":
            sql=" SELECT * FROM "+ table +" ORDER BY " + column + " DESC"
            print(sql)
            self.cursor.execute(sql)
        else:
            sql=" SELECT * FROM "+ table +" WHERE "
            # 원하는 column 값 넣어주기 
            for index in range(0,len(column)):
                sql+=column[index]+" = ? "
                # AND 찍어주기 
                if index >= 0 and index +1 != len(column):
                    sql += " AND "

            # print(sql,data)
            self.cursor.execute(sql,data)

        self.readResult=self.cursor.fetchall()
        # print(self.readResult)

    # update 합치기 
    def update(self,table,column,data):
        sql=" UPDATE "+table+" SET "
        for index in range(0,len(column)-1):
            sql+=column[index]+" =? " +","
        sql+=" WHERE "+column[-1]+" =? "

        self.cursor.execute(sql,data)
        self.connect.commit()

        # print(sql)
        
    # delete 합치기 
    def delete(self,table,column,data):
        sql=" DELETE FROM "+table+" WHERE "
        for index in range(0,len(column)):
            sql+=column[index]+" =? "

        self.cursor.execute(sql,data)
        self.connect.commit()