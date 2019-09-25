import json
import csv


def main():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open('data.json', 'w', encoding='UTF-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('数据保存完成！')


if __name__ == '__main__':
    main()


json_str = '{"name": "骆昊", "age": 38, "title": "叫兽"}'
result = json.loads(json_str)
print(result)
print(type(result))
print(result['name'])
print(result['age'])
