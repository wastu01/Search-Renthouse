import re
import time
import requests
from bs4 import BeautifulSoup
import pandas as pd

now = time.strftime("%Y%m%d_%H%M%S")

# region = input("輸入縣市")
region = "台中市"

cities = {
    "台北市": 0,
    "基隆市": 1,
    "新北市": 2,
    "宜蘭縣": 3,
    "桃園市": 4,
    "新竹市": 5,
    "新竹縣": 6,
    "苗栗縣": 7,
    "台中市": 8,
    "彰化縣": 9,
    "南投縣": 10,
    "雲林縣": 11,
    "嘉義市": 12,
    "嘉義縣": 13,
    "台南市": 14,
    "高雄市": 15,
    "澎湖縣": 16,
    "屏東縣": 17,
    "台東縣": 18,
    "花蓮縣": 19,
    "金門連江": 20
}

if region in cities:
    city_code = cities[region]
else:
    print("請重新輸入")
    exit()
  
zipcode = "403"

keyword = "西區"

sort = "21"

upd = "1"

rent_url = "https://www.rakuya.com.tw/rent/rent_search"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Referer": f"https://www.rakuya.com.tw/rent/rent_search?search=city&city={city_code}&zipcode={zipcode}&keyword=&sort={sort}&upd={upd}",
    "Origin": "https://www.rakuya.com.tw"
}

params = {
    "search": "city",
    "city": city_code,
    "zipcode": zipcode,
    "keyword": keyword,
    "sort": sort,
    "upd": upd
}

response = requests.get(rent_url, headers=headers, params=params)

print(response.url)

if response.status_code == 200:
    print("OK")
    soup = BeautifulSoup(response.text, 'html.parser')
    # with open(f"rakuya_pretty_{now}.html", "w", encoding="utf-8") as file:
    #     file.write(soup.prettify())
        
    # 篩選條件
    tags = soup.select('.block-search-tags')
    for tag in tags:
        clean_text = ' '.join(tag.text.split())
        print(repr(clean_text))
    
    container = soup.select_one('div.content.type-list')
    rental_info_list = []

    if container:
        obj_items = container.find_all(class_="obj-item")

        for idx, item in enumerate(obj_items):
            # 物件連結
            link = item.select_one('a')['href']
            background_image = item.select_one('a')['style'].split("url('")[1].split("')")[0]

            # 物件標題位置
            title = item.select_one('.obj-title h6 a').text.strip()
            location = item.select_one('.obj-address').text.strip()
            status = item.select_one('.obj-status').text.strip()
            

            # 物件價格
            price_text = ''.join(item.select_one('.obj-price span').text.split())  # 去除空格和換行符 
            price = int(re.sub(r'[^\d]', '', price_text))

            # 屋型、房型、坪數、樓層
            house_type = item.select_one('ul.obj-data li:nth-of-type(2) span:nth-of-type(1)').text.strip()
            room_type = item.select_one('ul.obj-data li:nth-of-type(2) span:nth-of-type(2)').text.strip()
            area_size = item.select_one('ul.obj-data li:nth-of-type(3) span:nth-of-type(1)').text.strip()
            floor = item.select_one('ul.obj-data li:nth-of-type(3) span:nth-of-type(2)').text.strip()
            
            
            # 更新時間
            update_time_text = item.select_one('.obj-update .sub06-c b').text.strip()
            # print(update_time_text)
            if '分鐘前更新' in update_time_text:
                update_time = int(re.sub(r'[^\d]', '', update_time_text))
            elif '秒前更新' in update_time_text:
                update_time = round(int(re.sub(r'[^\d]', '', update_time_text)) / 60, 2)
            else:
                update_time = 0

            # 瀏覽次數
            views_text = item.select_one('.obj-update').text.split('瀏覽次數：')[-1].strip()

            if '新上架' in views_text:
                views = 0
            else:
                views = int(views_text.split('次')[0])
            
            print(f"物件狀態：{status}")
            print(f"物件標題: {title}, 位置: {location}")
            print(f"價格: {price} 元")
            print(f"更新日期：{update_time}")
            print(f"觀看次數：{views}")
            print(house_type)
            print(room_type)
            print(area_size)
            print(floor)

else:
    print(f"請求失敗，狀態：{response.status_code}")