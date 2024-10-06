import time
import requests
from bs4 import BeautifulSoup

now = time.strftime("%Y%m%d_%H%M%S")

rent_url = "https://www.rakuya.com.tw/rent/rent_search"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
    "Referer": "https://www.rakuya.com.tw/rent/rent_search?search=&city=&zipcode=&keyword=&sort=&upd=",
    "Origin": "https://www.rakuya.com.tw"
}

params = {
    "search": "city",
    "city": "8",
    "zipcode": "403",
    "keyword": "學校",
    "sort": "21",
    "upd": "1"
}

response = requests.get(rent_url, headers=headers, params=params)

print(response.url)

if response.status_code == 200:
    print("OK")
    soup = BeautifulSoup(response.text, 'html.parser')
    with open(f"rakuya_pretty_{now}.html", "w", encoding="utf-8") as file:
        file.write(soup.prettify())
else:
    print(f"請求失敗，狀態：{response.status_code}")