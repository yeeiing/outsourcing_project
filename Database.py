import sqlite3

class Database:
    def __init__(self):
        # 연결
        self.connect=sqlite3.connect("data.db")
        self.cursor=self.connect.cursor()
        
        self.cursor.execute("CREATE TABLE IF NOT EXISTS profile(id TEXT PRIMARY KEY, pw TEXT, name TEXT, contact TEXT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS playlist(playlistTitle TEXT, userId TEXT, FOREIGN KEY(userId) REFERENCES profile(id))") 
        self.cursor.execute("CREATE TABLE IF NOT EXISTS video(playlistTitle TEXT, videoTitle TEXT, videoLink TEXT, userId TEXT, FOREIGN KEY(userId) REFERENCES profile(id))")   
    
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
    def read(self,table,column,data):
        sql=" SELECT * FROM "+ table +" WHERE "
        # 원하는 column 값 넣어주기 
        for index in range(0,len(column)):
            sql+=column[index]+" = ? "
            # AND 찍어주기 
            if index >= 0 and index +1 != len(column):
                sql += " AND "

        # print(sql)
        self.cursor.execute(sql,data)
        self.readResult=self.cursor.fetchall() # return 으로 받기 
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