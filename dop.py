from flask import Flask, request, Response, jsonify
import requests
from requests.auth import HTTPBasicAuth


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def proxy():
    other_server_url = 'https://store.tilda.cc/connectors/commerceml'

    data = request.get_data()

    # Вывод заголовков
    print("Заголовки запроса:")
    headers = dict(request.headers)
    h = ''
    if 'Authorization' in headers:
        h = {'Authorization': headers['Authorization']}
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
        res = requests.get(other_server_url, headers=h, params=args)
    elif request.method == 'POST':
        # Вывод содержимого POST
        print("POST параметры:")
        args = request.form.to_dict()
        print(args)
        res = requests.post(other_server_url, headers=h, params=args, data=data)

    print(f'Response from remote server: {res.text}')

    response = Response(res, res.status_code)
    return response


if __name__ == "__main__":
    app.run(debug=True)