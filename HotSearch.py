import requests
from Helper import MySqlHelper #从Helper.py中import MySqlHelper

class HotSearch_Baidu:
    def __init__(self):
        self.url = "https://top.baidu.com/api/board?platform=wise&tab=realtime"
        self.headers = {
            "User-Agent": "Mozilla/5.0"
        }
        self.helper = MySqlHelper()
        #self.的意思是把这个变量装在HotSearch_Baidu身上

    def get_data(self):
        response = requests.get(url = self.url, headers = self.headers)
        data = response.json()
        hot_list = data["data"]["cards"][0]["content"][0]["content"]

        return hot_list

    def save_data(self, hot_list, stop): #enumerate会返回两个东西，分别是编号和item
        for rank, item in enumerate(hot_list[1:stop], start = 1):
            title = item["word"]
            sql = f"""
                    INSERT INTO hot_search (rank_num, word)
                    VALUES ({rank}, '{title}')
                """
            self.helper.insert(sql)

baidu = HotSearch_Baidu()

baidu.helper.clear("hot_search")
hot_list = baidu.get_data()
baidu.save_data(hot_list, 11)
print(baidu.helper.query("SELECT * FROM hot_search"))