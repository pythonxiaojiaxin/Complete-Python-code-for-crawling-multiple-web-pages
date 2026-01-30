from selenium import webdriver
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time
import csv
a = Options()
a.add_argument('user-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36 Edg/142.0.0.0')
d = webdriver.Edge(options=a)
r = []
g = []
for i in range(1, 25):
    url = 'https://chengdu.anjuke.com/sale/p{}/?from=esf_list'
    s = url.format(i)
    d.get(s)
    time.sleep(5)
    l = BeautifulSoup(d.page_source, 'html.parser')
    t = d.find_elements(By.CLASS_NAME, 'property-content-title-name')
    t = [e.text for e in t]
    g.append(t)
    i = d.find_elements(By.CLASS_NAME, 'property-price-average')
    i = [t.text for t in i]
    r.append(i)
r = sum(r,[])
g = sum(g,[])
if len(r) == len(g):
    with open('2','w',newline='',encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['name','prices'])
        for i,(g,r) in enumerate(zip(g,r),1):
            w.writerow([g,r])
