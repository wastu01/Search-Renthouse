專案規劃內容： 

使用 Python BeautifulSoup 美麗湯套件進行爬蟲租屋網解析資料任務，定期回傳符合條件之租屋。

獲取的資料僅為個人使用，不會用於任何商業或營利用途，所有文字圖像內容為該網站所有。

Todo :

- 使用者可輸入參數 租金、地區、坪數 
- 資料清洗整理 ===> Regex or html css slect tag
- 資料排序 ===> Pandas sort, counter
- 傳送至 Line Notify
- 多頁資料

網址結構： 
`https://www.rakuya.com.tw/rent/rent_search?search=city&city=8&zipcode=403&keyword=學校&sort=21&upd=1`

全台灣縣市鄉鎮區郵遞區號：
`https://gist.github.com/wastu01/63bc811568fcefa1d54388a7b0287108`

