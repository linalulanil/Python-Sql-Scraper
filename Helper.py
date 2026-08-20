import mysql.connector
import os #os用来和操作系统打交道
#class里面def的是这个class的方法
class MySqlHelper: #设计蓝图
    def __init__(self): #初始化遥控器
        self.connection = mysql.connector.connect( #初始化要连接到sql
            host="localhost",
            port=3306,
            user="root",
            password=os.getenv("MYSQL_PASSWORD"), # get environment variable
            database="baidu_hot"
        )
    def query(self, sql): #给遥控器设计查询按钮 #谁来按按钮self就是谁，现在这个情况是helper
        cursor = self.connection.cursor()  # cursor是从遥控器里拿出一个负责给sql传达指令的小机器人
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close() #cursor工作结束
        return data #把结果还给外面的result，return后面写要送出去的东西，
        # return根本不知道返回给谁，但是谁在调用这个函数谁就能接收到return的快递

    def execute(self, sql):
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connection.commit()  # 确认修改
        cursor.close()

    def insert(self, sql):
        self.execute(sql)

    def update(self, sql):
        self.execute(sql)

    def delete(self, sql):
        self.execute(sql)

    def clear(self, table):
        sql = f"TRUNCATE TABLE {table}" #truncate：重置整张表，包括auto_increment
        self.execute(sql)

# import requests
# url = "https://top.baidu.com/api/board?platform=wise&tab=realtime"
# headers = {
#     "User-Agent": "Mozilla/5.0"
# }
# response = requests.get(url, headers=headers)
# # print(response.status_code)
# data = response.json()
# # print(data)
# hot_list = data["data"]["cards"][0]["content"][0]["content"]
#
# helper = MySqlHelper()
# helper.clear("hot_search")
# for rank, item in enumerate(hot_list[:10], start = 1):
#     title = item["word"]
#     sql = f"""
#     INSERT INTO hot_search (rank_num, word)
#     VALUES ({rank}, '{title}')
#     """ #f用来indicate后面字符串里有变量，"""用来indicate多行字符串
#     helper.insert(sql)
#
# print(helper.query("SELECT * FROM hot_search"))
