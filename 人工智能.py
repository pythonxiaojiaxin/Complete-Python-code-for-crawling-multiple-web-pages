from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from bs4 import BeautifulSoup
import time
import random
import csv
url = ''
def get(url):
    d = None
    try:
        i = './msedgedriver.exe'
        w = Service(i)
        a = Options()
        a.add_argument('user-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0')
        d = webdriver.Edge(options=a,service=w)
        d.get(url)
        time.sleep(random.uniform(1, 3))
        for i in range(10):
            d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
        s = BeautifulSoup(d.page_source, 'html.parser')
        return s
    except Exception as e:
        print('获取失败')
        return None
    finally:
        d.close()
def find(s):
    if not s:
        print('没有参数')
        return None
    z = (e.get_text().strip() for e in s.find_all('span', attrs={'class': 'movie-name-text'}))
    x = (e.get_text().strip() for e in s.find_all('span', attrs={'class': 'rating_num'}))
    c = (e.get_text().strip() for e in s.find_all('span', attrs={'class': 'comment-num'}))
    r = (e.get_text().strip() for e in s.find_all('div', attrs={'class': 'movie-misc'}))
    v = z,x,c,r
    if v:
        n,r,j,y = v
    else:
        print('无数据')
    with open('最终数据','w',newline='',encoding = 'utf-8') as f:
        w = csv.writer(f)
        w.writerow(['序列','标题','评分','评论','国家+总类别','演员'])
        for i,(n,r,j,y) in enumerate(zip(n,r,j,y),1):
            w.writerow([n,r,j,y])



