import requests
from bs4 import BeautifulSoup
from Helper import MySqlHelper

class Douban_scraper:
    def __init__(self): #init里只放不会变的东西
        self. headers = {
            "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36"
            }
        self.starts = [0, 25, 50, 75]
        self.url = "https://movie.douban.com/top250"

    def get_data(self):
        titles = []
        ranks = []
        years = []
        for i in self.starts:
            url = f"{self.url}?start={i}"
            response = requests.get(url = url, headers = self.headers)
            soup = BeautifulSoup(response.text, "html.parser")

            page_titles = self.titles(soup)
            page_ranks = self.rank_num(soup)
            page_years = self.release_year(soup)

            titles.extend(page_titles)
            ranks.extend(page_ranks)
            years.extend(page_years)
        return titles, ranks, years

    def titles(self, soup):
        all_titles = soup.find_all("span", attrs = {"class" : "title"})
        titles = []
        for title in all_titles:
            title_string = title.string
            if "/" not in title_string:
                titles.append(title_string)
        return titles

    def rank_num(self, soup):
        rank_num = soup.find_all("em")
        rank_num_list = []
        for rank in rank_num:
            rank_num_list.append(rank.string)
        return rank_num_list

    def release_year(self, soup):
        release_year = soup.find_all("div",
        attrs={"class": "bd"})
        release_year_list = []
        for bd in release_year:
                br = bd.find("p").find("br")
                # if br is not None: # 如果不是没找到br
                    # all_text = br.find_all_next(string=True) 
                    # for text in all_text:
                    #     print(repr(text)) #repr可以把空格啥的全显示出来
                if br is not None: 
                    year_text = br.find_next(
                    string = lambda text: text.strip()).strip() #这个地方不知道为什么，晚上解决
                    year = year_text[:4]            
                    release_year_list.append(year)
        return release_year_list

#把爬到的数据储存到sql里

from Helper import MySqlHelper

helper = MySqlHelper()
douban = Douban_scraper()
titles, ranks, years = douban.get_data()

helper.clear("douban_movies")
for i in range(len(titles)):
    sql = f"""
    INSERT INTO douban_movies
    (rank_num, title, release_year)
    VALUES ({ranks[i]}, '{titles[i]}', {years[i]})
    """
    helper.insert(sql)
print(helper.query("SELECT * FROM douban_movies"))



        
    
    

