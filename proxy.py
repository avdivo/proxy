from flask import Flask, request, Response
import requests


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def proxy():
    other_server_url = 'https://store.tilda.cc/connectors/commerceml'

    data = request.get_data()

    # Вывод заголовков
    print("Заголовки запроса:")
    headers = dict(request.headers)
    h = dict()
    if 'Authorization' in headers:
        h = {'Authorization': headers['Authorization']}
    if 'Cookie' in headers:
        h['Cookie'] = headers['Cookie']
    print(headers)

    # Вывод текстового содержимого
    print("Текстовое содержимое:")
    data = request.get_data()
    print(data)

    # Вывод cookies
    print("Куки:")
    cookies = request.cookies.to_dict()
    print(cookies)

    if request.method == 'GET':
        # Вывод содержимого GET
        print("GET параметры:")
        args = request.args.to_dict()
        print(args)
        res = requests.get(other_server_url, headers=h, params=args, cookies=cookies)
    elif request.method == 'POST':
        # Вывод содержимого POST
        print("POST параметры:")
        args = request.args.to_dict()
        print(args)
        res = requests.post(other_server_url, headers=h, params=args, data=data, cookies=cookies)

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
    app.run(debug=True)