list_url=['https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E5%96%9C%E5%89%A7&type=24&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E7%88%B1%E6%83%85&type=13&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E7%A7%91%E5%B9%BB&type=17&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E7%94%BB&type=25&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E6%82%AC%E7%96%91&type=10&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E6%83%8A%E6%82%9A&type=19&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E6%81%90%E6%80%96&type=20&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E7%BA%AA%E5%BD%95%E7%89%87&type=1&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E7%9F%AD%E7%89%87&type=23&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E6%83%85%E8%89%B2&type=6&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E9%9F%B3%E4%B9%90&type=14&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E6%AD%8C%E8%88%9E&type=7&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E5%AE%B6%E5%BA%AD&type=28&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E5%84%BF%E7%AB%A5&type=8&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E4%BC%A0%E8%AE%B0&type=2&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E5%8E%86%E5%8F%B2&type=4&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E6%88%98%E4%BA%89&type=22&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E7%8A%AF%E7%BD%AA&type=3&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E8%A5%BF%E9%83%A8&type=27&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E5%A5%87%E5%B9%BB&type=16&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E5%86%92%E9%99%A9&type=15&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E7%81%BE%E9%9A%BE&type=12&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E6%AD%A6%E4%BE%A0&type=29&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E5%8F%A4%E8%A3%85&type=30&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E8%BF%90%E5%8A%A8&type=18&interval_id=100:90&action=',
          'https://movie.douban.com/typerank?type_name=%E9%BB%91%E8%89%B2%E7%94%B5%E5%BD%B1&type=31&interval_id=100:90&action='
]
print('豆瓣电影网监测ai，用于获取排行榜前200名，标题，评分，评论数，国家+总类被，演员；保存在csv表格')
print('注：若重复获取，后一个数据会代替前一个')
print('注：后多余重复内容需要自己删除')
print('作者：肖佳鑫')
print('只用于学习')
while True:
    a = input('请输入：')
    if a == '剧情':
        print('ai：正在准备……')
        print('ai：准备完成，正在获取 爬虫1 i……')
        try:
            url = list_url[0]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')


    if a == '喜剧':
        print('ai：正在准备……')

        print('ai：准备完成，正在获取……')
        try:
            url = list_url[1]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')

    if a == '动作':
        print('ai：正在准备……')

        print('ai：准备完成，正在获取……')
        try:
            url = list_url[2]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')



    if a == '爱情':
        print('ai：正在准备……')


        print('ai：准备完成，正在获取……')
        try:
            url = list_url[3]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')


    if a == '科幻':
        print('ai：正在准备……')

        print('ai：准备完成，正在获取……')
        try:
            url = list_url[4]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')



    if a == '动画':
        print('ai：正在准备……')


        print('ai：准备完成，正在获取……')
        try:
            url = list_url[5]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')

    if a == '悬疑':
        print('ai：正在准备……')

        print('ai：准备完成，正在获取……')
        try:
            url = list_url[6]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')

    if a == '惊悚':
        print('ai：正在准备……')

        print('ai：准备完成，正在获取……')
        try:
            url = list_url[7]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')


    if a == '恐怖':
        print('ai：正在准备……')

        print('ai：准备完成，正在获取……')
        try:
            url = list_url[8]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')


    if a == '纪录片':
        print('ai：正在准备……')

        print('ai：准备完成，正在获取……')
        try:
            url = list_url[9]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')


    if a == '短片':
       print('ai：正在准备……')

       print('ai：准备完成，正在获取……')
       try:
           url = list_url[10]
           find(get(url))
           print('ai:完毕')
       except Exception as e:
           print('ai:出现错误，请重试')


    if a == '情色':
       print('ai：正在准备……')

       print('ai：准备完成，正在获取……')
       try:
           url = list_url[11]
           find(get(url))
           print('ai:完毕')
       except Exception as e:
           print('ai:出现错误，请重试')



    if a == '音乐':
       print('ai：正在准备……')


       print('ai：准备完成，正在获取……')
       try:
           url = list_url[12]
           find(get(url))
           print('ai:完毕')
       except Exception as e:
             print('ai:出现错误，请重试')



    if a == '歌舞':
        print('ai：正在准备……')
        print('ai：准备完成，正在获取……')
        try:
            url = list_url[13]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')

    if a == '家庭':
        print('ai：正在准备……')

        print('ai：准备完成，正在获取……')
        try:
            url = list_url[14]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')

    if a == '儿童':
        print('ai：正在准备……')


        print('ai：准备完成，正在获取……')
        try:
            url = list_url[15]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')



    if a == '传记':
        print('ai：正在准备……')

        print('ai：准备完成，正在获取……')
        try:
            url = list_url[16]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')



    if a == '历史':
        print('ai：正在准备……')

        print('ai：准备完成，正在获取……')
        try:
            url = list_url[17]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')

    if a == '战争':
        print('ai：正在准备……')


        print('ai：准备完成，正在获取……')
        try:
            url = list_url[18]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')


    if a == '犯罪':
        print('ai：正在准备……')

        print('ai：准备完成，正在获取……')
        try:
            url = list_url[19]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')

    if a == '西部':
        print('ai：正在准备……')


        print('ai：准备完成，正在获取……')
        try:
            url = list_url[20]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')

    if a == '奇幻':
        print('ai：正在准备……')


        print('ai：准备完成，正在获取……')
        try:
            url = list_url[21]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')

    if a == ('冒险'):
        print('ai：正在准备……')


        print('ai：准备完成，正在获取……')
        try:
            url = list_url[22]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')

    if a == '灾难':
        print('ai：正在准备……')

        print('ai：准备完成，正在获取……')
        try:
            url = list_url[23]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')


    if a == '武侠':
        print('ai：正在准备……')


        print('ai：准备完成，正在获取……')
        try:
            url = list_url[24]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')

    if a == '古装':
        print('ai：正在准备……')


        print('ai：准备完成，正在获取……')
        try:
            url = list_url[25]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')

    if a == '运动':
        print('ai：正在准备……')


        print('ai：准备完成，正在获取……')
        try:
            url = list_url[26]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')

    if a == '黑色电影':
        print('ai：正在准备……')

        print('ai：准备完成，正在获取……')
        try:
            url = list_url[27]
            find(get(url))
            print('ai:完毕')
        except Exception as e:
            print('ai:出现错误，请重试')


    if a == 'exit':
        break