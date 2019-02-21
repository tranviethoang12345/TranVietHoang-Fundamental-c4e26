from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

#1. Create connection
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

#2 Download page
raw_data = conn.read()
content = raw_data.decode("utf8")

# with open("s.cafef.html", "wb") as f:
#     f.write(raw_data)

#3 Find AOI
soup = BeautifulSoup(page_content, "html.parser")
table = soup.find("table", id="tableContent")

#4 Extract AOI
tr_list = div.ul.find_all("tr") 

news_list = []

for tr in tr_list:
    h3 = tr.h3
    a = h3.a
    name = a.string

    h4 = tr.h4
    a = h4.a
    title = a.string 
    
    news = {
        "Name" : name,
        "Title" : title,
    }
    news_list.append(news)

#5 Save
pyexcel.save_as(records=news_list, dest_file_name="Topmusic.xlsx")