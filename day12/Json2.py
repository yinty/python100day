import requests
import json


def main():
    resp = requests.get('http://api.tianapi.com/bulletin/?key=c5408714d0d663dac5a6785065abf767&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == '__main__':
    main()

