import requests
import urllib
import pandas as pd
import csv


#課題6-4 ランキング
def main():
    
    URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"
    APP_ID = '1019079537947262807'

    #キーワード入力、リクエストパラメーター作成
    params = {
    'applicationId' : APP_ID,
    'format':'json',
    'keyword':'鬼滅',
    }
    
    #APIを実行
    res = requests.get(URL,params)
    res.status_code
    result = res.json()
    items = result['Items']
    items_list = [item['Item'] for item in items]
    # df_items = pd.DataFrame(items_list)
    # print(df_items)


    #課題6-4 ランキングの出力
    item_info = {}
    for obj in items_list:
        
        item_info["item_name"] = obj["itemName"]
        item_info["item_rank"] = obj["rank"]
    print(item_info)
    
    # 課題6-4 CSVに出力
    with open('rank.csv','w',encoding="utf_8_sig") as f:
        writer =csv.writer(f)
        for k in item_info.items():
            writer.writerow([k])


    
    # df_items.to_csv('test.csv',encoding="utf-8_sig")

main()
