import requests
import urllib


def get_api(url):
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


def main():
    keyword = "鬼滅"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1019079537947262807".format(
        keyword)
<<<<<<< HEAD
    payload = {
    'hits': 30,#一度のリクエストで返してもらう最大個数（MAX30)
    'page':1,#何ページ目か
    'postageFlag':1,#送料込みの商品に限定
    }
    r = requests.get(url, params=payload)
    resp = r.json()
    total = int(resp['count'])
    Max = total/30 + 1
    print("【num of item】",total)
    print("【num of page】",Max)
    print("===================================")

    counter = 0
    for i in resp['Items']:
        counter = counter + 1
        item = i['Item']
        name = item['itemName']
        print('【No.】'+ str(counter)) 
        print('【Name】' + str(name[:30].encode('utf-8')) + '...')
        print('【Price】' + '¥' +str(item['itemPrice']))
        print('【URL】',item['itemUrl'])
        print('【shop】',item['shopName'])
        print('【text】', item['itemCaption'])


    # print(get_api(url))
=======

    print(get_api(url))
>>>>>>> bb69eec9cca8c48e84557e48ac02a85db9eb7825


main()

商
