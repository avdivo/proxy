import requests
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def process():
    headers = dict(request.headers)
    data = request.get_data()
    cookies = dict(request.cookies)
    get_data = dict(request.args)
    print('-----', get_data)
    if request.method == 'POST':
        # Обработка POST
        data = request.get_json()
    else:
        # Обработка GET
        data = request.args

    response = requests.post("http://example.com/api", json=data)
    # result = response.json()

    print(f"Server response: {result}")

    return jsonify(result)


if __name__ == '__main__':
    app.run()

