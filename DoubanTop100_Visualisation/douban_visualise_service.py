from HelperForDouban import MySqlHelper
import matplotlib.pyplot as plt
class VisualisationHelper:
    def __init__(self):
        self.helper = MySqlHelper() #这个class可以通过self.helper.query(...)向sql请求数据

    def movies_by_year(self):
        sql = """
            SELECT release_year, COUNT(*) AS movie_count
            FROM douban_movies
            GROUP BY release_year
            ORDER BY release_year
            """
        result = self.helper.query(sql)

        year = []
        amount = []
        for row in result:
            year.append(row[0])
            amount.append(row[1])
        return year, amount

    def plot_amount_by_year(self):
        year, amount = self.movies_by_year()
        #plt.bar(year, amount) 横轴用year，纵轴用amount
        bars = plt.bar(year, amount)
        plt.bar_label(bars)
        plt.xlabel("Year")
        plt.ylabel("Number")
        plt.title("Number of Top 100 Movies by Release Year")
        plt.show()


visualisation = VisualisationHelper()
result = visualisation.plot_amount_by_year()
print(result)

#现在开始画图








