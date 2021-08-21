import requests
import urllib

REQUEST_URL = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706'
APP_ID = '1099071000661495268'


def search_items(keyword: str):

    params = {
        'keyword':keyword,
        'applicationId' : APP_ID,
        'format':'json',
        'minPrice':10000
    }

    res = execute_api(url=REQUEST_URL,params=params)

    



    result = requests.get(url)
    
    
    counter = 0
    for i in resp['Items']:
        counter = counter + 1
        item = i['Item']
        name = item['itemName']
            print '【No.】'+ str(counter)
        print '【Name】' + str(name[:30].encode('utf-8')) + '...'
        print '【Price】' + '¥' +str(item['itemPrice'])
        print '【URL】',item['itemUrl']
        print '【shop】',item['shopName']
        print '【text】', item['itemCaption']
    return result.json()


