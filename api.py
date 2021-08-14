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

    print(get_api(url))


main()
