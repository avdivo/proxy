import time

from flask import Flask, request, Response
import requests
import sys
import datetime

class Tee:
    def __init__(self):
        self.file = open('log.txt', 'a')
        self.stdout = sys.stdout
        sys.stdout = self

    def write(self, message):
        self.file.write(message)
        self.stdout.write(message)

    def flush(self):
        self.file.flush()
        self.stdout.flush()

    def close(self):
        if self.file:
            sys.stdout = self.stdout
            self.file.close()
            self.file = None


app = Flask(__name__)

@app.route('/store.tilda.cc/connectors/commerceml', methods=['GET', 'POST'])
def proxy():
    print(' ------------------------------ Вход ------------------------------')
    other_server_url = 'https://store.tilda.cc/connectors/commerceml'

    # Вывод заголовков
    print("Заголовки запроса:")
    headers = dict(request.headers)
    h = dict()
    if 'Authorization' in headers:
        h = {'Authorization': headers['Authorization']}
    if 'Cookie' in headers:
        h['Cookie'] = headers['Cookie']

    headers['Host'] = 'store.tilda.cc'
    print(headers)

    # Вывод текстового содержимого
    print("Текстовое содержимое:")
    data = request.data.decode()
    print(data)


    # Вывод cookies
    print("Куки:")
    cookies = request.cookies.to_dict()
    print(cookies)

    if request.method == 'GET':
        # Вывод содержимого GET
        print("Метод GET:")
        args = request.args.to_dict()
        print(args)
        res = requests.get(other_server_url, headers=headers, params=args, cookies=cookies)
    elif request.method == 'POST':
        # Вывод содержимого POST
        print("Метод POST")
        args = request.args.to_dict()
        print(args)
        res = requests.post(other_server_url, headers=headers, params=args, data=data, cookies=cookies)

    cookies = dict(res.cookies)
    print(f'\nОтвет текст: {res.text}')
    print(f'Заголовок: {res.headers}')
    print(f'Куки: {cookies}\n')

    print('----------------------------------------------------------------\n')
    response = Response(res, res.status_code)
    for cookie_name, cookie_value in cookies.items():
        response.set_cookie(cookie_name, cookie_value)

    return response


if __name__ == "__main__":
    tee = Tee()
    print(datetime.date.today(), datetime.datetime.now().time())

    app.run(debug=True)

    tee.close()
