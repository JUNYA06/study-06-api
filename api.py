import requests
import urllib
import pandas as pd


def get_api(url):
    
    return result.json()


def main():
    
    URL = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
    APP_ID = '1019079537947262807'

    params = {
    'applicationId' : APP_ID,
    'format':'json',
    'keyword':'鬼滅',
    }
    

    res = requests.get(URL,params)
    res.status_code
    result = res.json()
    items = result['Items']
    items_list = [item['Item'] for item in items]
    df_items = pd.DataFrame(items_list)[:3]
    print(df_items)

    # 課題6-2 商品名と価格の一覧を取得
    columns = [  'itemName', 'itemPrice','shopCode', 'shopName','reviewCount',
    'itemUrl']
    df = df_items[columns]
    print(df.head())

    #課題6-4 ランキングの出力
    # for obj in result["Items"]:
    #     print(f'rank: {obj["Item"]["rank"]} / item_name: {obj["Item"]["itemName"]}')


    # 課題6-4 CSVに出力
    # df_items.to_csv('test.csv',encoding="utf-8_sig")

main()