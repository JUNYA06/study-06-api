import requests
import pandas as pd

REQUEST_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
APP_ID = '1099071000661495268'

params = {
    'applicationId' : APP_ID,
    'format':'json',
    'keyword':'毀滅',
    'minPrice':10000
}

res = requests.get(REQUEST_URL,params)
res.status_code
result = res.json()
items = result['Items']

df = pd.DataFrame(items)[:3]

# 内包表記
items_list = [item['Item'] for item in items]
df_items = pd.DataFrame(items_list)[:3]
print(df_items)




columns = [ 'availability', 'shopAffiliateUrl',
'itemCode',  'itemName', 'itemPrice','shopCode', 'shopName', 'reviewCount',
 'itemUrl']
df = df_items[columns]
df_items.to_csv('test.csv')