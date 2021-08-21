import requests
import urllib
import pandas as pd


def get_api(url):
    
    return result.json()


def main():
    
    URL = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?"
    APP_ID = '1019079537947262807'

    params = {
    'applicationId' : APP_ID,
    'format':'json',
    'keyword':'鬼滅',
    }
    

    res = requests.get(URL,params)
    result = res.json()

    for obj in result["Products"]:
        print(f'product_name: {obj["Product"]["productName"]} / max_price: {obj["Product"]["maxPrice"]} / min_price: {obj["Product"]["minPrice"]}')
main()